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

		const basket = await db.basket.findMany({
			where: {
				userId: user.id
			}
		})

		console.log(basket);


		const productInBusket = []

		for (var itemBasket of basket) {
			var product = await db.product.findFirst({
				where: {
					id: itemBasket.productId
				}
			})
			console.log(product);
			const newItemBasket = {
				productId: product?.id,
				productName: product?.name,
				productImage: product?.image,
				productDescription: product?.description,
				productPrice: product?.price,
				productCount: itemBasket.count
			}
			console.log(newItemBasket);

			productInBusket.push(newItemBasket);
		};
		console.log(productInBusket);

		return NextResponse.json(productInBusket, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};


export const POST = async (req: NextRequest) => {
	try {
		const user = await currentUser();
		const body = await req.json();


		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		};

		const productInBusket = await db.basket.findFirst({
			where: {
				userId: user.id,
				productId: body.productId
			}
		});

		var countProductInBuske = productInBusket?.count;

		if (user.id && body.productId && countProductInBuske === undefined) {
			const product = await db.basket.create({
				data: {
					userId: user.id,
					productId: body.productId,
					count: 1
				}
			})


		} else if (user.id && body.productId && countProductInBuske && productInBusket && countProductInBuske !== 0) {
			return NextResponse.json({ success: 'Товар уже есть в корзине!' })
		};

		return NextResponse.json({ success: 'Товар добавлен в корзину!' }, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};

export const DELETE = async (req: NextRequest) => {
	try {
		const user = await currentUser();
		const body = await req.json();

		console.log(body);

		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		};

		const deleteItemFromBusket = await db.basket.findFirst({
			where: {
				productId: body.productId
			}
		});

		if (deleteItemFromBusket) {
			await db.basket.delete({
				where: {
					id: deleteItemFromBusket.id
				}
			});
		}
		;
		return NextResponse.json({ success: 'Товар удалён с корзины!' }, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};

export const PUT = async (req: NextRequest) => {
	try {
		const user = await currentUser();
		const body = await req.json();


		if (!user) {
			return NextResponse.json({ error: "Необходимо авторизоваться" }, { status: 401 });
		};

		const productInBusket = await db.basket.findFirst({
			where: {
				userId: user.id,
				productId: body.productId
			}
		});

		var countProductInBuske = productInBusket?.count;


		console.log(body.changeCount);

		if (productInBusket?.id && countProductInBuske) {
			if (body.changeCount == 'plus') {
				await db.basket.update({
					where: {
						id: productInBusket?.id
					},
					data: {
						count: countProductInBuske + 1
					},
				})
				
			} else if (body.changeCount = 'minus') {
				await db.basket.update({
					where: {
						id: productInBusket?.id
					},
					data: {
						count: countProductInBuske - 1
					},
				})
			}
		}


		return NextResponse.json({ success: 'Изменено количество товара!' }, { status: 200 });
	} catch (error: any) {
		return NextResponse.json({ error: error.message }, { status: 500 });
	}
};