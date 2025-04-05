package com.figures.figures;

import com.figures.figures.points.Point2D;
import com.figures.interfaces.IShape;

public class Trapeze extends QGon {
    public Trapeze(Point2D[] p) {
        super(p);
//        if (!isTrapezoid()) {
//            throw new IllegalArgumentException("Введите корректные данные для трапеции!");
//        }
    }

    @Override
    public double square() {
        double k1 = (p[2].getX(1) - p[0].getX(1)) / (p[2].getX(0) - p[0].getX(0));
        double k2 = (p[3].getX(1) - p[1].getX(1)) / (p[3].getX(0) - p[1].getX(0));
        double phi = Math.atan((k2 - k1) / (1 + k1 * k2));

        double a = Math.sqrt(Math.pow(p[2].getX(0) - p[0].getX(0), 2) + Math.pow(p[2].getX(1) - p[0].getX(1), 2));
        double b = Math.sqrt(Math.pow(p[3].getX(0) - p[1].getX(0), 2) + Math.pow(p[3].getX(1) - p[1].getX(1), 2));

        return 0.5 * a * b * Math.abs(Math.sin(phi));
    }

    public boolean isTrapezoid() {
        boolean parallel = false;
        boolean horizontal = false;
        for (int i = 0; i < 4; i++) {
            int j = (i + 1) % 4;
            int k = (i + 2) % 4;
            int l = (i + 3) % 4;
            if (p[i].getX(1) == p[j].getX(1) && p[k].getX(1) == p[l].getX(1) && p[i].getX(1) == p[k].getX(1)) {
                horizontal = true;
                if (p[i].getX(0) < p[j].getX(0)) {
                    if (p[k].getX(0) > p[l].getX(0) && p[k].getX(0) > p[i].getX(0) && p[l].getX(0) < p[j].getX(0)) {
                        parallel = true;
                    }
                } else {
                    if (p[l].getX(0) > p[k].getX(0) && p[l].getX(0) > p[j].getX(0) && p[k].getX(0) < p[i].getX(0)) {
                        parallel = true;
                    }
                }
            }
        }
        return parallel && horizontal;
    }

    @Override
    public IShape shift(Point2D a) {
        Point2D[] res = new Point2D[n];
        for (int i = 0; i < n; i++) {
            res[i] = new Point2D(new double[]{p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1)});
        }
        return new Trapeze(res);
    }

    @Override
    public IShape rot(double phi) {
        Point2D[] res = new Point2D[n];
        for (int i = 0; i < n; i++) {
            res[i] = p[i].rot(phi);
        }
        return new Trapeze(res);
    }

    @Override
    public IShape symAxis(int i) {
        Point2D[] res = new Point2D[n];
        for (int j = 0; j < n; j++) {
            res[j] = (Point2D) p[j].symAxis(i);
        }
        return new Trapeze(res);
    }
}
