'use client';

import { CiSearch } from "react-icons/ci";
import Image from 'next/image';
import Link from 'next/link';
import {
	Popover,
	PopoverContent,
	PopoverTrigger,
} from "@/components/ui/popover";
import { Input } from '@/components/ui/input';
import { Search } from 'lucide-react';
import { ScrollArea } from "@/components/ui/scroll-area"
import { Button } from '@/components/ui/button';


export const ModalSearch = () => {
	return (
		<Popover>
			<PopoverTrigger>
				<CiSearch className='w-[18px] h-[18px] text-white hover:text-[#9466ff]' />
			</PopoverTrigger>
			<PopoverContent className='md:w-[200px] lg:w-[480px]'>
				<div className="relative ml-auto flex-1 md:grow-0">
					<Search className="absolute left-2.5 top-2.5 h-4 w-4 text-muted-foreground" />
					<Input
						type="search"
						placeholder="Названия товара..."
						className="w-full rounded-lg bg-background pl-8 md:w-[200px] lg:w-[450px]"
					/>
					<ScrollArea className="min-h-[50px] max-h-[150px] lg:w-[450px]">
						<div className='grid grid-flow-col grid-cols-[80px_1fr_100px] gap-1 p-3 pb-0'>
							<div className='relative h-[80px] w-[80px]'>
								<Image src='/product.jpg' alt='product' fill className='object-fill' />
							</div>
							<div>
								<h3>Title</h3>
								<p>description</p>
							</div>
							<div className='grid grid-flow-row'>
								<p className='text-center'>3200 Руб</p>
								<Button>
									Купить
								</Button>
								<Button
									size='sm'
									variant='link'
									asChild
									className='px-0 font-normal'
								>
									<span>
										В избранное
									</span>
								</Button>
							</div>
						</div>
					</ScrollArea>
				</div>
			</PopoverContent>
		</Popover>
	);
};