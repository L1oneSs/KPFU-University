import { getUserByEmail } from '@/data/user';
import { getVerificationTokenByToken } from '@/data/verificationToken';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server';


export const POST = async (req: NextRequest) => {
	try {
		const body = await req.json();
		const { token } = body;

		if (!token) {
			return NextResponse.json({ error: "Токен не предоставлен!" }, { status: 401, statusText: 'No token provided!' });
		}

		const existingToken = await getVerificationTokenByToken(token);

		if (!existingToken) {
			return NextResponse.json({ error: "Токен не существует!" }, { status: 401, statusText: 'Token does not exist!' });
		};

		// если токен истёк
		const hasExpired = new Date(existingToken.expires) < new Date();

		if (hasExpired) {
			return NextResponse.json({ error: "Срок действия токена истек!" }, { status: 401, statusText: 'Token has expired!' });
		};

		const existingUser = await getUserByEmail(existingToken.email);

		if (!existingUser) {
			return NextResponse.json({ error: "Электронной почты не существует!" }, { status: 401, statusText: 'Email does not exist!' });
		};

		await db.user.update({
			where: { id: existingUser.id },
			data: {
				emailVerified: new Date(),
				email: existingToken.email,
			}
		});

		const hasVerificationToken = await db.verificationToken.findFirst({
			where: { id: existingToken.id }
		});

		if (hasVerificationToken) {
			await db.verificationToken.delete({
				where: { id: existingToken.id }
			});
		};


		return NextResponse.json({success: "Адрес электронной почты подтвержден!"}, { status: 200, statusText: 'Email verified!' });
	} catch (error: any) {
		console.log(error.message);
		return NextResponse.json({ error: error.message }, { status: 500 });
	};

};