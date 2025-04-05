import { db } from '@/lib/db';
import { hash } from 'bcryptjs';

export const getHashtag = async (id: string) => {
	try {
		const hashtag = await db.hashtag.findFirst({
			where: {
				id
			}
		});

		return hashtag;
	} catch {
		return null;
	}
};