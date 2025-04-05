import { Header } from '@/components/layout/header';
import StartpageContent from './start/components/StartpageContent';
import { Footer } from '@/components/layout/footer';
import CardProduct from '@/components/ui/cardProduct';
import SellerCard from '@/components/ui/sellerCard';

export default function Home() {
	const sellerData = {
		id: 1,
		name: "Trading house AST-Eksmo",
		location: "Business complex Moscow City, Tower Empire",
		rating: 4.5,
		imageUrl: "https://www.litres.ru/static/copyrights_logo/9339265_640.jpg",
	  };
	return (
		<main>
			<Header/>
			<StartpageContent></StartpageContent>
			<Footer/>
		</main>
	);
}