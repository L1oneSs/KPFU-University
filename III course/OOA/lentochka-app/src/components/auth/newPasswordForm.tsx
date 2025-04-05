'use client';

import * as z from 'zod';
import { useForm } from 'react-hook-form';
import { zodResolver } from '@hookform/resolvers/zod';
import { CardWrapper } from '@/components/auth/cardWrapper';
import { Form, FormControl, FormField, FormItem, FormLabel, FormMessage } from '@/components/ui/form';
import { NewPasswordSchema } from '@/schemas';
import { Input } from '@/components/ui/input';
import { Button } from '@/components/ui/button';
import { FormError } from '@/components/formError';
import { FormSuccess } from '@/components/formSuccess';
import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query';
import { useState } from 'react';
import { useSearchParams } from 'next/navigation';
import newPasswordService from '@/services/newPasswordService';


export const NewPasswordForm = () => {

	const queryClient = useQueryClient();
	const searchParams = useSearchParams();

	const token = searchParams.get('token');

	console.log(token);


	const [error, setError] = useState<string | undefined>('');
	const [success, setSuccess] = useState<string>('');

	const form = useForm<z.infer<typeof NewPasswordSchema>>({
		resolver: zodResolver(NewPasswordSchema),
		defaultValues: {
			password: '',
			token: '',
		},
	});


	const mutation = useMutation({
		mutationKey: ['new-password'],
		mutationFn: (val: z.infer<typeof NewPasswordSchema>) => newPasswordService.change(val),
		onSuccess: (data: any) => {
			console.log('Success!', data);
			console.log(data.statusText);
			setSuccess(data.data.success);
		},
		onError: (error: any) => {
			setError(error.response.data.error);
			console.log(error.message);
		}
	});



	const onSubmit = (values: z.infer<typeof NewPasswordSchema>) => {

		if (!token) return setError('Отсуствует токен!');

		setError('');
		setSuccess('');


		mutation.mutate({ ...values });
	};

	const onResetNewPassword = () => {
		console.log('Ok');

	}


	return (
		<div className='grid min-h-screen justify-center items-center'>
			<CardWrapper
				headerLabel='Введите новый пароль'
				backButtonLabel='Вернуться к входу в систему'
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
								name='password'
								render={({ field }) => (
									<FormItem>
										<FormLabel>Пароль</FormLabel>
										<FormControl>
											<Input
												{...field}
												disabled={mutation.isPending}
												placeholder='******'
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
							Сброс пароля
						</Button>
					</form>
				</Form>
			</CardWrapper>
		</div >
	);
};
