import axios from 'axios';
import { IFriends } from '@/interface/IFriend';

class FriendsService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/friends`;

	async getbynickname(nickname: string) {
		return axios.post<string>(this.URL, nickname);
	};

	async updatefriend(friend: IFriends) {
		return axios.put<IFriends>(this.URL, friend);
	};

    async getAll() {
        return axios.get(this.URL)
    };

	async deletefriend(friend: IFriends){
		 return axios.delete(this.URL, { data: { friend } });
	}


};

export default new FriendsService();