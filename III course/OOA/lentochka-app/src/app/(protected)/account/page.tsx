import { Header } from "@/components/layout/header";
import { Footer } from "@/components/layout/footer";
import Sidebar from "@/components/Sidebar";
import ProfileCard from "@/app/(protected)/account/components/ProfileCard";
import { currentUser } from '@/lib/auth';
import axios from 'axios';

export default async function AccountPage() {
	const user = currentUser();

	if (user === undefined) await axios.get(`${process.env.NEXT_PUBLIC_APP_URL}/api/session`);

	return (
		<main>
			<Header></Header>
			<div className="flex flex-row">
				<Sidebar></Sidebar>
				<div className="flex-grow">
					<ProfileCard></ProfileCard>
				</div>
			</div>
			<Footer></Footer>
		</main>
	);
}