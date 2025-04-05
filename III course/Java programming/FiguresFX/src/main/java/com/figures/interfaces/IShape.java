package com.figures.interfaces;

import com.figures.figures.points.Point2D;

public interface IShape {
    double square(); // площадь фигуры
    double length(); // длина/периметр фигуры
    IShape shift(Point2D a); // сдвиг фигуры на вектор, заданный объектом класса Classes.Point2D
    IShape rot(double phi); // поворот фигуры на угол phi в радианах относительно начала координат
    IShape symAxis(int i); // симметрия фигуры относительно оси под заданным номером
    boolean cross(IShape i); // проверка на пересечение с другой фигурой
}
