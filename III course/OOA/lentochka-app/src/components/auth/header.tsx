import { Poppins } from 'next/font/google';
import { cn } from '@/lib/utils';

const font = Poppins({
	subsets: ['latin'],
	weight: ['600']
});

interface HeaderProps {
	label: string
};

export const Header = ({ label }: HeaderProps) => {
	return (
		<div className='w-full grid gap-y-4 items-center justify-center'>
			<h1 className={cn(
				'text-3xl font-semibold text-center',
				font.className
			)}>
				Авторизация
			</h1>
			<p className='text-muted-foreground text-center text-sm'>{label}</p>
		</div>
	);
};