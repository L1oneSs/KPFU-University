import { PrismaClient } from '@prisma/client';

const prisma = new PrismaClient();

async function getWishlists(userId: string) {
    try {
        const user = await prisma.user.findUnique({
            where: { id: userId },
            include: { wishlists: true },
        });

        if (!user) {
            throw new Error('User not found');
        }

        return user.wishlists;
    } catch (error) {
        console.error('Error fetching wishlists:', error);
        throw error;
    } finally {
        await prisma.$disconnect();
    }
}

export default getWishlists;
