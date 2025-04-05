import { auth } from '@/auth';
import { getHashtag } from '@/data/line';
import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server';



export const GET = async (req: NextRequest) => {
    try {
        const user = await currentUser();

        if (!user) {
            return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
        }

        const friends = await db.friends.findMany({
            where: {userId: user.id}
        })

        console.log(friends)

        const products: any[] = []

        for (const friend of friends) {
            const wishlists = await db.wishlist.findMany({
                where: { userId: friend.userIdPFriend }
            });
            console.log(wishlists)
            if (wishlists) {
                for (let i=0; i < wishlists.length; i++) {
                    console.log(wishlists[i])
                    const product = await db.product.findFirst({
                        where: { id: wishlists[i].productId }
                    });
                    console.log(product)
                    const user = await db.user.findFirst({
                        where: { id: wishlists[i].userId }
                    });
                    console.log(user)
                    if (product && user) {
                        const value = {
                            id: product.id,
                            userImage: user.image,
                            nickname: user.nickname,
                            name: user.name,
                            productName: product.name,
                            productDescription: product.description,
                            productImage: product.image,
                            productHashtagId: product.hashtagId,
                            productHashtag: await getHashtag(product.hashtagId),
                            productLink: product.slug
                        }
                        console.log(value)
                        products.push(value);
                    }
                }
            }
        }

        

        return NextResponse.json(products, { status: 200 });
    } catch (error: any) {
        return NextResponse.json({ error: error.message }, { status: 500 });
    }
};