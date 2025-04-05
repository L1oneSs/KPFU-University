import React from 'react';

interface Product {
  id: number;
  name: string;
  price: number;
  description: string;
  imageUrl: string;
}

const sampleProduct: Product = {
  id: 1,
  name: "Sample Product",
  price: 10.99,
  description: "This is a sample product description.",
  imageUrl: "https://via.placeholder.com/150",
};

const CardProduct: React.FC = () => {
  return (
    <div className="max-w-xs rounded overflow-hidden shadow-lg">
      <img className="w-full" src={sampleProduct.imageUrl} alt={sampleProduct.name} />
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{sampleProduct.name}</div>
        <p className="text-gray-700 text-base">{sampleProduct.description}</p>
      </div>
      <div className="px-6 py-4">
        <span className="inline-block bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2">${sampleProduct.price}</span>
      </div>
    </div>
  );
};

export default CardProduct;
