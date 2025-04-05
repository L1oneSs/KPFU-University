"use client"
import React from 'react';
import { motion } from 'framer-motion';


const StartpageHeaderContent: React.FC = () => {
  const videoRef = React.useRef<HTMLVideoElement>(null);

  return (
    <div className="relative bg-neutral-50 h-screen">
      <div className="absolute inset-0 z-10">
        <video ref={videoRef} className="absolute inset-0 w-full h-full object-cover" loop autoPlay muted>
          <source src="/video3.mp4" type="video/mp4" />
        </video>
        <div className="absolute inset-0 bg-black opacity-25" />
      </div>
      <div className="relative z-20 flex flex-col items-center justify-center gap-16 px-8 py-20">
        <motion.div
          initial={{ opacity: 0, y: 40, x: -40 }} 
          animate={{ opacity: 1, y: 0, x: 0 }} 
          transition={{ duration: 0.5, delay: 0.2 }} 
        >
          <p className="text-5xl font-bold text-left text-white">Откройте мир подарков с нами</p>
        </motion.div>
      </div>
    </div>
  );
};

export default StartpageHeaderContent;