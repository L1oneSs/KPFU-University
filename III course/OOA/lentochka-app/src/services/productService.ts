import axios from 'axios';
import * as z from 'zod';
import { NewProductSchema } from '@/schemas';
import { IProduct } from '@/interface/IProduct';

class ProductService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/product`;

	async getByCategory(category: string) {
		return axios.get(`${this.URL}?category=${category}`);
	};
	
}

export default new ProductService();