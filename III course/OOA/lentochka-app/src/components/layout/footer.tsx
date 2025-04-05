"use client"

import React from 'react';

export const Footer = () => {
	return (
		<footer className="bg-gray-900 text-white py-8 w-full">
			<div className="container mx-auto flex flex-col md:flex-row justify-between px-4">
				<div className="flex flex-col items-center">
					<p className="text-xs">©2024 "Joyful Presents Co."</p>
					<p className="text-xs">Все права защищены.</p>
				</div>
				<div className="flex items-center mt-4 md:mt-0">
					<p className="mr-8"></p>
					<ul className="text-sm flex space-x-8">
						<li>
							<a href="#" className="hover:text-gray-300">Условия использования</a>
						</li>
						<li>
							<a href="#" className="hover:text-gray-300">Политика конфиденциальности</a>
						</li>
					</ul>
				</div>
			</div>
		</footer>
	);
};
