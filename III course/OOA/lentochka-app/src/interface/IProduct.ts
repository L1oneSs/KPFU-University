import { Category } from '@prisma/client';

export interface IProduct {
	id: string;
	name: string;
	category: Category;
	hashtagId: string;
	slug: string;
	price: number;
	description: string;
	image: string;
}