import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function pushToWishlist(userId: string, data: { url: string, hashtags: string[] }) {
    try {
        const user = await prisma.user.findUnique({
            where: { id: userId },
        });

        if (!user) {
            throw new Error('User not found');
        }

        const wishlist = await prisma.wishlist.create({
            data: {
                userId: user.id,
                links: {
                    create: [{ url: data.url }],
                },
                hashtags: {
                    create: data.hashtags.map(tag => ({ tag })),
                },
            },
            include: { links: true, hashtags: true },
        });

        return wishlist;
    } catch (error) {
        console.error('Error pushing to wishlist:', error);
        throw error;
    } finally {
        await prisma.$disconnect();
    }
}

export default pushToWishlist;
