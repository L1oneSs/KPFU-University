'use client';

import { DropdownMenu, DropdownMenuContent, DropdownMenuItem, DropdownMenuTrigger } from '@/components/ui/dropdown-menu';
import { Avatar, AvatarImage, AvatarFallback } from '@/components/ui/avatar';
import { FaUser } from 'react-icons/fa';
import { ExitIcon } from '@radix-ui/react-icons';
import { useCurrentUser } from '@/hooks/useCurrentUser';
import { LogoutButton } from './logoutButton';
import { Button } from '@/components/ui/button';
import Link from 'next/link';

export const UserButton = () => {
	const user = useCurrentUser();

	return (
		<div className='grid items-center'>
			<DropdownMenu>
				<DropdownMenuTrigger>
					<Avatar>
						<AvatarImage src={user?.image || ''} alt='avatar image' />
						<AvatarFallback className='bg-sky-500'>
							<FaUser className='text-white' />
						</AvatarFallback>
					</Avatar>
				</DropdownMenuTrigger>
				<DropdownMenuContent className='w-40' align='end'>
					<DropdownMenuItem>
						<Link href='/profile'>
							Профиль
						</Link>
					</DropdownMenuItem>
					<DropdownMenuItem>
						<Link href='/write'>
							Новая запись
						</Link>
					</DropdownMenuItem>
					<DropdownMenuItem>
						<Link href='/settings'>
							Настройки
						</Link>
					</DropdownMenuItem>
					<LogoutButton>
						<DropdownMenuItem>
							<ExitIcon className='h-4 w-4 mr-2' />
							Выйти
						</DropdownMenuItem>
					</LogoutButton>
				</DropdownMenuContent>
			</DropdownMenu>
		</div>
	)
};