import React from 'react';
import Content from './components/Content';
import Sidebar from '@/components/Sidebar';
import { Header } from '@/components/layout/header';
import { Footer } from '@/components/layout/footer';

const Friends = () => {
    return (
        <div>
            <Header/>
            <div className="flex flex-row">  
                <Sidebar></Sidebar>
                <div className="flex-grow bg-repeat bg-contain" style={{ backgroundImage: 'url("back2.jpg")', backgroundSize: 'auto' }}>
                <Content/>
                </div>
            </div>
            <Footer></Footer>
        </div>
    );
};

export default Friends;
