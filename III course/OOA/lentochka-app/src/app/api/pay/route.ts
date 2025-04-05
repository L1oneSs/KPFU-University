import { auth } from '@/auth';
import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server';

export const GET = async (req: NextRequest) => {
	try {
		const user = await currentUser();

		const url = await req.nextUrl;
		const { searchParams } = url;
		const orderId = searchParams.get('order');

		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		};


		console.log('orderId', orderId)

		var order;

		if (orderId) {
			order = await db.order.findFirst({
				where: { id: orderId },
			})
		}

		var totalPrice = 0;

		if (order?.productId) {
			for (let itemOrderProductId of order?.productId) {
				var product;
				if (itemOrderProductId) {
					product = await db.product.findFirst({
						where: { id: itemOrderProductId }
					});
					if (product?.id) totalPrice = product?.price;
				}
			}
		}

		return NextResponse.json(totalPrice, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};

export const PUT = async (req: NextRequest) => {
	try {
		const user = await currentUser();

		const url = await req.nextUrl;

		const { searchParams } = url;

		const orderId = searchParams.get('order');

		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		};

		const body = await req.json()

		console.log('orderId', orderId)
		console.log('body', body.adress);

		// Получаем текущую дату
		let currentDate = new Date();
		// Получаем дату через 7 дней
		let nextWeek = new Date();
		nextWeek.setDate(currentDate.getDate() + 7);

		let randomDate = new Date(currentDate.getTime() + Math.random() * (nextWeek.getTime() - currentDate.getTime()));
		console.log(randomDate);
		var order;

		if (orderId) {
			order = await db.order.update({
				where: { id: orderId },
				data: {
					adress: body.adress,
					deliveryDate: randomDate,
					status: 'Оплачено'
				}
			})
		}

		console.log(order);

		return NextResponse.json({ status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};