package com.figures.figures;

import com.figures.abstractclasses.OpenFigure;
import com.figures.figures.points.Point2D;
import com.figures.interfaces.IPolyPoint;
import com.figures.interfaces.IShape;

public class Polyline extends OpenFigure implements IPolyPoint {
    // Приватные поля класса
    private int n;
    private Point2D[] p;

    // Конструктор класса, принимающий массив точек
    public Polyline(Point2D[] p) {
        // Задание количества точек
        n = p.length;
        // Задание массива точек
        this.p = p;
    }

    // Метод для получения количества точек в ломаной линии
    public int getN() {
        return n;
    }

    // Метод для получения массива точек ломаной линии
    public Point2D[] getP() {
        return p;
    }

    // Метод для получения точки ломаной линии по индексу
    public Point2D getP(int i) {
        // Проверка на корректность индекса
        if (i < 0 || i >= n) {
            throw new IllegalArgumentException("Неверный индекс координаты.");
        }
        return p[i];
    }

    // Метод для задания массива точек ломаной линии
    public void setP(Point2D[] p) {
        this.p = p;
    }

    // Метод для задания точки ломаной линии по индексу
    public void setP(Point2D p, int i) {
        // Проверка на корректность индекса
        if (i < 0 || i >= n) {
            throw new IllegalArgumentException("Неверный индекс координаты.");
        }
        this.p[i] = p;
    }

    // Метод для вычисления длины ломаной линии
    @Override
    public double length() {
        double res = 0;
        // Вычисление длины каждого отрезка и добавление к общей длине
        for (int i = 0; i < n - 1; i++) {
            double dx = p[i].getX(0) - p[i + 1].getX(0);
            double dy = p[i].getX(1) - p[i + 1].getX(1);
            res += Math.sqrt(dx * dx + dy * dy);
        }
        return res;
    }

    // Метод для перемещения ломаной линии на заданный вектор
    @Override
    public IShape shift(Point2D a) {
        // Создание нового массива точек
        Point2D[] res = new Point2D[n];
        // Перемещение каждой точки линии на заданный вектор
        for (int i = 0; i < n; i++) {
            res[i] = new Point2D(new double[]{p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1)});
        }
        // Создание новой ломаной линии с перемещенными точками
        return new Polyline(res);
    }

    // Метод для поворота ломаной линии на заданный угол
    @Override
    public IShape rot(double phi) {
        // Создание нового массива точек
        Point2D[] res = new Point2D[n];
        // Поворот каждой точки линии на заданный угол
        for (int i = 0; i < n; i++) {
            res[i] = p[i].rot(phi);
        }
        // Создание новой ломаной линии с повернутыми точками
        return new Polyline(res);
    }

    // Метод для выполнения симметрии ломаной линии относительно заданной оси
    @Override
    public IShape symAxis(int i) {
        // Создание нового массива точек
        Point2D[] res = new Point2D[n];
        // Выполнение симметрии каждой точки линии относительно заданной оси
        for (int j = 0; j < n; j++) {
            res[j] = (Point2D) p[j].symAxis(i);
        }
        // Создание новой ломаной линии с симметричными точками
        return new Polyline(res);
    }

    // Переопределение метода проверки пересечения для класса Classes.Polyline
    @Override
    public boolean cross(IShape i) {
        if (!(i instanceof Polyline)) {
            throw new IllegalArgumentException("Аргумент должен быть экземпляром класса Classes.Polyline");
        }

        // Привести аргумент к типу Classes.Polyline
        Polyline other = (Polyline) i;

        // Проверить пересечения всех отрезков текущей и другой полилиний
        for (int j = 0; j < n - 1; j++) {
            for (int k = 0; k < other.n - 1; k++) {
                // Получить координаты отрезков в формате начало-конец
                Point2D p1 = p[j];
                Point2D p2 = p[j + 1];
                Point2D q1 = other.p[k];
                Point2D q2 = other.p[k + 1];
                if (new Segment(p1, p2).cross(new Segment(q1, q2))) {
                    return true;
                }
            }
        }

        // Если пересечений не найдено, вернуть false
        return false;
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder("[ ");
        for (int i = 0; i < n; i++) {
            res.append(p[i].toString());
            if (i < n - 1) {
                res.append(", ");
            }
        }
        res.append(" ]");
        return res.toString();
    }
}
