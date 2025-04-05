import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from "next/server";


export const PUT = async(req: NextRequest) => {
    const user = await currentUser()

    const body = await req.json()
    console.log(body)

    if (!user) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401})

    await db.user.update({
        where: {
            id: user.id
        }, 

        data: {
            image: body.image,
            description: body.description
        }
    })
    
    console.log(user)
    return NextResponse.json({message: "Данные успешно обновлены"}, {status: 200})

}


export const GET = async(req: NextRequest) => {
    const Currentuser = await currentUser()

    if (!Currentuser) return NextResponse.json({error: 'Пользователь не авторизован'}, {status: 401})

    const user = await db.user.findFirst({
        where: {
            id: Currentuser.id
        }, 
    })
    
    console.log(user)
    return NextResponse.json(user, {status: 200})

}

