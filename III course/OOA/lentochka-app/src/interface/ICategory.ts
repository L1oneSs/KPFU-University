import { IProduct } from './IProduct';

export interface ICategory {
	id: string;
    tag: string;
    title: string;
    img: string;
    Product: IProduct[];
}

