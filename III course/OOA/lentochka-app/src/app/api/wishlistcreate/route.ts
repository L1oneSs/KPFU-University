import { auth } from '@/auth';
import { getHashtag } from '@/data/line';
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

		const hastagTag = await db.category.findFirst({
			where: { tag: body.hashtag }
		})

		if (user.id && hastagTag?.id) {
			product = await db.product.create({
				data: {
					categoryId: hastagTag?.id,
					name: body.name,
					description: body.description,
					image: body.img,
					slug: body.link,
                    price: 0
				},
			});
		}

        if(user.id && product?.id){
            await db.wishlist.create({
            data: {
                productId: product?.id,
                userId: user.id,
            }
        })
        }
        

		return NextResponse.json("Вишлист успешно создан!", { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};

export const GET = async (req: NextRequest) => {
    try {
        const user = await currentUser();

        if (!user) {
            return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
        }

        const wishlists = await db.wishlist.findMany({
            where: { userId: user.id }
        });

		console.log(wishlists)

        const products: any[] = [];

        for (const wishlist of wishlists) {
            const product = await db.product.findFirst({
                where: { id: wishlist.productId }
            });
            if (product) {
                if (product.description){
                    product.hashtag = await getHashtag(product.hashtagId)
                }
                products.push(product);
            }
        }

        console.log(products);

        return NextResponse.json(products, { status: 200 });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
};
