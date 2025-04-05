using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Windows.Forms.AxHost;

namespace Figure_Classes_1
{
    public class Segment : OpenFigure
    {
        private Point2D start; // начальная точка сегмента
        private Point2D finish; // конечная точка сегмента

        // Конструктор, принимающий начальную и конечную точки
        public Segment(Point2D s, Point2D f)
        {
            start = s;
            finish = f;
        }

        // Методы получения и установки начальной точки
        public Point2D getStart()
        {
            return start;
        }

        public void setStart(Point2D a)
        {
            start = a;
        }

        // Методы получения и установки конечной точки
        public Point2D getFinish()
        {
            return finish;
        }

        public void setFinish(Point2D a)
        {
            finish = a;
        }

        // Метод, вычисляющий длину сегмента
        public override double length()
        {
            double dx = finish.getX(0) - start.getX(0);
            double dy = finish.getX(1) - start.getX(1);
            return Math.Sqrt(dx * dx + dy * dy);
        }

        // Метод сдвига (перемещения) отрезка на заданный вектор
        public override IShape shift(Point2D a)
        {
            // Создание новых точек с координатами, сдвинутыми на заданный вектор
            Point2D newStart = new Point2D(new double[] { start.getX(0) + a.getX(0), start.getX(1) + a.getX(1) });
            Point2D newFinish = new Point2D(new double[] { finish.getX(0) + a.getX(0), finish.getX(1) + a.getX(1) });
            // Возвращение нового отрезка с сдвинутыми координатами точек
            return new Segment(newStart, newFinish);
        }

        // Метод поворота отрезка на заданный угол
        public override IShape rot(double phi)
        {
            // Создание новых точек, полученных путем поворота исходных точек на заданный угол
            Point2D newStart = start.rot(phi);
            Point2D newFinish = finish.rot(phi);
            // Возвращение нового отрезка с повернутыми координатами точек
            return new Segment(newStart, newFinish);
        }

        // Метод симметрии относительно заданной оси
        public override IShape symAxis(int i)
        {
            // Создание новых точек, полученных путем симметрии исходных точек относительно заданной оси
            Point2D newStart = (Point2D)start.symAxis(i);
            Point2D newFinish = (Point2D)finish.symAxis(i);
            // Возвращение нового отрезка с симметричными координатами точек
            return new Segment(newStart, newFinish);
        }

        public override bool cross(IShape i)
        {
            if (!(i is Segment))
            {
                throw new ArgumentException("Аргумент должен быть экземпляром класса Segment");
            }

            // Приведение аргумента i к типу Segment.
            Segment other = i as Segment;

            // Получение координат начала и конца отрезков.
            var a = start;
            var b = finish;
            var c = other.start;
            var d = other.finish;

            // Проверка на совпадение координат начала и конца отрезков.
            if (a.getX(0) == c.getX(0) && a.getX(1) == c.getX(1) && b.getX(0) == d.getX(0) && b.getX(1) == d.getX(1)) return true;

            // Расчет значений переменных для дальнейших проверок.
            var ua = (d.getX(0) - c.getX(0)) * (a.getX(1) - c.getX(1)) - (d.getX(1) - c.getX(1)) * (a.getX(0) - c.getX(0));
            var ub = (b.getX(0) - a.getX(0)) * (a.getX(1) - c.getX(1)) - (b.getX(1) - a.getX(1)) * (a.getX(0) - c.getX(0));
            var denom = (d.getX(1) - c.getX(1)) * (b.getX(0) - a.getX(0)) - (d.getX(0) - c.getX(0)) * (b.getX(1) - a.getX(1));

            // Проверка на то, что отрезки пересекаются.
            if (denom == 0)
            {
                return false;
            }

            ua /= denom;
            ub /= denom;

            if (ua >= 0 && ua <= 1 && ub >= 0 && ub <= 1)
            {
                return true;
            }

            return false;

        }


        public override string ToString()
        {
            string res = "[ " + start + "; " + finish + " ]";
            return res;
        }
    }
}
