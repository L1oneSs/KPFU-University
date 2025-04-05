import axios from 'axios';
import * as z from 'zod';
import { NewProductSchema } from '@/schemas';
import { IProduct } from '@/interface/IProduct';

class NewProductService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/admin/new-product`;

	async create(newPost: z.infer<typeof NewProductSchema>) {
		return axios.post(`${this.URL}`, newPost);
	}

	async getByCategory(category: string) {
		return axios.get(`${this.URL}?category=${category}`);
	}
}

export default new NewProductService();