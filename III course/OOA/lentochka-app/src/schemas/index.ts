import { UserRole } from '@prisma/client';
import * as z from "zod";


export const NewProductSchema = z.object({
	name: z.string().min(1, {
		message: "Заполните поле!",
	}),
	description: z.string().min(1, {
		message: "Заполните поле!",
	}),
	hashtag: z.string(),
	image: z.optional(z.string()),
	price: z.coerce.number(),
});

export const WishListItemSchema = z.object({
	name: z.string().min(1, {
		message: "Заполните поле!",
	}),
	description: z.string().min(1, {
		message: "Заполните поле!",
	}),
	hashtag: z.string(),
	image: z.optional(z.string()),
	link: z.string().min(1, {
		message: "Заполните поле!",
	}),
});


export const LoginSchema = z.object({
	email: z.string().email({
		message: "Email is required",
	}),
	password: z.string().min(1, {
		message: "Password is required",
	}),
	code: z.optional(z.string()),
	twoFactor: z.optional(z.boolean()),
	callbackUrl: z.optional(z.string().nullable()),
});

export const PaySchema = z.object({
	cardNumber: z.coerce.number(),
	date: z.coerce.number(),
	cvc: z.coerce.number(),
	adress: z.string()
});

export const RegisterSchema = z.object({
	email: z.string().email({
		message: "Заполните поле email!",
	}),
	password: z.string().min(6, {
		message: "Минимум 6 символов в поле пароль!",
	}),
	name: z.string().min(1, {
		message: 'Заполните поле ФИО!'
	}),
	nickname: z.string().min(1, {
		message: 'Заполните поле псевдоним!',

	})
});


export const ResetSchema = z.object({
	email: z.string().email({
		message: "Email is required",
	})
});

export const NewPasswordSchema = z.object({
	password: z.string().min(6, {
		message: "Minimum of 6 characters required",
	}),
	token: z.string(),
});

export const SettingsSchema = z.object({
	name: z.optional(z.string()),
	email: z.optional(z.string().email()),
	password: z.optional(z.string().min(6)),
	newPassword: z.optional(z.string().min(6)),
	isTwoFactorEnabled: z.optional(z.boolean()),
	role: z.enum([UserRole.ADMIN, UserRole.USER])
}).refine((data) => {
	if (data.password && !data.newPassword) return false;

	return true;
}, {
	message: 'New password is required!',
	path: ['newPassword']
}).refine((data) => {
	if (data.newPassword && !data.password) return false;

	return true;
}, {
	message: 'Password is required!',
	path: ['Password']
});

