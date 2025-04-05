import { PrismaClient, User } from '@prisma/client';
import { useQuery } from '@tanstack/react-query';

const prisma = new PrismaClient();

export const useAllUsers = () => {
    const getAllUsers = async () => {
        try {
            const users = await prisma.user.findMany();
            return users;
        } catch (error) {
            console.log(error)
            throw new Error(`Error loading users: ${error}`);
            
        }
    };

    const { data: users, isLoading, isError, error } = useQuery<User[], Error>({
        queryKey: ['allUsers'], 
        queryFn: getAllUsers,
    });

    return {
        users,
        isLoading,
        isError,
        error, 
    };
};
