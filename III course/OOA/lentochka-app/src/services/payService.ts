import { LoginSchema, PaySchema } from '@/schemas';
import axios from 'axios';
import * as z from 'zod';


class PayService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/pay`;

	async update(values: z.infer<typeof PaySchema>, orderId: string) {
		return axios.put<z.infer<typeof PaySchema>>(`${this.URL}?order=${orderId}`, values);
	};

	async get(orderId: string){
		return axios.get(`${this.URL}?order=${orderId}`);
	}


};

export default new PayService();