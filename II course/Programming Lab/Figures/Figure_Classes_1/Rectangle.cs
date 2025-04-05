using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figure_Classes_1
{
    public class Rectangle : QGon
    {
        public Rectangle(Point2D[] p) : base(p) { if (!IsRectangle()) throw new ArgumentException("Введите корректные данные для прямоугольника!"); }
        public override double square()
        {
            // вычисление длины сторон прямоугольника по координатам вершин
            double a = Math.Sqrt(Math.Pow(p[1].getX(0) - p[0].getX(0), 2) + Math.Pow(p[1].getX(1) - p[0].getX(1), 2));
            double b = Math.Sqrt(Math.Pow(p[2].getX(0) - p[1].getX(0), 2) + Math.Pow(p[2].getX(1) - p[1].getX(1), 2));
            // вычисление площади прямоугольника
            return a * b;
        }

        public bool IsRectangle()
        {
            // проверяем, что противоположные стороны равны и параллельны
            bool parallel = false;
            bool equal = false;
            for (int i = 0; i < 4; i++)
            {
                int j = (i + 1) % 4;
                int k = (i + 2) % 4;
                int l = (i + 3) % 4;
                if (p[i].getX(0) == p[j].getX(0) && p[k].getX(0) == p[l].getX(0))
                {
                    if (p[i].getX(1) < p[j].getX(1))
                    {
                        if (p[k].getX(1) > p[l].getX(1) && p[k].getX(1) > p[i].getX(1) && p[l].getX(1) < p[j].getX(1))
                        {
                            parallel = true;
                            equal = (p[j].getX(1) - p[i].getX(1)) == (p[l].getX(1) - p[k].getX(1));
                        }
                    }
                    else
                    {
                        if (p[l].getX(1) > p[k].getX(1) && p[l].getX(1) > p[j].getX(1) && p[k].getX(1) < p[i].getX(1))
                        {
                            parallel = true;
                            equal = (p[i].getX(1) - p[j].getX(1)) == (p[k].getX(1) - p[l].getX(1));
                        }
                    }
                }
            }

            return parallel && equal;
        }

        public override IShape shift(Point2D a)
        {
            // создание массива вершин сдвинутого прямоугольника
            Point2D[] res = new Point2D[n];
            for (int i = 0; i < n; i++)
            {
                res[i] = new Point2D(new double[] { p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1) });
            }
            // создание нового прямоугольника с измененными координатами вершин
            return new Rectangle(res);
        }

        public override IShape rot(double phi)
        {
            // создание массива вершин повернутого прямоугольника
            Point2D[] res = new Point2D[n];
            for (int i = 0; i < n; i++)
            {
                res[i] = p[i].rot(phi);
            }
            // создание нового прямоугольника с измененными координатами вершин
            return new Rectangle(res);
        }

        public override IShape symAxis(int i)
        {
            // создание массива вершин отраженного прямоугольника
            Point2D[] res = new Point2D[n];
            for (int j = 0; j < n; j++)
            {
                res[j] = (Point2D)p[j].symAxis(i);
            }
            // создание нового прямоугольника с измененными координатами вершин
            return new Rectangle(res);
        }

    }
}
