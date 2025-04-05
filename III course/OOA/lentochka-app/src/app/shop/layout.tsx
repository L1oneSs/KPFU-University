import { Footer } from '@/components/layout/footer';
import { HeaderShop } from '@/components/layout/shop/header';

export default function ShopLayout({ children }: { children: React.ReactNode }) {
	return (
		<div>
			<HeaderShop />
			{children}
			<Footer />
		</div>
	);
}