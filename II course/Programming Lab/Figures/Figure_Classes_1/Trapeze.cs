using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figure_Classes_1
{
    public class Trapeze : QGon
    {
        public Trapeze(Point2D[] p) : base(p)
        {
            if (!IsTrapezoid())
            {
                throw new ArgumentException("Введите корректные данные для трапеции!");
            }               
        }
        // Метод для вычисления площади трапеции
        public override double square()
        {
            // Вычисляем угол наклона трапеции
            double k1 = (p[2].getX(1) - p[0].getX(1)) / (p[2].getX(0) - p[0].getX(0));
            double k2 = (p[3].getX(1) - p[1].getX(1)) / (p[3].getX(0) - p[1].getX(0));
            double phi = Math.Atan((k2 - k1) / (1 + k1 * k2));

            // Вычисляем длины оснований трапеции
            double a = Math.Sqrt(Math.Pow(p[2].getX(0) - p[0].getX(0), 2) + Math.Pow(p[2].getX(1) - p[0].getX(1), 2));
            double b = Math.Sqrt(Math.Pow(p[3].getX(0) - p[1].getX(0), 2) + Math.Pow(p[3].getX(1) - p[1].getX(1), 2));

            // Вычисляем площадь трапеции
            return 0.5 * a * b * Math.Abs(Math.Sin(phi));
        }

        public bool IsTrapezoid()
        {
            // определяем, лежат ли две вершины на одной горизонтальной линии, а две другие - на другой горизонтальной линии, параллельной первой
            bool parallel = false;
            bool horizontal = false;
            for (int i = 0; i < 4; i++)
            {
                int j = (i + 1) % 4;
                int k = (i + 2) % 4;
                int l = (i + 3) % 4;
                if (p[i].getX(1) == p[j].getX(1) && p[k].getX(1) == p[l].getX(1) && p[i].getX(1) == p[k].getX(1))
                {
                    horizontal = true;
                    if (p[i].getX(0) < p[j].getX(0))
                    {
                        if (p[k].getX(0) > p[l].getX(0) && p[k].getX(0) > p[i].getX(0) && p[l].getX(0) < p[j].getX(0))
                        {
                            parallel = true;
                        }
                    }
                    else
                    {
                        if (p[l].getX(0) > p[k].getX(0) && p[l].getX(0) > p[j].getX(0) && p[k].getX(0) < p[i].getX(0))
                        {
                            parallel = true;
                        }
                    }
                }
            }

            return parallel && horizontal;
        }

        // Метод для перемещения трапеции на заданный вектор
        public override IShape shift(Point2D a)
        {
            // Создаем новый массив точек, сдвинув каждую точку на заданный вектор
            Point2D[] res = new Point2D[n];
            for (int i = 0; i < n; i++)
            {
                res[i] = new Point2D(new double[] { p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1) });
            }
            return new Trapeze(res);
        }

        // Метод для поворота трапеции на заданный угол
        public override IShape rot(double phi)
        {
            // Создаем новый массив точек, повернув каждую точку на заданный угол
            Point2D[] res = new Point2D[n];
            for (int i = 0; i < n; i++)
            {
                res[i] = p[i].rot(phi);
            }
            return new Trapeze(res);
        }

        // Метод для отражения трапеции относительно оси симметрии
        public override IShape symAxis(int i)
        {
            // Создаем новый массив точек, отразив каждую точку относительно оси симметрии
            Point2D[] res = new Point2D[n];
            for (int j = 0; j < n; j++)
            {
                res[j] = (Point2D)p[j].symAxis(i);
            }
            return new Trapeze(res);
        }

    }
}
