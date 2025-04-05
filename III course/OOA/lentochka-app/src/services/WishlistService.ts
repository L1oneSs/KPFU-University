import axios from 'axios';
import * as z from 'zod';
import { NewProductSchema, WishListItemSchema } from '@/schemas';

class WishlistService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/wishlistcreate`;

	async create(newPost: z.infer<typeof WishListItemSchema>) {
		return axios.post(`${this.URL}`, newPost);
	}

    async getWishlists() {
		return axios.get(`${this.URL}`, );
	}
}

export default new WishlistService();