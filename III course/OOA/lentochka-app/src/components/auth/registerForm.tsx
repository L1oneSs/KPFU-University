'use client';

import * as z from 'zod';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { CardWrapper } from '@/components/auth/cardWrapper';
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form';
import { RegisterSchema } from '@/schemas';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { FormError } from '@/components/formError';
import { FormSuccess } from '@/components/formSuccess';
import { useState } from 'react';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import registerService from '@/services/registerService';


export const RegisterForm = () => {
	const queryClient = useQueryClient();

	const [error, setError] = useState<string | undefined>('');
	const [success, setSuccess] = useState<string>('');

	const form = useForm<z.infer<typeof RegisterSchema>>({
		resolver: zodResolver(RegisterSchema),
		defaultValues: {
			email: '',
			password: '',
			name: '',
			nickname: '',
		},
	});


	const { data } = useQuery({
		queryKey: ['register'],
		select: ({ data }) => {
			setError(data.error),
				setSuccess(data.success)
		}
	});

	const mutation = useMutation({
		mutationKey: ['register'],
		mutationFn: (val: z.infer<typeof RegisterSchema>) => registerService.create(val),
		onError: (error: any) => {
			setError(error.response.data.error);
			console.log(error.message);
		},
		onSuccess: (data: any) => {
			console.log('Success!', data);
			queryClient.invalidateQueries({ queryKey: ['register'] });
			setSuccess(data.data.success);
		}
	})

	const onSubmit = (values: z.infer<typeof RegisterSchema>) => {
		setError('');
		setSuccess('');

		mutation.mutate(values);
	}

	return (
		<CardWrapper
			headerLabel='Создать учетную запись'
			backButtonLabel='У вас уже есть учетная запись?'
			backButtonHref='/auth/login'
		>
			<Form {...form}>
				<form
					onSubmit={form.handleSubmit(onSubmit)}
					className='space-y-6'
				>
					<div className='space-y-4'>
						<FormField
							control={form.control}
							name='name'
							render={({ field }) => (
								<FormItem>
									<FormLabel>ФИО</FormLabel>
									<FormControl>
										<Input
											{...field}
											disabled={mutation.isPending}
											placeholder='Иванов Иван'
										/>
									</FormControl>
									<FormMessage />
								</FormItem>
							)}
						/>
						<FormField
							control={form.control}
							name='nickname'
							render={({ field }) => (
								<FormItem>
									<FormLabel>Псевдоним</FormLabel>
									<FormControl>
										<Input
											{...field}
											disabled={mutation.isPending}
											placeholder='ivanivanov2003'
										/>
									</FormControl>
									<FormMessage />
								</FormItem>
							)}
						/>
						<FormField
							control={form.control}
							name='email'
							render={({ field }) => (
								<FormItem>
									<FormLabel>Email</FormLabel>
									<FormControl>
										<Input
											{...field}
											disabled={mutation.isPending}
											placeholder='ivanovivan@example.com'
											type='email'
										/>
									</FormControl>
									<FormMessage />
								</FormItem>
							)}
						/>
						<FormField
							control={form.control}
							name='password'
							render={({ field }) => (
								<FormItem>
									<FormLabel>Пароль</FormLabel>
									<FormControl>
										<Input
											{...field}
											placeholder='******'
											disabled={mutation.isPending}
											type='password'
										/>
									</FormControl>
									<FormMessage />
								</FormItem>
							)}
						/>
					</div>
					<FormError message={error} />
					<FormSuccess message={success} />
					<Button
						type='submit'
						disabled={mutation.isPending}
						className='w-full'
					>
						Зарегистрироваться
					</Button>
				</form>
			</Form>
		</CardWrapper>
	)
}