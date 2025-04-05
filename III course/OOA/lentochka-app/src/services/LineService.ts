import axios from 'axios';
import * as z from 'zod';
import { NewProductSchema, WishListItemSchema } from '@/schemas';

class Line {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/line`;

    async getWishlists() {
		return axios.get(`${this.URL}`);
	}
}

export default new Line();