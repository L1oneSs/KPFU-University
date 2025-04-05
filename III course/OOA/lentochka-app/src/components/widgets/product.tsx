'use client';

import { IProduct } from '@/interface/IProduct';
import { Card, CardContent, CardFooter, CardHeader, CardTitle } from '@/components/ui/card';
import Image from 'next/image';
import { truncateText } from '@/helpers';
import { Button } from '@/components/ui/button';
import { useMutation, useQueryClient } from '@tanstack/react-query';
import basketService from '@/services/basketService';
import { toast } from 'react-hot-toast';

interface ProductProps {
	product: IProduct;
}

interface IClickProductInBasket {
	productId: string
}

export const Product = ({ product }: ProductProps) => {

	const queryClient = useQueryClient();

	const { mutate, isPending, isSuccess } = useMutation({
		mutationKey: ['basket-add-data'],
		mutationFn: (values: IClickProductInBasket) => basketService.create(values),
		onSuccess(data: any) {
			toast.success(data.data.success);
			queryClient.invalidateQueries({ queryKey: ['basket-get-data'] });
		},
	});

	const onClick = (productId: string) => {
		const values = {
			productId
		};
		mutate(values)
	}

	return (
		<Card>
			<CardHeader>
				<CardTitle>
					{product.name}
				</CardTitle>
			</CardHeader>
			<CardContent className='p-6'>
				{product.image &&
					<div className='h-[200px] relative'>
						<Image src={`/${product.image}`} alt={product.name} className='object-cover' fill />
					</div>
				}
				<div dangerouslySetInnerHTML={{ __html: truncateText(product.description, 52) }} />
				<div>
					<p>Цена: <span>{product.price}</span></p>
				</div>
			</CardContent>
			<CardFooter>
				<Button className='w-full' onClick={() => onClick(product.id)}>Купить</Button>
			</CardFooter>
		</Card>
	);
}