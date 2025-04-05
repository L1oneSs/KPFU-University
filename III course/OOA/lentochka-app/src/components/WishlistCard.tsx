"use client"
import React, { useState } from 'react';
import { HiPencilAlt, HiX } from 'react-icons/hi';
import gift from '/public/grey-present.jpg';
import Slider from 'react-slick';
import 'slick-carousel/slick/slick.css';
import 'slick-carousel/slick/slick-theme.css';
import { toast } from 'react-hot-toast';
import { IProduct } from '@/interface/IProduct';

interface WishlistCardProps{
  products: IProduct[]
}


const WishlistCard = ({products}: WishlistCardProps) => {
  return (
    products.map((product) => (
      <div className="relative bg-white rounded-xl shadow-md overflow-hidden max-w-sm">
      <div className="p-2 flex flex-col">
        <div className="flex mt-20 justify-center mb-10">
        {product?.image && (
          <img className="h-auto max-w-full object-center md:w-48" src={product.image} alt="Product" />
        )}
        </div>
        <div className="p-8 flex flex-col gap-y-10 min-w-80"> 
        <div>
          <div className="uppercase tracking-wide text-sm text-indigo-500 font-semibold">Описание</div>
            <div dangerouslySetInnerHTML={{ __html: product.description }} className='mt-2 text-gray-500' />
          </div>
          <div>
            <label htmlFor="links" className="block text-sm font-medium text-gray-700">Ссылка на продукт: </label>
            <div>{product.slug}</div>
          </div>
          <div>
            <label htmlFor="hashtags" className="block text-sm font-medium text-gray-700">Категория: </label>
            <div>{product.hashtag?.title}</div>
          </div>
          <div>
            <label htmlFor="hashtags" className="block text-sm font-medium text-gray-700">Название: </label>
            <div>{product.name}</div>
          </div>
        </div>
      </div>
    </div>
    ))
  );
};

export default WishlistCard;