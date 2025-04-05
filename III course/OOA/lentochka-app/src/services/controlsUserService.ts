import axios from 'axios';

class ControlsUserService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/admin/control`;

	async ban(userId: string) {
		return axios.put(this.URL, userId);
	};;

	async getAll() {
		return axios.get(this.URL)
	};

	async delete(userId: string) {
		return axios.delete(this.URL, { data: { userId } });
	}


};

export default new ControlsUserService();