using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figure_Classes_1
{
    public interface IPolyPoint
    {
        Point2D getP(int i); // возвращает координаты i-ой вершины многоугольника в виде объекта Point2D
        void setP(Point2D p, int i); // устанавливает новые координаты i-ой вершины многоугольника на основе объекта Point2D
    }
}
