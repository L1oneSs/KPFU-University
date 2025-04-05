import {
	Popover,
	PopoverContent,
	PopoverTrigger,
} from "@/components/ui/popover";
import { ScrollArea } from "@/components/ui/scroll-area";
import { useQuery, useQueryClient } from '@tanstack/react-query';
import orderBasketService from '@/services/orderBasket';
import { BeatLoader } from 'react-spinners';
import Image from 'next/image';
import { PiListPlus } from "react-icons/pi";
import { formatTime, truncateText } from '@/helpers';


export const OrderBasket = () => {

	const { data: orderBasketData, isLoading, isSuccess: isSucces } = useQuery({
		queryKey: ['order-basket'],
		queryFn: () => orderBasketService.getAll(),
		select: ({ data }) => data
	});

	console.log(orderBasketData);


	return (
		<Popover>
			<PopoverTrigger>
				<PiListPlus className='w-[18px] h-[18px] text-white hover:text-[#9466ff]' />
			</PopoverTrigger>
			<PopoverContent className='md:w-[200px] lg:w-[480px] p-3'>
				<div className='grid grid-flow-col col-[1fr_20px] mb-[6px] border-b-2'>
					<h2 className='font-bold text-xl text-center grid justify-center'>
						Заказы
					</h2>
				</div>
				<ScrollArea className="min-h-[50px] max-h-[150px] w-[450px] mb-[6px] border-b-2 overflow-y-scroll">
					{isLoading && <div className='grid justify-center'><BeatLoader className='grid grid-flow-col my-6' /></div>}


					{isSucces && orderBasketData.map((order: any) => (
						<div key={order.productId} className='grid grid-flow-col grid-cols-[80px_1fr] gap-1 py-[6px]'>

							<div className='relative h-[80px] w-[80px]'>
								<Image src={`/${order.productImage}`} alt='product' fill className='object-fill' />
							</div>
							<div className='grid grid-rows-[1fr_20px] p-2 pr-0'>
								<div className='grid grid-flow-col grid-rows-2 gap-2'>
									<h3>{order.productName}</h3>
									<div dangerouslySetInnerHTML={{ __html: truncateText(order.productDescription, 26) }} />
								</div>
								<div className='grid grid-cols-2 justify-evenly'>
									<p>{order.status}</p>
									<p>{order.status === 'Оплачено' && formatTime(order.deliveryDate)}</p>
								</div>
							</div>
						</div>
					))}
				</ScrollArea>
			</PopoverContent>

		</Popover>

	);
};