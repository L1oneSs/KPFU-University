'use client';

import productService from '@/services/productService';
import { useQuery } from '@tanstack/react-query';
import { IProduct } from '@/interface/IProduct';
import { Product } from '@/components/widgets/product';
import { BeatLoader } from 'react-spinners';

interface ProductListProps {
	category: string;
};


export const ProductList = ({ category }: ProductListProps) => {
	const { data: productData, isSuccess, isLoading } = useQuery({
		queryKey: ['product', category],
		queryFn: () => productService.getByCategory(category),
		select: ({ data }) => data
	});


	return (
		<div className='pt-6 px-14'>
			<h2 className='text-2xl text-foreground mb-3'>{category.toLocaleUpperCase()}</h2>
			{isLoading && <div className='grid justify-center'><BeatLoader className='grid grid-flow-col my-6' /></div>}
			<div className='p-6 grid grid-cols-4'>
				{Array.isArray(productData) && productData.map((product: IProduct) => (
					<Product product={product} key={product.id} />
				))}
			</div>
		</div>
	);
};