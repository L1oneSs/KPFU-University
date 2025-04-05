package com.figures.figures;

import com.figures.figures.points.Point2D;
import com.figures.interfaces.IShape;

public class Rectangle extends QGon {
    public Rectangle(Point2D[] p) {
        super(p);
//        if (!isRectangle()) {
//            throw new IllegalArgumentException("Введите корректные данные для прямоугольника!");
//        }
    }

    @Override
    public double square() {
        // Вычисление длины сторон прямоугольника по координатам вершин
        double a = Math.sqrt(Math.pow(p[1].getX(0) - p[0].getX(0), 2) + Math.pow(p[1].getX(1) - p[0].getX(1), 2));
        double b = Math.sqrt(Math.pow(p[2].getX(0) - p[1].getX(0), 2) + Math.pow(p[2].getX(1) - p[1].getX(1), 2));
        // Вычисление площади прямоугольника
        return a * b;
    }

    public boolean isRectangle() {
        // Проверяем, что противоположные стороны равны и параллельны
        boolean parallel = false;
        boolean equal = false;
        for (int i = 0; i < 4; i++) {
            int j = (i + 1) % 4;
            int k = (i + 2) % 4;
            int l = (i + 3) % 4;
            if (p[i].getX(0) == p[j].getX(0) && p[k].getX(0) == p[l].getX(0)) {
                if (p[i].getX(1) < p[j].getX(1)) {
                    if (p[k].getX(1) > p[l].getX(1) && p[k].getX(1) > p[i].getX(1) && p[l].getX(1) < p[j].getX(1)) {
                        parallel = true;
                        equal = (p[j].getX(1) - p[i].getX(1)) == (p[l].getX(1) - p[k].getX(1));
                    }
                } else {
                    if (p[l].getX(1) > p[k].getX(1) && p[l].getX(1) > p[j].getX(1) && p[k].getX(1) < p[i].getX(1)) {
                        parallel = true;
                        equal = (p[i].getX(1) - p[j].getX(1)) == (p[k].getX(1) - p[l].getX(1));
                    }
                }
            }
        }

        return parallel && equal;
    }

    @Override
    public IShape shift(Point2D a) {
        // Создание массива вершин сдвинутого прямоугольника
        Point2D[] res = new Point2D[n];
        for (int i = 0; i < n; i++) {
            res[i] = new Point2D(new double[]{p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1)});
        }
        // Создание нового прямоугольника с измененными координатами вершин
        return new Rectangle(res);
    }

    @Override
    public IShape rot(double phi) {
        // Создание массива вершин повернутого прямоугольника
        Point2D[] res = new Point2D[n];
        for (int i = 0; i < n; i++) {
            res[i] = p[i].rot(phi);
        }
        // Создание нового прямоугольника с измененными координатами вершин
        return new Rectangle(res);
    }

    @Override
    public IShape symAxis(int i) {
        // Создание массива вершин отраженного прямоугольника
        Point2D[] res = new Point2D[n];
        for (int j = 0; j < n; j++) {
            res[j] = (Point2D) p[j].symAxis(i);
        }
        // Создание нового прямоугольника с измененными координатами вершин
        return new Rectangle(res);
    }
}
