'use client';

import { Card, CardContent } from "@/components/ui/card"
import {
	Carousel,
	CarouselContent,
	CarouselItem,
	CarouselNext,
	CarouselPrevious,
} from "@/components/ui/carousel"
import { ICategory } from '@/interface/ICategory';
import categoryService from '@/services/categoryService';
import { useQuery } from '@tanstack/react-query'
import Image from 'next/image';
import Link from 'next/link';
import { BeatLoader } from 'react-spinners';

export function CategoryList() {

	const { data: categoriesData, isLoading, isSuccess } = useQuery({
		queryKey: ['categories'],
		queryFn: () => categoryService.getAll(),
		select: ({ data }) => data
	})

	return (
		<div className='pt-6 px-14'>
			<h2 className='text-2xl text-foreground mb-3'>Категории: </h2>
			{isLoading && <div className='grid justify-center'><BeatLoader className='grid grid-flow-col my-6' /></div>}

			{isSuccess && <Carousel
				opts={{
					align: "start",
				}}
			>
				<CarouselPrevious />
				<CarouselContent>
					{isSuccess && categoriesData.map((category: ICategory) => (
						<CarouselItem key={category.id} className="basis-1/6 ">

							<Link href={`/shop?category=${category.tag}`} className="border-gray-400 border rounded-md grid grid-cols-[40px_1fr] items-center justify-center gap-2 min-h-[80px] px-3">
								{category.img &&
									<Image
										src={`/${category.img}`}
										alt={category.title}
										width={32}
										height={32}
										objectFit='cover'
										className='rounded-[50%] h-[32px]'
									/>
								}
								<p className="text-md font-semibold">{category.title}</p>
							</Link>

						</CarouselItem>
					))}
				</CarouselContent>

				<CarouselNext />
			</Carousel>}
		</div>
	)
}
