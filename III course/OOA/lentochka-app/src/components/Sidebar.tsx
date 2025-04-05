"use client";
import React from "react";
import { useRouter } from "next/navigation";

const Sidebar: React.FC = () => {
  const router = useRouter();

  const profileSubmit = () => {
    router.push("/account");
  };

  const friendsSubmit = () => {
    router.push("/friends");
  };

  const settingsSubmit = () => {
    router.push("/settings");
  };

  const lineSubmit = () => {
    router.push("/line");
  };

  return (
    <div className="h-auto min-h-screen w-64 bg-gray-900 text-gray-300 flex flex-col justify-between">
      <div className="mt-8 flex flex-col gap-y-4">
        <button
          className="block w-full py-2 px-4 text-left hover:bg-gray-800 hover:text-white transition duration-300 ease-in-out"
          onClick={profileSubmit}
        >
          <svg
            className="inline w-6 h-6 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M12 5l7 7-7 7M5 12h14"
            ></path>
          </svg>
          Профиль
        </button>
        <button
          className="block w-full py-2 px-4 text-left hover:bg-gray-800 hover:text-white transition duration-300 ease-in-out"
          onClick={friendsSubmit}
        >
          <svg
            className="inline w-6 h-6 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M10 20v-6h4v6m0-10v-6h-4v6m-4 10c0 1.104.896 2 2 2h8c1.104 0 2-.896 2-2V10h-2V8h-2v2h-4V8H8v2H6v2h2v6H6zm8-12v2h2V8h-2zm-4 2v2h2V8h-2z"
            ></path>
          </svg>
          Друзья
        </button>
        <button className="block w-full py-2 px-4 text-left hover:bg-gray-800 hover:text-white transition duration-300 ease-in-out"
        onClick={lineSubmit}>
          <svg
            className="inline w-6 h-6 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M4 6h16M4 10h16M4 14h16M4 18h16"
            ></path>
          </svg>
          Лента
        </button>
        <button 
			className="block w-full py-2 px-4 text-left hover:bg-gray-800 hover:text-white transition duration-300 ease-in-out"
			onClick={() => router.push('/shop')}
		>
          <svg
            className="inline w-6 h-6 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M7 3v4M17 3v4M5 12h14M12 3v18"
            ></path>
          </svg>
          Магазин
        </button>
        <button
          className="block w-full py-2 px-4 text-left hover:bg-gray-800 hover:text-white transition duration-300 ease-in-out"
          onClick={settingsSubmit}
        >
          <svg
            className="inline w-6 h-6 mr-2"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
            xmlns="http://www.w3.org/2000/svg"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              d="M19 9v-4h-4V3h-2v2H9V3H7v2H3v4h4v2H3v4h4v2h2v-2h2v2h4v-4h-4v-2h4V9h2zm-4 4v4h-4v-4H7v-4h4V7h4v4h4v4h-4z"
            ></path>
          </svg>
          Настройки
        </button>
      </div>
      <div className="mb-8">{/* Дополнительный контент, если необходим */}</div>
    </div>
  );
};

export default Sidebar;
