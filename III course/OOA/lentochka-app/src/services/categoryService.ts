import axios from 'axios';

class CategoriesService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/categories`;

	async getAll() {
		return axios.get(this.URL)
	};

};

export default new CategoriesService();