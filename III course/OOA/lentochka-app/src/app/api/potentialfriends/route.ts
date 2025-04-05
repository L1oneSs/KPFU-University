import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from "next/server";

export const POST = async (req: NextRequest) => {
    const body = await req.json()
    const user = await currentUser()
    var potentialFriend
    console.log(body)



    if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401})
    
    const userPFriend = await db.user.findUnique({
        where: {nickname: body.nickname}
    })
    
    if (user.id && userPFriend){
            potentialFriend = await db.potentialFriends.create({
            data: {
                nicknameTo: body.nickname as string,
                nicknameBy: user.nickname,
                userId: user.id,
                userIdPFriend: userPFriend?.id
            }
        })
     }   
    console.log(potentialFriend)
    return NextResponse.json(potentialFriend, {status: 200})
}

export const GET = async() => {
    const user = await currentUser()

    if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 200})

    const friends = await db.potentialFriends.findMany({
        where: {userIdPFriend: user?.id}
    })

    const friendsfrom = await db.potentialFriends.findMany({
        where: {userId: user?.id}
    })

    return NextResponse.json({friends, friendsfrom} , {status: 200})

}

export const PUT = async(req: NextRequest) => {

    const body = await req.json()

    const potentialFriendsRecord = await db.potentialFriends.findFirst({
        where: {
            userId: body.friend.userId, 
            userIdPFriend: body.friend.userIdPFriend
        }
    })

    if (!potentialFriendsRecord) return NextResponse.json({error: 'Запись не найдена'}, {status: 401})

    await db.potentialFriends.delete({
            where: {
                id: potentialFriendsRecord.id
        }
    })
    

    return NextResponse.json({message: "Запрос отклонен"}, {status: 200})

}