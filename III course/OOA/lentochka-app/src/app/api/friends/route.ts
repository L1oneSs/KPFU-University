import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from "next/server";

export const POST = async (req: NextRequest) => {
    const body = await req.json()
    console.log(body)
    const potentialFriend = await db.user.findUnique({
        where: {nickname: body.inputValue}
    })
    console.log(potentialFriend)
    return NextResponse.json(potentialFriend, {status: 200})
}

export const GET = async() => {
    const user = await currentUser()

    if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401})

    const friends = await db.friends.findMany({
        where: {userId: user?.id}
    })

    return NextResponse.json(friends, {status: 200})
}

export const PUT = async(req: NextRequest) => {
    const user = await currentUser()

    const body = await req.json()
    console.log(body)

    if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401})


    const potentialFriendsRecord = await db.potentialFriends.findFirst({
        where: {
            userId: body.friend.userId, 
            userIdPFriend: body.friend.userIdPFriend
        }
    })

    if (!potentialFriendsRecord) return NextResponse.json({error: 'Запись не найдена'}, {status: 401})
    
    var deleteID
        
    
        await db.friends.create({
            data: {
            nicknameTo: potentialFriendsRecord.nicknameTo as string,
            nicknameBy: potentialFriendsRecord.nicknameBy,
            userId: potentialFriendsRecord.userId,
            userIdPFriend: potentialFriendsRecord.userIdPFriend
        }
        })

        await db.friends.create({
            data: {
            nicknameTo: potentialFriendsRecord.nicknameBy as string,
            nicknameBy: potentialFriendsRecord.nicknameTo,
            userId: potentialFriendsRecord.userIdPFriend,
            userIdPFriend: potentialFriendsRecord.userId
        }
        })

        if(user.id){
            deleteID = await db.potentialFriends.findFirst({
                    where: {
                        userId: potentialFriendsRecord.userId, 
                        userIdPFriend: user.id
                    }
                })
            }

        if(deleteID){
                await db.potentialFriends.delete({
                        where: {
                            id: deleteID.id
                    }
            })}

    

    if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401})

    

    return NextResponse.json({message: "Добавлен в друзья"}, {status: 200})

}

export const DELETE = async(req: NextRequest) => {
    const body = await req.json(); 

    const friendIdToDelete = body.friend; 

    const user = await currentUser()

    if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401})
    
    var friendFirstId
    var friendSecondId

    if (user.id){


            friendFirstId = await db.friends.findFirst({
                where: {
                    userId: user.id, 
                    userIdPFriend: friendIdToDelete.userIdPFriend
                }
            })
            
            if(friendFirstId){
                await db.friends.delete({
                        where: {
                            id: friendFirstId.id
                    }
            })}

            friendSecondId = await db.friends.findFirst({
                where: {
                    userId: friendIdToDelete.userIdPFriend, 
                    userIdPFriend: user.id
                }
            })

            if(friendSecondId){
                await db.friends.delete({
                        where: {
                            id: friendSecondId.id
                    }
            })}
        }
        

    return NextResponse.json({message: "Друг успешно удален"}, {status: 200});
}