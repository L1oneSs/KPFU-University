'use client';

import Link from 'next/link';
import { IoIosMenu } from "react-icons/io";
import { Button } from '@/components/ui/button';
import {
	DropdownMenu,
	DropdownMenuContent,
	DropdownMenuItem,
	DropdownMenuLabel,
	DropdownMenuPortal,
	DropdownMenuSeparator,
	DropdownMenuSub,
	DropdownMenuSubContent,
	DropdownMenuSubTrigger,
	DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu"
import {
	HoverCard,
	HoverCardContent,
	HoverCardTrigger,
} from "@/components/ui/hover-card"


export const MenuShop = () => {
	return (
		<DropdownMenu>
			<DropdownMenuTrigger
				asChild
				className='w-[200px] bg-transparent border-none text-white grid grid-flow-col gap-2 items-center justify-start hover:text-[#9466ff] hover:bg-transparent hover:bg-none active:bg-transparent '
			>
				<Button variant="outline"><IoIosMenu /> Меню</Button>
			</DropdownMenuTrigger >
			<DropdownMenuContent >
				<DropdownMenuSub>
					<DropdownMenuSubTrigger>
						Каталог
					</DropdownMenuSubTrigger>
					<DropdownMenuPortal>
						<DropdownMenuSubContent>
							<DropdownMenuSub>
								<DropdownMenuSubTrigger>
									Одежда
								</DropdownMenuSubTrigger>
								<DropdownMenuPortal>
									<DropdownMenuSubContent>
										<DropdownMenuItem>
											<Link href='/catalog/cloth?offset=0&type=t-shirts'>
												Футболка
											</Link>
										</DropdownMenuItem>
									</DropdownMenuSubContent>
								</DropdownMenuPortal>
							</DropdownMenuSub>
							<DropdownMenuSeparator />
							<DropdownMenuItem>И так далее...</DropdownMenuItem>
						</DropdownMenuSubContent>
					</DropdownMenuPortal>
				</DropdownMenuSub>
				<DropdownMenuSub>
					<DropdownMenuSubTrigger>
						Покупателям
					</DropdownMenuSubTrigger>
					<DropdownMenuPortal>
						<DropdownMenuSubContent>
							<DropdownMenuItem>
								<Link href='/about'>
									О нас
								</Link>
							</DropdownMenuItem>
							<DropdownMenuItem>
								<Link href='/blog'>
									Блог
								</Link>
							</DropdownMenuItem>
							<DropdownMenuItem>
								<Link href='/shipping-and-playment'>
									Доставка и оплата
								</Link>
							</DropdownMenuItem>
							<DropdownMenuItem>
								<Link href='/purchase-returns'>
									Возврат товара
								</Link>
							</DropdownMenuItem>
						</DropdownMenuSubContent>
					</DropdownMenuPortal>
				</DropdownMenuSub>
				<DropdownMenuItem>
					<HoverCard>
						<HoverCardTrigger>Контакты</HoverCardTrigger>
						<HoverCardContent>
							<p>Телефон:</p>
							<p>Email:</p>
							<p>Адрес:</p>
						</HoverCardContent>
					</HoverCard>
				</DropdownMenuItem>
			</DropdownMenuContent >
		</DropdownMenu >
	);
};	