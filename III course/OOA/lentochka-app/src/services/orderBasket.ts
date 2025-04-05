import axios from 'axios';




class OrderBasketService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/order-basket`;

	async getAll() {
		return axios.get(this.URL);
	};

};

export default new OrderBasketService();