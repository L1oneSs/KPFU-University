package com.figures.figures.points;

public class Point2D extends Point {
    // Конструктор без параметров, создающий двумерную точку
    public Point2D() {
        super(2);
    }

    // Конструктор, принимающий массив координат, создающий двумерную точку
    public Point2D(double[] x) {
        super(2, x);
    }

    // Метод, возвращающий новую точку, полученную из данной поворотом на угол phi
    public static Point2D rot(Point2D a, double phi) {
        double[] res = new double[2];
        res[0] = a.x[0] * Math.cos(phi) - a.x[1] * Math.sin(phi);
        res[1] = a.x[0] * Math.sin(phi) + a.x[1] * Math.cos(phi);
        return new Point2D(res);
    }

    // Метод, поворачивающий данную точку на угол phi и возвращающий новую точку
    public Point2D rot(double phi) {
        double[] res = new double[2];
        res[0] = x[0] * Math.cos(phi) - x[1] * Math.sin(phi);
        res[1] = x[0] * Math.sin(phi) + x[1] * Math.cos(phi);
        return new Point2D(res);
    }

    // Метод, возвращающий новую точку, полученную из данной симметрией относительно оси i
    @Override
    public Point symAxis(int i) {
        double[] res = new double[2];
        for (int j = 0; j < dim; j++) {
            res[j] = x[j];
        }
        if (i < 0 || i >= 2) {
            throw new IllegalArgumentException("Неверный номер оси.");
        }

        if (i == 0)
            res[1] = -res[1];
        else
            res[0] = -res[0];

        return new Point2D(res);
    }
}
