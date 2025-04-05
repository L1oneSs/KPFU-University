using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figure_Classes_1
{
    // Четырехугольник
    public class QGon : NGon
    {
        public QGon(Point2D[] p) : base(p) { }

        // Переопределение метода вычисления площади четырехугольника
        public override double square()
        {
            // Вычисление длин сторон многоугольника
            double a = Math.Sqrt(Math.Pow(p[1].getX(0) - p[0].getX(0), 2) + Math.Pow(p[1].getX(1) - p[0].getX(1), 2));
            double b = Math.Sqrt(Math.Pow(p[2].getX(0) - p[1].getX(0), 2) + Math.Pow(p[2].getX(1) - p[1].getX(1), 2));
            double c = Math.Sqrt(Math.Pow(p[0].getX(0) - p[2].getX(0), 2) + Math.Pow(p[0].getX(1) - p[2].getX(1), 2));

            // Вычисление полупериметра многоугольника
            double pr = (a + b + c) / 2;
            // Вычисление площади треугольника методом Герона
            double pr1 = Math.Sqrt(pr * (pr - a) * (pr - b) * (pr - c));

            a = Math.Sqrt(Math.Pow(p[0].getX(0) - p[3].getX(0), 2) + Math.Pow(p[0].getX(1) - p[3].getX(1), 2));
            b = Math.Sqrt(Math.Pow(p[3].getX(0) - p[2].getX(0), 2) + Math.Pow(p[3].getX(1) - p[2].getX(1), 2));

            // Вычисление полупериметра второго треугольника
            pr = (a + b + c) / 2;
            // Вычисление площади второго треугольника методом Герона
            double pr2 = Math.Sqrt(pr * (pr - a) * (pr - b) * (pr - c));

            // Возвращение суммы площадей двух треугольников
            return pr1 + pr2;

        }

        // Переопределение метода сдвига многоугольника на заданный вектор
        public override IShape shift(Point2D a)
        {
            Point2D[] res = new Point2D[n];
            for (int i = 0; i < n; i++)
            {
                res[i] = new Point2D(new double[] { p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1) });
            }
            return new QGon(res);
        }

        // Переопределение метода поворота многоугольника на заданный угол
        public override IShape rot(double phi)
        {
            Point2D[] res = new Point2D[n];
            for (int i = 0; i < n; i++)
            {
                res[i] = p[i].rot(phi);
            }
            return new QGon(res);
        }

        // Симметрично отражаем многоугольник относительно оси i
        public override IShape symAxis(int i)
        {
            Point2D[] res = new Point2D[n];
            for (int j = 0; j < n; j++)
            {
                res[j] = (Point2D)p[j].symAxis(i);
            }
            return new QGon(res);
        }
    }
}
