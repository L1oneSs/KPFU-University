import Image from 'next/image';
import { Router, Trash } from 'lucide-react';
import { HiOutlineShoppingBag } from 'react-icons/hi';
import {
	Popover,
	PopoverContent,
	PopoverTrigger,
} from "@/components/ui/popover";
import { ScrollArea } from "@/components/ui/scroll-area";
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import basketService from '@/services/basketService';
import { IBasket } from '@/interface/IBasket';
import toast from 'react-hot-toast';
import { BeatLoader } from 'react-spinners';
import { Button } from '@/components/ui/button';
import { useRouter } from 'next/navigation';
import orderService from '@/services/orderService';

interface IdeleteProductFromBasket {
	productId: string
};

interface IChangeCountProductInBasket {
	productId: string;
	changeCount: string;
};

interface IPay {
	arrProductId: string[]
}

export const BasketShop = () => {

	const queryClient = useQueryClient();
	const router = useRouter();

	var totalPrice = 0;

	const { data: basketShop, isLoading, isSuccess: isBasketShopSucces } = useQuery({
		queryKey: ['basket-get-data'],
		queryFn: () => basketService.get(),
		select: ({ data }) => data
	});

	isBasketShopSucces && Array.isArray(basketShop) && basketShop.map((itemBasketShop: IBasket) => {
		totalPrice += itemBasketShop.productPrice * itemBasketShop.productCount;
	});

	const { mutate: deleteMutation, isSuccess: isDeleteMutationSucces, isPending: isDeleteMutationPending } = useMutation({
		mutationKey: ['delete-basket'],
		mutationFn: (values: IdeleteProductFromBasket) => basketService.delete(values),
		onSuccess: (data) => {
			toast.success(data.data.success);
			queryClient.invalidateQueries({ queryKey: ['basket-get-data'] });
		}
	})

	const { mutate: changeMutation, isSuccess: isChangeMutationSuccess, isPending: isChangeMutatuionPending } = useMutation({
		mutationKey: ['change-basket'],
		mutationFn: (values: IChangeCountProductInBasket) => basketService.update(values),
		onSuccess: (data) => {
			toast.success(data.data.success);
			queryClient.invalidateQueries({ queryKey: ['basket-get-data'] });
		}
	})

	const { mutate: payMutation, isSuccess: payMutationSuccess, isPending: payMutatuionPending } = useMutation({
		mutationKey: ['pay'],
		mutationFn: (values: IPay) => orderService.create(values),
		onSuccess: (data) => {
			router.push(`/shop/pay?order=${data.data.id}`)
		}
	})

	// console.log(basketShop);


	const onPay = () => {
		var arrProductId: string[] = [];
		isBasketShopSucces && Array.isArray(basketShop) && basketShop.map((itemBasketShop: IBasket) => {
			arrProductId.push(itemBasketShop.productId);
		});

		const values = {
			arrProductId,
		};
		payMutation(values);
	}

	const onDeleteItemFromBasket = (productId: string) => {
		const values = {
			productId
		}
		deleteMutation(values);
	};

	const onChange = (productId: string, changeCount: string) => {
		const values = {
			productId,
			changeCount
		};
		changeMutation(values);
	}

	return (
		<Popover>
			<PopoverTrigger>
				<HiOutlineShoppingBag className='w-[18px] h-[18px] text-white hover:text-[#9466ff]' />
			</PopoverTrigger>
			<PopoverContent className='md:w-[200px] lg:w-[480px] p-3'>
				<div className='grid grid-flow-col col-[1fr_20px] mb-[6px] border-b-2'>
					<h2 className='font-bold text-xl text-center grid justify-center'>
						Корзина
					</h2>
				</div>
				<ScrollArea className="min-h-[50px] max-h-[150px] w-[450px] mb-[6px] border-b-2 overflow-y-scroll">
					{isLoading && <div className='grid justify-center'><BeatLoader className='grid grid-flow-col my-6' /></div>}


					{isBasketShopSucces && basketShop.map((product: IBasket) => (
						<div key={product.productId} className='grid grid-flow-col grid-cols-[80px_1fr] gap-1 py-[6px]'>

							<div className='relative h-[80px] w-[80px]'>
								<Image src={`/${product.productImage}`} alt='product' fill className='object-fill' />
							</div>
							<div className='grid grid-rows-[1fr_20px]'>
								<div className='grid grid-flow-col grid-cols-[1fr_20px] gap-2 p-2 pr-0'>
									<h3>{product.productName}</h3>
									<Trash className='w-[20px] h-[20px] cursor-pointer' onClick={() => onDeleteItemFromBasket(product.productId)} />
								</div>
								<div className='grid grid-flow-col grid-cols-[2fr_1fr] gap-3'>
									<div className='rounded-xl bg-muted grid grid-flow-col grid-cols-3'>
										<span onClick={() => onChange(product.productId, 'minus')} className='grid justify-center cursor-pointer'>-</span>
										<span className='grid justify-center'>{product.productCount}</span>
										<span onClick={() => onChange(product.productId, 'plus')} className='grid justify-center cursor-pointer'>+</span>
									</div>
									<p className='grid justify-end'>
										{product.productPrice} P
									</p>
								</div>
							</div>
						</div>
					))}
				</ScrollArea>
				<div>
					<div className='grid grid-flow-col grid-cols-[2fr_1fr] gap-3 my-2'>
						<p>
							Сумма заказа:
						</p>
						<p className='grid justify-end'>
							{totalPrice} ₽
						</p>
					</div>
					<Button className='w-full' onClick={onPay}>
						Оформить заказ
					</Button>
				</div>
			</PopoverContent>

		</Popover>

	);
};