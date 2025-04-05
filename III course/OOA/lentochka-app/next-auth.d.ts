import NextAuth, { DefaultSession } from 'next-auth';
import { UserRole } from '@prisma/client';

export type ExtendedUser = DefaultSession['user'] & {
	role: UserRole;
	isOAuth: boolean;
	isTwoFactorEnabled: boolean;
	nickname: string;
	description: string;
};

declare module "next-auth" {
	interface Session {
		user: ExtendedUser;
	};
};
