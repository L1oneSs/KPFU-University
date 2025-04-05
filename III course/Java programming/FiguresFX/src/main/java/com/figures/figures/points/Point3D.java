package com.figures.figures.points;

public class Point3D extends Point {
    public Point3D() {
        super(3);
    }

    public Point3D(double[] x) {
        super(3, x);
    }

    // Статический метод, вычисляющий векторное произведение двух векторов типа Classes.Point3D
    public static Point3D cross_prod(Point3D p1, Point3D p2) {
        double[] res = new double[3];
        res[0] = p1.x[1] * p2.x[2] - p1.x[2] * p2.x[1];
        res[1] = p1.x[2] * p2.x[0] - p1.x[0] * p2.x[2];
        res[2] = p1.x[0] * p2.x[1] - p1.x[1] * p2.x[0];
        return new Point3D(res);
    }

    // Метод, вычисляющий векторное произведение текущего объекта типа Classes.Point3D и переданного в метод объекта типа Classes.Point3D
    public Point3D cross_prod(Point3D p) {
        double[] res = new double[3];
        res[0] = x[1] * p.x[2] - x[2] * p.x[1];
        res[1] = x[2] * p.x[0] - x[0] * p.x[2];
        res[2] = x[0] * p.x[1] - x[1] * p.x[0];
        return new Point3D(res);
    }

    // Статический метод, вычисляющий смешанное произведение трех векторов типа Classes.Point3D
    public static double mix_prod(Point3D p1, Point3D p2, Point3D p3) {
        return p1.x[0] * (p2.x[1] * p3.x[2] - p3.x[1] * p2.x[2])
                + p1.x[1] * (p2.x[2] * p3.x[0] - p3.x[2] * p2.x[0])
                + p1.x[2] * (p2.x[0] * p3.x[1] - p3.x[0] * p2.x[1]);
    }

    // Метод, вычисляющий смешанное произведение текущего объекта типа Classes.Point3D и двух переданных в метод объектов типа Classes.Point3D
    public double mix_prod(Point3D p1, Point3D p2) {
        return x[0] * (p1.x[1] * p2.x[2] - p2.x[1] * p1.x[2])
                + x[1] * (p1.x[2] * p2.x[0] - p2.x[2] * p1.x[0])
                + x[2] * (p1.x[0] * p2.x[1] - p2.x[0] * p1.x[1]);
    }
}
