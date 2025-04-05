import NextAuth from "next-auth";
import { PrismaAdapter } from '@auth/prisma-adapter';
import { db } from "@/lib/db";
import authConfig from '@/auth.config';
import { getUserById } from '@/data/user';
import { getAccountByUserId } from '@/data/account';
import { UserRole } from '@prisma/client';
import { getTwoFactorConfirmationByUserId } from '@/data/twoFactorConfirmation';

export const {
	handlers: { GET, POST },
	auth,
	signIn,
	signOut,
} = NextAuth({
	pages: {
		signIn: '/auth/login',
		error: '/auth/error'
	},
	events: {
		async linkAccount({ user }) {
			await db.user.update({
				where: { id: user.id },
				data: { emailVerified: new Date() }
			})
		}
	},
	callbacks: {
		async signIn({ user, account }) {
			console.log({
				user,
				account
			});

			// Вход через гугол и гитхаб
			if (account?.provider !== 'credentials') return true;

			const existingUser = await getUserById(user.id);
			// Запрет на вход без верификации
			if (!existingUser?.emailVerified) return false;

			if (existingUser.isTwoFactorEnabled) {
				const twoFactorConfirmation = await getTwoFactorConfirmationByUserId(existingUser.id);

				if (!twoFactorConfirmation) return false;

				await db.twoFactorConfirmation.delete({
					where: { id: twoFactorConfirmation.id }
				});

			};

			return true;
		},
		async session({ token, session }) {
			if (token.sub && session.user) {
				session.user.id = token.sub
			}

			if (token.role && session.user) {
				session.user.role = token.role as UserRole;
			}

			if (token.isTwoFactorEnabled && session.user) {
				session.user.isTwoFactorEnabled = token.isTwoFactorEnabled as boolean;
			}

			if (session.user) {
				session.user.name = token.name;
				session.user.nickname = token.nickname as string;
				session.user.description = token.description as string;
				session.user.email = token.email as string;
				session.user.isOAuth = token.isOAuth as boolean;
			}

			return session;
		},
		async jwt({ token, trigger, session }) {

			if (!token.sub) return token;

			const existingUser = await getUserById(token.sub);

			if (!existingUser) return token;

			if (trigger === "update" && session?.user?.name) {
				token.name = session.user.name
			}


			const existingAccount = await getAccountByUserId(existingUser.id);

			token.isOAuth = !!existingAccount;
			token.name = existingUser.name;
			token.nickname = existingUser.nickname;
			token.description = existingUser.description
			token.email = existingUser.email;
			token.role = existingUser.role;
			token.isTwoFactorEnabled = existingUser.isTwoFactorEnabled;

			return token;
		}
	},
	adapter: PrismaAdapter(db),
	session: { strategy: 'jwt' },
	...authConfig,
})