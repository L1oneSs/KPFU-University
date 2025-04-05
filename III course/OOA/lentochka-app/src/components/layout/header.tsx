"use client"

import React, { useState } from 'react';
import logo from "/public/logo.png";
import { Button, Popover, MenuItem } from '@mui/material';
import copy from 'clipboard-copy';
import { toast } from 'react-hot-toast';
import { useRouter } from 'next/navigation';
import { signOut, useSession } from 'next-auth/react';


export const Header = () => {
	const session = useSession();
	const router = useRouter();
	
	const [anchorEl, setAnchorEl] = useState<null | HTMLElement>(null);
	const [aboutAnchorEl, setAboutAnchorEl] = useState<null | HTMLElement>(null);

	const handleClick = (event: React.MouseEvent<HTMLButtonElement>) => {
		setAnchorEl(event.currentTarget);
	};

	const handleClick_2 = (event: React.MouseEvent<HTMLButtonElement>) => {
		setAboutAnchorEl(event.currentTarget);
	};

	const handleClose = () => {
		setAnchorEl(null);
	};

	const handleClose_2 = () => {
		setAboutAnchorEl(null);
	};

	const handleOptionClick = (option: string, text: string) => {
		copy(text); // Копировать текст в буфер обмена
		handleClose(); // Закрыть Popover
		toast.success(`Текст "${text}" скопирован`); // Вывести уведомление
	};

	const handleTechSupportClick = () => {
		window.location.href = 'mailto:lentochka_support@gmail.com';
	};

	const openSigninPage = () => {
		router.push('/auth/login');
	}

	const openSignoutPage = () => {
		signOut();
	}


	return (
		<div className="bg-white text-gray-900 py-4 px-8 flex justify-between items-center relative">
			<div className="flex items-center">
				<img src={logo.src} alt="Логотип" className="h-14 object-contain mr-5" />
				<div className="ml-6 flex items-center gap-8">
					<Button onClick={handleClick}>Контакты</Button>
					<Popover
						open={Boolean(anchorEl)}
						anchorEl={anchorEl}
						onClose={handleClose}
						anchorOrigin={{
							vertical: 'bottom',
							horizontal: 'center',
						}}
						transformOrigin={{
							vertical: 'top',
							horizontal: 'center',
						}}
					>
						<MenuItem onClick={() => handleOptionClick('email', 'lentochka@gmail.com')}>Email: lentochka@gmail.com</MenuItem>
						<MenuItem onClick={() => handleOptionClick('phone', '8999999999')}>Phone: 8999999999</MenuItem>
					</Popover>
					<Button onClick={handleClick_2}>О нас</Button>
					<Popover
						open={Boolean(aboutAnchorEl)}
						anchorEl={aboutAnchorEl}
						onClose={handleClose_2}
						anchorOrigin={{
							vertical: 'bottom',
							horizontal: 'center',
						}}
						transformOrigin={{
							vertical: 'top',
							horizontal: 'center',
						}}
					>
						<p>
							Очень важная информация о лучшей
						</p>
						<p>
							компании на свете, которая предоставит
						</p>
						<p>
							все услуги практически бесплатно под
						</p>
						<p>
							большой процент.
						</p>
					</Popover>
					<button onClick={handleTechSupportClick}>Техподдержка</button>
				</div>
			</div>
			<div className="flex bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded mr-2">
				{session.status === "unauthenticated" && (
					<button onClick={openSigninPage}>Войти</button>
				)}
				{session.status === "authenticated" && (
					<button onClick={openSignoutPage}>Выйти</button>
				)}
			
			</div>
		</div>
	);
};
