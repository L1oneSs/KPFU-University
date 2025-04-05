import { ExtendedUser } from '../../../next-auth'
import { Card, CardContent, CardHeader } from '@/components/ui/card';
import { Badge } from '@/components/ui/badge';
import { useRouter } from 'next/navigation';

interface UserInfoProps {
	user?: ExtendedUser;
	label: string;
}

export const UserInfo = ({ user, label }: UserInfoProps) => {

	const router = useRouter();

	if (user?.id === null) router.refresh();
	return (
		<div className='grid justify-center items-center min-h-screen'>
			<Card className='w-[600px] md:w-[450px] sm:w-[300px] shadow-md'>
				<CardHeader>
					<p className='text-2xl font-semibold text-center'>
						{label}
					</p>
				</CardHeader>
				<CardContent className='space-y-4'>
					<div className='grid grid-flow-col items-center justify-between rounded-lg p-3 shadow-sm'>
						<p className='text-sm font-medium'>
							ФИО
						</p>
						<p className='truncate text-xs max-w-[180px] font-mono p-1 bg-slate-100 rounded-md'>
							{user?.name}
						</p>
					</div>
					<div className='grid grid-flow-col items-center justify-between rounded-lg p-3 shadow-sm'>
						<p className='text-sm font-medium'>
							Email
						</p>
						<p className='truncate text-xs max-w-[180px] font-mono p-1 bg-slate-100 rounded-md'>
							{user?.email}
						</p>
					</div>
					<div className='grid grid-flow-col items-center justify-between rounded-lg p-3 shadow-sm'>
						<p className='text-sm font-medium'>
							Роль
						</p>
						<p className='truncate text-xs max-w-[180px] font-mono p-1 bg-slate-100 rounded-md'>
							{user?.role}
						</p>
					</div>
					<div className='grid grid-flow-col items-center justify-between rounded-lg p-3 shadow-sm'>
						<p className='text-sm font-medium'>
							Двухфакторная аутентификация
						</p>
						<Badge
							variant={user?.isTwoFactorEnabled ? 'success' : 'destructive'}
						>
							{user?.isTwoFactorEnabled ? 'ON' : 'OFF'}
						</Badge>
					</div>
				</CardContent>
			</Card>
		</div>
	);
};