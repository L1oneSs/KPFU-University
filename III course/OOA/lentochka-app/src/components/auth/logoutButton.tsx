'use client';

import { signOut } from 'next-auth/react';
import { Button } from '../ui/button';

interface logoutButtonProps {
	children?: React.ReactNode;
};


export const LogoutButton = ({ children }: logoutButtonProps) => {
	const onClick = () => {
		signOut();
	};

	return (
		<Button  onClick={onClick} className='cursor-pointer'>
			{children}
		</Button>
	);
};