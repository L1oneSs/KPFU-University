import { auth } from '@/auth';
import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server';


export const POST = async (req: NextRequest) => {
	try {
		const user = await currentUser();
		const body = await req.json();

		var product;

		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		}

		if (user.role === 'USER') return NextResponse.json({ error: 'Нет доступа' }, { status: 403 });

		const hastagTag = await db.category.findFirst({
			where: { tag: body.hashtag }
		});

		if (user.id && hastagTag?.id) {
			product = await db.product.create({
				data: {
					categoryId: hastagTag?.id,
					slug: body.slug,
					name: body.name,
					description: body.description,
					image: body.img,
					price: Number(body.price),
				},
			});
		}

		return NextResponse.json(product, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};