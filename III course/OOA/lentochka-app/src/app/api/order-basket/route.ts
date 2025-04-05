import { auth } from '@/auth';
import { currentUser } from '@/lib/auth';
import { db } from '@/lib/db';
import { NextRequest, NextResponse } from 'next/server';

export const GET = async (req: NextRequest) => {
	try {
		const user = await currentUser();

		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		};

		var orders;

		if (user.id) {
			orders = await db.order.findMany({
				where: { userId: user.id },
			})
		}

		console.log(orders);

		const orderArray = [];

		if (orders) {
			for (let itemOrders of orders) {
				for (let productOrder of itemOrders.productId) {
					var product;
					if (productOrder) {
						product = await db.product.findFirst({
							where: { id: productOrder }
						});
					}
					var resOrder;
					if (product) {
						resOrder = {
							id: itemOrders.id,
							status: itemOrders.status,
							adress: itemOrders.adress,
							deliveryDate: itemOrders.deliveryDate,
							productName: product.name,
							productDescription: product.description,
							productImage: product.image,
						};
					}
					orderArray.push(resOrder);
				}
			}
		}		

		return NextResponse.json(orderArray, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};