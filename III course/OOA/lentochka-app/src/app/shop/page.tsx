import { Feature } from '@/components/widgets/feature';
import { CategoryList } from '@/components/widgets/categoryList';
import { ProductList } from '@/components/widgets/productList';

export default function ShopPage({ searchParams }: any) {
	const page = parseInt(searchParams.page) || 1;
	const category = searchParams.category || 'electronics';

	return (
		<div className='min-h-svh'>
			<Feature/>
			<CategoryList />
			<ProductList category={category}/>
		</div>
	);
}