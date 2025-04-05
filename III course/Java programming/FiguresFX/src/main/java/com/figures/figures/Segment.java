package com.figures.figures;

import com.figures.abstractclasses.OpenFigure;
import com.figures.figures.points.Point2D;
import com.figures.interfaces.IShape;

public class Segment extends OpenFigure {
    private Point2D start; // начальная точка сегмента
    private Point2D finish; // конечная точка сегмента

    // Конструктор, принимающий начальную и конечную точки
    public Segment(Point2D s, Point2D f) {
        start = s;
        finish = f;
    }

    // Методы получения и установки начальной точки
    public Point2D getStart() {
        return start;
    }

    public void setStart(Point2D a) {
        start = a;
    }

    // Методы получения и установки конечной точки
    public Point2D getFinish() {
        return finish;
    }

    public void setFinish(Point2D a) {
        finish = a;
    }

    // Метод, вычисляющий длину сегмента
    @Override
    public double length() {
        double dx = finish.getX(0) - start.getX(0);
        double dy = finish.getX(1) - start.getX(1);
        return Math.sqrt(dx * dx + dy * dy);
    }

    // Метод сдвига (перемещения) отрезка на заданный вектор
    @Override
    public IShape shift(Point2D a) {
        // Создание новых точек с координатами, сдвинутыми на заданный вектор
        Point2D newStart = new Point2D(new double[]{start.getX(0) + a.getX(0), start.getX(1) + a.getX(1)});
        Point2D newFinish = new Point2D(new double[]{finish.getX(0) + a.getX(0), finish.getX(1) + a.getX(1)});
        // Возвращение нового отрезка с сдвинутыми координатами точек
        return new Segment(newStart, newFinish);
    }

    // Метод поворота отрезка на заданный угол
    @Override
    public IShape rot(double phi) {
        // Создание новых точек, полученных путем поворота исходных точек на заданный угол
        Point2D newStart = start.rot(phi);
        Point2D newFinish = finish.rot(phi);
        // Возвращение нового отрезка с повернутыми координатами точек
        return new Segment(newStart, newFinish);
    }

    // Метод симметрии относительно заданной оси
    @Override
    public IShape symAxis(int i) {
        // Создание новых точек, полученных путем симметрии исходных точек относительно заданной оси
        Point2D newStart = (Point2D) start.symAxis(i);
        Point2D newFinish = (Point2D) finish.symAxis(i);
        // Возвращение нового отрезка с симметричными координатами точек
        return new Segment(newStart, newFinish);
    }

    @Override
    public boolean cross(IShape i) {
        if (!(i instanceof Segment)) {
            throw new IllegalArgumentException("Аргумент должен быть экземпляром класса Classes.Segment");
        }

        // Приведение аргумента i к типу Classes.Segment.
        Segment other = (Segment) i;

        // Получение координат начала и конца отрезков.
        Point2D a = start;
        Point2D b = finish;
        Point2D c = other.start;
        Point2D d = other.finish;

        // Проверка на совпадение координат начала и конца отрезков.
        if (a.getX(0) == c.getX(0) && a.getX(1) == c.getX(1) && b.getX(0) == d.getX(0) && b.getX(1) == d.getX(1))
            return true;

        // Расчет значений переменных для дальнейших проверок.
        double ua = (d.getX(0) - c.getX(0)) * (a.getX(1) - c.getX(1)) - (d.getX(1) - c.getX(1)) * (a.getX(0) - c.getX(0));
        double ub = (b.getX(0) - a.getX(0)) * (a.getX(1) - c.getX(1)) - (b.getX(1) - a.getX(1)) * (a.getX(0) - c.getX(0));
        double denom = (d.getX(1) - c.getX(1)) * (b.getX(0) - a.getX(0)) - (d.getX(0) - c.getX(0)) * (b.getX(1) - a.getX(1));

        // Проверка на то, что отрезки пересекаются.
        if (denom == 0) {
            return false;
        }

        ua /= denom;
        ub /= denom;

        return ua >= 0 && ua <= 1 && ub >= 0 && ub <= 1;
    }

    @Override
    public String toString() {
        return "[ " + start + "; " + finish + " ]";
    }
}
