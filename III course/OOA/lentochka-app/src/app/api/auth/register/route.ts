import * as z from 'zod';
import bcrypt from "bcryptjs";
import { db } from '@/lib/db';
import { RegisterSchema } from '@/schemas';
import { NextRequest, NextResponse } from 'next/server';
import { getUserByEmail } from '@/data/user';
import { generateVerificationToken } from '@/lib/token';
import { sendVerificationEmail } from '@/lib/mail';



export const POST = async (req: NextRequest) => {
	try {
		const body = await req.json();
		const validatedFields = RegisterSchema.safeParse(body);

		if (!validatedFields.success) {
			return NextResponse.json({ error: 'Неверные поля!' }, { status: 401, statusText: 'Invalidated!' });
		};

		const { email, password, name, nickname } = validatedFields.data;
		const hashedPassword = await bcrypt.hash(password, 10);
		const existingUser = await getUserByEmail(email);

		if (existingUser) {
			return NextResponse.json({ error: 'Электронная почта уже используется!' }, { status: 401, statusText: 'Email already in use!' });
		};

		await db.user.create({
			data: {
				name,
				email,
				password: hashedPassword,
				nickname: nickname

			}
		})


		const verificationToken = await generateVerificationToken(email);
		await sendVerificationEmail(verificationToken.email, verificationToken.token);


		console.log('Confirmation email sent!', verificationToken);
		return NextResponse.json({ success: 'Подтверждение отправлено по электронной почте!' }, { status: 200 });;

	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};