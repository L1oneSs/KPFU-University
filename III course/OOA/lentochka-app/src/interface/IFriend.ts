import { IUser } from "./IUser"

export interface IFriends{
    id: string
    nicknameBy: string
    nicknameTo: string
    userId: string
    userIdPFriend: string
    user: IUser[]
}

