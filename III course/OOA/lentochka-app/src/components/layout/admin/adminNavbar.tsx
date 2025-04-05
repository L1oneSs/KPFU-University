'use client';

import { Button } from '@/components/ui/button';
import Link from 'next/link';
import { usePathname } from 'next/navigation';


export const AdminNavbar = () => {
	const pathname = usePathname();

	return (
		<nav className='grid grid-flow-col grid-cols-2 gap-x-2 items-center p-4 border-b w-[1200px] xl:w-[1024px] lg:w-[767px] md:w-[650px] sm:w-[300px] shadow-md'>
			<Button
				asChild
				variant={pathname === '/admin/control' ? 'default' : 'outline'}
				className='md:text-sm sm:text-xs'
			>
				<Link href='/admin/control'>
					Управление
				</Link>
			</Button>
			<Button
				asChild
				variant={pathname === '/admin/new-product' ? 'default' : 'outline'}
				className='md:text-sm sm:text-xs'
			>
				<Link href='/admin/new-product'>
					CMS
				</Link>
			</Button>
		</nav>
	);
};