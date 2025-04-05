import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server'

export const GET = async (req: NextRequest) => {
	const user = await currentUser();

	if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401});

	const url = await req.nextUrl;

	const { searchParams } = url;

	const category = searchParams.get('category');

	const categorySlug = await db.category.findFirst({
		where: {tag: category as string}
	});
	
	console.log(categorySlug);
	

	const product = await db.product.findMany({
		where: { categoryId: categorySlug?.id }
	});

	console.log(product);

	return NextResponse.json(product, {status: 200});
}