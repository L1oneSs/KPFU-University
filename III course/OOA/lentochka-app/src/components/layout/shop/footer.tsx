import Image from 'next/image';

export const FooterShop = () => {
	return (
		<footer className='grid grid-flow-col grid-cols-3 items-center relative px-9 py-6 bg-gray-900'>
			<Image src='/logo.img' alt='Logotype' height={40} width={80}/>
			<div>
				<p>+7 (898) 754-39-89</p>
				<p>lentochka@mail.ru</p>
			</div>
			
		</footer>
	);
}