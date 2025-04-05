package com.figures.interfaces;

import com.figures.figures.points.Point2D;

public interface IPolyPoint {
    Point2D getP(int i); // возвращает координаты i-ой вершины многоугольника в виде объекта Classes.Point2D
    void setP(Point2D p, int i); // устанавливает новые координаты i-ой вершины многоугольника на основе объекта Classes.Point2D
}
