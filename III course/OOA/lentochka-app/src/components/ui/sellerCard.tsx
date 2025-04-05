import React from 'react';

interface Seller {
  id: number;
  name: string;
  location: string;
  rating: number;
  imageUrl: string;
}

interface SellerCardProps {
  seller: Seller;
}

const SellerCard: React.FC<SellerCardProps> = ({ seller }) => {
  return (
    <div className="max-w-xs rounded overflow-hidden shadow-lg">
      <img className="w-full h-auto" src={seller.imageUrl} alt={seller.name} />
      <div className="px-6 py-4">
        <div className="font-bold text-xl mb-2">{seller.name}</div>
        <p className="text-gray-700 text-base">{seller.location}</p>
        <p className="text-gray-700 text-base">Rate: {seller.rating}</p>
      </div>
    </div>
  );
};

export default SellerCard;
