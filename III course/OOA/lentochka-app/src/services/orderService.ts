import axios from 'axios';


interface IPay { 
	arrProductId: string[]
}

class OrderService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/order`;

	async create(values: IPay) {
		return axios.post(this.URL, values);
	};

	async get() {
		return axios.get(this.URL);
	};

	// async delete(productId: IClickProductInBasket) {
	// 	return axios.delete(this.URL, { data: productId });
	// };

	// async update(values: IChangeCountProductInBasket) {
	// 	return axios.put(this.URL, values);
	// };
};

export default new OrderService();