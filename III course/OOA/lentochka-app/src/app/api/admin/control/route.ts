import { currentUser } from '@/lib/auth'
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server';


export const GET = async () => {
	const isUser = await currentUser();
	var product;


	if (!isUser) {
		return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
	}

	if (isUser.role === 'USER') return NextResponse.json({ error: 'Нет доступа' }, { status: 403 })


	const user = await db.user.findMany({
		where: {
			NOT: {
				role: 'ADMIN'
			}
		},
		orderBy: {
			name: 'asc'
		},
		select: {
			id: true,
			name: true,
			email: true,
			nickname: true,
			isUserBanned: true,
		}
	});

	return NextResponse.json(user, { status: 200 });
}


export const PUT = async (req: NextRequest) => {
	const isUser = await currentUser();
	const body = await req.json();

	if (!isUser) {
		return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
	}

	if (isUser.role === 'USER') return NextResponse.json({ error: 'Нет доступа' }, { status: 403 })

	const changeUser = await db.user.findUnique({
		where: { id: body.userId }
	})

	await db.user.update({
		where: { id: body.userId },
		data: {
			isUserBanned: !changeUser?.isUserBanned
		}
	})

	return NextResponse.json({ status: 200 });
};

export const DELETE = async (req: NextRequest) => {
	const isUser = await currentUser();
	const body = await req.json();

	if (!isUser) {
		return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
	}

	await db.user.delete({
		where: { id: body.userId },
	})

	return NextResponse.json({ status: 200 });
};
