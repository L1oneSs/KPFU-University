'use client';

import { Card, CardHeader, CardTitle, CardContent } from '@/components/ui/card';
import controlsUserService from '@/services/controlsUserService';
import { useQuery, useQueryClient, useMutation } from '@tanstack/react-query';
import { BeatLoader } from 'react-spinners';
import { Switch } from '@/components/ui/switch';
import { Button } from '@/components/ui/button';
import toast from 'react-hot-toast';
import { AdminNavbar } from '@/components/layout/admin/adminNavbar';
import { useCurrentRole } from '@/hooks/useCurrentRole';

interface IUserConrol {
	id: string;
	email: string;
	name: string;
	nickname: string;
	isUserBanned: boolean;
}

export default function ControlPage() {
	const queryClient = useQueryClient();
	const role = useCurrentRole();

	const { data: usersData, isLoading, isSuccess } = useQuery({
		queryKey: ['controls-users'],
		queryFn: () => controlsUserService.getAll(),
		select: ({ data }) => data
	})

	const { mutate: mutateUserBanned, isPending: isPendingUserBanned, } = useMutation({
		mutationKey: ['user-ban'],
		mutationFn: (userId: string) => controlsUserService.ban(userId),
		onSuccess: (data) => {
			toast.success('Изменения вступили в силу!')
			queryClient.invalidateQueries({ queryKey: ['controls-users'] })
		}
	})

	const { mutate: mutateUserDelete, isPending: isPendingUserDelete, } = useMutation({
		mutationKey: ['user-ban'],
		mutationFn: (userId: string) => controlsUserService.delete(userId),
		onSuccess: (data) => {
			toast.success('Изменения вступили в силу!')
			queryClient.invalidateQueries({ queryKey: ['controls-users'] })
		}
	})


	const onBanned = (userId: string) => {
		mutateUserBanned({ userId });
	};

	const onDelete = (userId: string) => {
		mutateUserDelete({ userId })
	}

	if (role === 'USER') {
		return (
			<div className='grid items-center justify-center min-h-screen gap-y-4 bg-teal-950'>
				<div>
					<p className='text-secondary text-2xl font-semibold text-center'>
						403 Ошибка
					</p>
					<p className='text-secondary text-2xl font-semibold text-center'>
						⚔️ Доступ запрещён
					</p>
				</div>
			</div>
		)
	}

	return (
		<div className='grid items-center justify-center min-h-screen bg-teal-950'>
			<Card className='w-[1200px] xl:w-[1024px] lg:w-[767px] md:w-[650px] sm:w-[300px] shadow-md'>
				<AdminNavbar />
				<CardHeader>
					<CardTitle>
						<p className='text-2xl font-semibold text-center md:text-lg'>
							🔑 Управление
						</p>
					</CardTitle>
				</CardHeader>

				{isLoading && <div className='grid justify-center'><BeatLoader className='grid grid-flow-col my-6' /></div>}
				{isSuccess &&
					<CardContent>
						<div className='grid grid-flow-col grid-cols-4 items-center gap-1'>
							<div className='text-base text-center font-medium grid justify-center md:text-xs sm:text-[9px]'>ФИО</div>
							<div className='text-base text-center font-medium grid justify-center md:text-xs sm:text-[9px]'>Псевдоним</div>
							<div className='text-base text-center font-medium grid justify-center md:text-xs sm:text-[9px]'>Бан</div>
						</div>

						{usersData.map((user: IUserConrol) => (
							<div className='grid grid-flow-col grid-cols-4 items-center gap-1' key={user.id}>
								<div className='text-base text-center font-medium grid justify-center md:text-xs sm:text-[9px]'>{user.name}</div>
								<div className='text-base text-center font-medium grid justify-center md:text-xs sm:text-[9px]'>{user.nickname}</div>
								<div className='grid items-center justify-center p-3 '>
									<Switch
										checked={user?.isUserBanned}
										onCheckedChange={() => onBanned(user.id)}
										disabled={isPendingUserBanned}
									/>
								</div>
								<div className='grid items-center justify-center p-3 '>
									<Button
										variant='destructive'
										onClick={() => onDelete(user.id)}
										disabled={isPendingUserDelete}
									>
										Удалить
									</Button>
								</div>
							</div>

						))}
					</CardContent>
				}
			</Card>
		</div>
	);
};