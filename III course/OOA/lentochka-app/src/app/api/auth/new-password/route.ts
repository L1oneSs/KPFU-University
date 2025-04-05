import { getPasswordResetTokenByToken } from '@/data/passwordReset';
import { getUserByEmail } from '@/data/user';
import { NewPasswordSchema } from '@/schemas';
import { NextRequest, NextResponse } from 'next/server';
import bcrypt from 'bcryptjs';
import { db } from '@/lib/db';


export const POST = async (req: NextRequest) => {
	try {
		const body = await req.json();

		const validatedFields = NewPasswordSchema.safeParse(body);

		
		if (!validatedFields.success) {
			return NextResponse.json({ error: "Недопустимые поля!" }, { status: 401, statusText: "Invalid fields!" });
		};

		const { password, token } = validatedFields.data;

		const existingToken = await getPasswordResetTokenByToken(token);
		if (!existingToken) {
			return NextResponse.json({ error: "Недопустимые поля!" }, { status: 401, statusText: 'Invalid token!' });
		};

		const hasExpired = new Date(existingToken.expires) < new Date();
		if (hasExpired) {
			return NextResponse.json({ error: "Срок действия токена истек!" }, { status: 401, statusText: 'Token has expired!' });
		};

		const existingUser = await getUserByEmail(existingToken.email);
		if (!existingUser) {
			return NextResponse.json({ error: "Электронная почта не существует!" }, { status: 401, statusText: 'Email does not exist!' });
		};

		const hashedPassword = await bcrypt.hash(password, 10);

		await db.user.update({
			where: { id: existingUser.id },
			data: { password: hashedPassword },
		});

		await db.passwordResetToken.delete({
			where: { id: existingToken.id },
		});

		return NextResponse.json({success: "Пароль обновлен!"}, { status: 200, statusText: 'Password updated!' });
	} catch (error: any) {
		console.log(error.message);
		return NextResponse.json({ error: error.message }, { status: 500 });
	};
}