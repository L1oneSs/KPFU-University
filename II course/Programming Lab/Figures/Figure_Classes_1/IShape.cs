using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figure_Classes_1
{
    public interface IShape
    {
        double square(); // площадь фигуры
        double length(); // длина/периметр фигуры
        IShape shift(Point2D a); // сдвиг фигуры на вектор заданный объектом класса Point2D
        IShape rot(double phi); // поворот фигуры на угол phi в радианах относительно начала координат
        IShape symAxis(int i); // симметрия точки относительно оси под заданным номером
        bool cross(IShape i); // проверка на пересечение с другой фигурой
    }
}
