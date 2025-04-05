package com.figures.figures;

import com.figures.figures.points.Point2D;
import com.figures.interfaces.IShape;

public class TGon extends NGon {
    public TGon(Point2D[] p) {
        super(p);
        // Проверяем, что все три точки не лежат на одной прямой
        if ((p[1].getX(1) - p[0].getX(1)) * (p[2].getX(0) - p[1].getX(0)) == (p[2].getX(1) - p[1].getX(1)) * (p[1].getX(0) - p[0].getX(0))) {
            throw new IllegalArgumentException("Введите корректные координаты для треугольника!");
        }
    }

    @Override
    public double square() {
        // Вычисление длин сторон треугольника
        double a = Math.sqrt(Math.pow(p[1].getX(0) - p[0].getX(0), 2) + Math.pow(p[1].getX(1) - p[0].getX(1), 2));
        double b = Math.sqrt(Math.pow(p[2].getX(0) - p[1].getX(0), 2) + Math.pow(p[2].getX(1) - p[1].getX(1), 2));
        double c = Math.sqrt(Math.pow(p[0].getX(0) - p[2].getX(0), 2) + Math.pow(p[0].getX(1) - p[2].getX(1), 2));
        // Вычисление полупериметра
        double pr = (a + b + c) / 2;
        // Вычисление площади по формуле Герона
        return Math.sqrt(pr * (pr - a) * (pr - b) * (pr - c));
    }

    @Override
    public IShape shift(Point2D a) {
        Point2D[] res = new Point2D[n];
        // Сдвиг каждой точки на заданный вектор
        for (int i = 0; i < n; i++) {
            res[i] = new Point2D(new double[]{p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1)});
        }
        return new TGon(res);
    }

    @Override
    public IShape rot(double phi) {
        Point2D[] res = new Point2D[n];
        // Поворот каждой точки на заданный угол
        for (int i = 0; i < n; i++) {
            res[i] = p[i].rot(phi);
        }
        return new TGon(res);
    }

    @Override
    public IShape symAxis(int i) {
        Point2D[] res = new Point2D[n];
        // Отражение каждой точки относительно заданной оси симметрии
        for (int j = 0; j < n; j++) {
            res[j] = (Point2D) p[j].symAxis(i);
        }
        return new TGon(res);
    }
}
