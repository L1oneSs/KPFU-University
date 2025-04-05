'use client'
import WishlistCard from '@/components/WishlistCard';
import LineService from '@/services/LineService';
import { useQuery } from '@tanstack/react-query';
import React, { useState } from 'react';
import { Header } from "@/components/layout/header";
import { Footer } from "@/components/layout/footer";
import Sidebar from "@/components/Sidebar";

const Line = () => {
    const { data: wishlistData, isSuccess: isWishlistSuccess, isLoading } = useQuery({
        queryKey: ['wishlistFriend'],
        queryFn: () => LineService.getWishlists(),
        select: ({ data }) => data
    });

    console.log(wishlistData)

    const [loadingMessage, setLoadingMessage] = useState("Загрузка...");

    const wishlistToCard: any = []
    const wishlistUsers: any = []

    if (isWishlistSuccess) {
        wishlistData.forEach((wishlist: any) => {
            const wishlistObject = {
                image: wishlist.productImage,
                description: wishlist.productDescription,
                slug: wishlist.productLink,
                hashtag: wishlist.productHashtag,
                name: wishlist.productName
            }

            const user = {
                userImage: wishlist.userImage,
                nickname: wishlist.nickname,
                name: wishlist.name 
            }

            const existingIndex = wishlistUsers.findIndex((user: any) => user.nickname === wishlist.nickname);

            if (existingIndex === -1) {
                wishlistUsers.push(user);
            }

            wishlistToCard.push(wishlistObject);

        });
    }


    console.log(wishlistData);

    return (
        <main>
            <Header></Header>
            <div className="flex flex-row">
                <Sidebar></Sidebar>
                <div className="flex items-center justify-center flex-grow bg-repeat bg-contain" style={{ backgroundImage: 'url("back2.jpg")', backgroundSize: 'auto' }}>
                    <div className="mx-auto max-w-screen-sm px-2 sm:px-4 md:px-6 lg:px-8 xl:px-10">
                        {isLoading ? (
                            <div className="flex items-center justify-center mb-8 gap-4 font-bold text-2xl ">
                                {loadingMessage}
                            </div>
                        ) : (
                            wishlistData && wishlistData.length > 0 ? (
                                wishlistUsers.map((user: any) => (
                                    <div key={user.id} className="border-b border-gray-300 py-6">
                                        <div className="flex items-center justify-center mb-8 gap-4 bg-white rounded-xl shadow-md p-4 mt-4 inline-block max-w-sm">
                                            <div className="mr-4">
                                                {user.userImage == '' ?
                                                    <img src="/avatar.png" className="rounded-full w-16 h-16 object-cover" alt="Аватарка"></img> :
                                                    <img src={user.userImage} className="rounded-full w-16 h-16 object-cover" alt="Аватарка"></img>
                                                }
                                            </div>
                                            <div>
                                                <div className="text-lg font-bold">{user.nickname}</div>
                                                <div>{user.name}</div>
                                            </div>
                                        </div>
                                        <div className="flex flex-col items-center justify-center mb-8 gap-4">
                                            <WishlistCard products={wishlistToCard}></WishlistCard>
                                        </div>
                                    </div>
                                ))
                            ) : (
                                <div className="flex items-center justify-center mb-8 gap-4 font-bold text-2xl ">
                                    {loadingMessage}
                                </div>
                            )
                        )}
                    </div>
                </div>
            </div>
            <Footer></Footer>
        </main>
    );
};

export default Line;
