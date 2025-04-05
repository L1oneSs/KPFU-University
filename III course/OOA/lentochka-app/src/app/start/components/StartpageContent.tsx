"use client"
import React, { useState, useEffect, useRef } from 'react';
import { motion } from 'framer-motion';
import { IoGiftOutline, IoPeopleOutline, IoHeartOutline, IoHappyOutline } from 'react-icons/io5'; // Импорт новых иконок
import StartpageHeaderContent from './StartpageHeaderContent';

const StartpageContent = () => {
  const [isVisible, setIsVisible] = useState(false);
  const ref = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const onScroll = () => {
      if (ref.current) {
        const top = ref.current.getBoundingClientRect().top;
        const windowHeight = window.innerHeight;
        if (top < windowHeight) {
          setIsVisible(true);
        }
      }
    };

    window.addEventListener('scroll', onScroll);
    return () => window.removeEventListener('scroll', onScroll);
  }, []);

  return (
    <div>
      <StartpageHeaderContent />
      <div className="relative bg-neutral-300/90">
        <div ref={ref} className="relative z-20 flex flex-col items-center justify-center gap-40 px-8 py-20">
          
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={isVisible ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5 }}
          >
            <div className="flex flex-col gap-y-8">
              <div className="flex flex-row justify-center items-center gap-x-4">
                <IoGiftOutline size={48} className="text-blue-500" /> 
                <h2 className="text-3xl font-bold text-center text-white">Дарите подарки с удовольствием</h2>
              </div>
              <p className="text-xl text-center text-white">Наш сайт поможет вам легко и быстро подарить идеальный подарок для любого случая.</p>
            </div>
          </motion.div>
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={isVisible ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.5, delay: 0.2 }}
          >
            <div className="flex flex-col gap-y-8">
              <div className="flex flex-row justify-center items-center gap-x-4">
                <IoPeopleOutline size={48} className="text-blue-500" /> 
                <h2 className="text-3xl font-bold text-center text-white">Создавайте вишлисты</h2>
              </div>
              <p className="text-xl text-center text-white">Поделитесь своими желаниями с друзьями и близкими, чтобы они могли порадовать вас идеальным подарком.</p>
            </div>
          </motion.div>
          
          <div className="flex flex-row justify-around w-full">
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={isVisible ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.5, delay: 0.4 }}
              className="text-center text-white"
            >
              <div className="flex flex-col justify-center items-center gap-y-10">
                <div className="flex flex-row gap-x-8">
                  <IoHeartOutline size={48} className="text-blue-500 mb-4" />
                  <h3 className="text-2xl font-bold">Лучшие подарки для всех случаев</h3>
                </div>
                <motion.img
                  initial={{ opacity: 0, y: 20 }}
                  animate={isVisible ? { opacity: 1, y: 0 } : {}}
                  transition={{ duration: 0.5, delay: 0.8 }}
                  src="image1.jpg"
                  alt="Изображение 1"
                  className="w-32 h-32 object-cover rounded-full"
                />
              </div>
            </motion.div>

            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={isVisible ? { opacity: 1, y: 0 } : {}}
              transition={{ duration: 0.5, delay: 0.4 }}
              className="text-center text-white"
            >
              <div className="flex flex-col justify-center items-center gap-y-10">
                <div className="flex flex-row gap-x-8">
                  <IoHappyOutline size={48} className="text-blue-500 mb-4" />
                  <h3 className="text-2xl font-bold">Делитесь радостью вместе с нами</h3>
                </div>
                <motion.img
                  initial={{ opacity: 0, y: 20 }}
                  animate={isVisible ? { opacity: 1, y: 0 } : {}}
                  transition={{ duration: 0.5, delay: 0.8 }}
                  src="image2.jpg"
                  alt="Изображение 2"
                  className="w-32 h-32 object-cover rounded-full"
                />
              </div>
            </motion.div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default StartpageContent;