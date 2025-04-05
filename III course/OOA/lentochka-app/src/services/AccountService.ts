import axios from 'axios';

interface iChange {
    image: string
    description: string
}

class FriendsService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/account`;

	async updatefriend(value: iChange) {
		return axios.put<iChange>(this.URL, value);
	};

    async getUser() {
		return axios.get(this.URL, );
	};

};

export default new FriendsService();