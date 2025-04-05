import { auth } from '@/auth';
import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server';


export const POST = async (req: NextRequest) => {
	try {
		const user = await currentUser();

		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		};

		const body = await req.json()

		console.log(body);

		var order;

		if (user.id && body.arrProductId) {
			order = await db.order.create({
				data: {
					userId: user.id,
					productId: body.arrProductId,
					createdAt: new Date(),
					status: 'Не оплачено',
					adress: '',
					deliveryDate: new Date(0),
				}
			});
		}

		if (user.id && body.arrProductId) {
			for (let productId of body.arrProductId) {
			order = await db.basket.deleteMany({
				where: {
					productId: productId,
					userId: user.id
				}
			});
}		};

		console.log(order);

		return NextResponse.json(order, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};