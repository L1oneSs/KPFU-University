import axios from 'axios';



interface IClickProductInBasket {
	productId: string
}

interface IChangeCountProductInBasket {
	productId: string;
	changeCount: string;
}


class BasketService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/basket`;

	async create(productId: IClickProductInBasket) {
		return axios.post(this.URL, productId);
	};

	async get() {
		return axios.get(this.URL);
	};

	async delete(productId: IClickProductInBasket) {
		return axios.delete(this.URL, { data: productId });
	};

	async update(values: IChangeCountProductInBasket) {
		return axios.put(this.URL, values);
	};
};

export default new BasketService();