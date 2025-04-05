'use client';

import { Card, CardHeader, CardContent } from '@/components/ui/card';
import { Button } from '@/components/ui/button';
import { Input } from '@/components/ui/input';
import { Form, FormControl, FormItem, FormLabel, FormMessage, FormField, FormDescription } from '@/components/ui/form';
import { FormError } from '@/components/formError';
import { FormSuccess } from '@/components/formSuccess';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/components/ui/select';
import { Switch } from '@/components/ui/switch';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { PaySchema, SettingsSchema } from '@/schemas';
import * as z from 'zod';
import settingsService from '@/services/settingsService';
import { useState } from 'react';
import { useCurrentUser } from '@/hooks/useCurrentUser';
import { UserRole } from '@prisma/client';
import { Footer } from '@/components/layout/footer';
import { Header } from '@/components/layout/header';
import Sidebar from '@/components/Sidebar';
import payService from '@/services/payService';
import toast from 'react-hot-toast';
import { useRouter } from 'next/navigation';


export default function PayPage({ searchParams }: any) {
	
	const queryClient = useQueryClient();
	const router = useRouter();
	const orderId = searchParams.order;

	const form = useForm<z.infer<typeof PaySchema>>({
		resolver: zodResolver(PaySchema),
	});

	const { data: totalPrice, isLoading, isSuccess } = useQuery({
		queryKey: ['totalPrice-data'],
		queryFn: () => payService.get(orderId),
		select: ({ data }) => data
	});

	const mutation = useMutation({
		mutationKey: ['pay-mutation'],
		mutationFn: (val: z.infer<typeof PaySchema>) => payService.update(val, orderId),
		onSuccess: (data: any) => {
			toast.success('Товар оплачен!');
			queryClient.invalidateQueries({
				queryKey: ['order-basket']
			});
			router.push('/shop');
		},
		onError: (error: any) => {
			console.log(error.message);
		}
	});

	const onSubmit = (values: z.infer<typeof PaySchema>) => {
		mutation.mutate(values);
	};

	return (
		<div>
			<div className="flex flex-row">
				<div className="flex-grow">
					<div className='grid items-center justify-center min-h-screen bg-[radial-gradient(ellipse_at_top,_var(--tw-gradient-stops))] bg-repeat bg-cover' style={{ backgroundImage: 'url("back2.jpg")', backgroundSize: 'auto' }}>
						<Card className='w-[600px] md:w-[450px] sm:w-[300px]'>
							<CardHeader>
								<p className='text-2xl font-semibold text-center'>
									Оплата
								</p>
							</CardHeader>
							<CardContent>


								<Form {...form}>
									<form
										className='space-y-6'
										onSubmit={form.handleSubmit(onSubmit)}
									>
										<div className='space-y-4'>

											<FormField
												control={form.control}
												name='cardNumber'
												render={({ field }) => (
													<FormItem>
														<FormLabel>Номер карты</FormLabel>
														<FormControl>
															<Input
																{...field}
																placeholder='4276 8943 8800 7823'
																disabled={mutation.isPending}
															/>
														</FormControl>
														<FormMessage />
													</FormItem>
												)}
											/>
											<FormField
												control={form.control}
												name='date'
												render={({ field }) => (
													<FormItem>
														<FormLabel>Действует до</FormLabel>
														<FormControl>
															<Input
																{...field}
																placeholder='1245'
																disabled={mutation.isPending}
															/>
														</FormControl>
														<FormMessage />
													</FormItem>
												)}
											/>
											<FormField
												control={form.control}
												name='cvc'
												render={({ field }) => (
													<FormItem>
														<FormLabel>Действует до</FormLabel>
														<FormControl>
															<Input
																{...field}
																placeholder='324'
																disabled={mutation.isPending}
															/>
														</FormControl>
														<FormMessage />
													</FormItem>
												)}
											/>
											<FormField
												control={form.control}
												name='adress'
												render={({ field }) => (
													<FormItem>
														<FormLabel>Адрес</FormLabel>
														<FormControl>
															<Input
																{...field}
																placeholder='г. Казань, ул. Деревня-Универсиады 5'
																disabled={mutation.isPending}
															/>
														</FormControl>
														<FormMessage />
													</FormItem>
												)}
											/>
										</div>
										<div className='grid grid-cols-[2fr_1fr]'>
											<p>Сумма оплаты:</p>
											{isSuccess && <span>{totalPrice} ₽</span>}
										</div>
										<Button
											className='bg-blue-500 w-full hover:bg-blue-700 text-white font-bold py-4 px-4 rounded mr-2'
											type='submit'
											disabled={mutation.isPending}
										>
											Оплатить
										</Button>
									</form>
								</Form>
							</CardContent>
						</Card>
					</div>
				</div>
			</div>

		</div>
	);
}