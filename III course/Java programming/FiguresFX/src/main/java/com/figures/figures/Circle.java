package com.figures.figures;

import com.figures.figures.points.Point2D;
import com.figures.interfaces.IShape;

public class Circle implements IShape {
    // Приватные поля класса, хранящие радиус и координаты центра окружности
    private double r;
    private Point2D p;

    // Конструктор класса Classes.Circle, принимающий координаты центра окружности и ее радиус
    public Circle(Point2D p, double r) {
        // Проверка на правильность введенных данных
        if (r <= 0) {
            throw new IllegalArgumentException("Неверный радиус.");
        }
        // Присвоение значений полям
        this.p = p;
        this.r = r;
    }

    // Метод для получения координат центра окружности
    public Point2D getP() {
        return p;
    }

    // Метод для изменения координат центра окружности
    public void setP(Point2D p) {
        this.p = p;
    }

    // Метод для получения радиуса окружности
    public double getR() {
        return r;
    }

    // Метод для изменения радиуса окружности
    public void setR(double r) {
        this.r = r;
    }

    // Метод для вычисления площади окружности
    public double square() {
        return Math.PI * r * r;
    }

    // Метод для вычисления длины окружности
    public double length() {
        return 2 * Math.PI * r;
    }

    // Метод для перемещения окружности на заданный вектор
    public IShape shift(Point2D a) {
        return new Circle(new Point2D(new double[]{p.getX(0) + a.getX(0), p.getX(1) + a.getX(1)}), r);
    }

    // Метод для поворота окружности на заданный угол
    public IShape rot(double phi) {
        return new Circle(p.rot(phi), r);
    }

    // Метод для получения симметричной окружности относительно заданной оси
    public IShape symAxis(int i) {
        return new Circle((Point2D) p.symAxis(i), r);
    }

    // Метод для проверки пересечения данной окружности с другой фигурой
    public boolean cross(IShape i) {
        // Если входной параметр является экземпляром класса Classes.Circle, то выполняется следующее
        if (i instanceof Circle) {
            // Приведение входного параметра к типу Classes.Circle
            Circle c = (Circle) i;
            // Вычисление расстояния между центрами окружностей
            double res = Math.sqrt(Math.pow(p.getX(0) - c.p.getX(0), 2) + Math.pow(p.getX(1) - c.p.getX(1), 2));
            // Проверка на пересечение окружностей
            return res < (r + c.r) && res > Math.abs(r - c.r);
        } else {
            throw new IllegalArgumentException("Аргумент должен быть экземпляром класса Classes.Circle");
        }
    }

    // Переопределение метода toString
    @Override
    public String toString() {
        return "[Центр:" + p + ", радиус: " + r + "]";
    }
}
