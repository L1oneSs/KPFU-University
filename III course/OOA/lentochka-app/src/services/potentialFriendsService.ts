import { IFriends } from '@/interface/IFriend';
import axios from 'axios';


class PotentialFriendsService {
	private URL = `${process.env.NEXT_PUBLIC_APP_URL}/api/potentialfriends`;

	async addfriendbynickname(nickname: string) {
		return axios.post<string>(this.URL, nickname);
	};

    async deletepotentialfriend(friend: IFriends) {
		return axios.put<IFriends>(this.URL, friend);
	};

    async getAll() {
        return axios.get(this.URL)
    };


};

export default new PotentialFriendsService();