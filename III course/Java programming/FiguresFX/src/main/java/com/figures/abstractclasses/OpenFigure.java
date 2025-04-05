package com.figures.abstractclasses;

import com.figures.figures.points.Point2D;
import com.figures.interfaces.IShape;

public abstract class OpenFigure implements IShape {

    @Override
    public double square() {
        return 0;
    }

    public abstract double length();
    public abstract IShape shift(Point2D a);
    public abstract IShape rot(double phi);
    public abstract IShape symAxis(int i);
    public abstract boolean cross(IShape i);
}
