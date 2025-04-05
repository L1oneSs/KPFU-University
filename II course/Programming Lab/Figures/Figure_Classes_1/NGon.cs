using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Figure_Classes_1
{
    public class NGon : IShape, IPolyPoint
    {
        protected int n; // число вершин многоугольника
        protected Point2D[] p; // массив точек вершин

        public NGon(Point2D[] p) // конструктор принимает массив точек вершин
        {
            if (p.Length < 3) // если число вершин меньше трех
            {
                throw new ArgumentException("Неверное количество углов."); // выбрасываем исключение с сообщением об ошибке
            }
            n = p.Length; // присваиваем числу вершин значение длины массива точек вершин
            this.p = p; // сохраняем массив точек вершин
        }

        public int getN() // метод возвращает число вершин многоугольника
        {
            return n;
        }

        public Point2D[] getP() // метод возвращает массив точек вершин
        {
            return p;
        }

        public Point2D getP(int i) // метод возвращает i-ую точку вершины многоугольника
        {
            if (i < 0 || i >= n) // если i не попадает в диапазон от 0 до n-1
            {
                throw new ArgumentException("Неверный индекс координаты."); // выбрасываем исключение с сообщением об ошибке
            }
            return p[i]; // возвращаем i-ую точку вершины
        }

        public void setP(Point2D[] p) // метод устанавливает новые координаты вершин многоугольника
        {
            this.p = p; // сохраняем новый массив точек вершин
        }

        public void setP(Point2D p, int i) // метод устанавливает новые координаты i-ой вершины многоугольника
        {
            if (i < 0 || i >= n) // если i не попадает в диапазон от 0 до n-1
            {
                throw new ArgumentException("Неверный индекс координаты."); // выбрасываем исключение с сообщением об ошибке
            }
            this.p[i] = p; // сохраняем новую координату i-ой вершины
        }

        // Определяется метод для вычисления площади многоугольника(ПО ФОРМУЛЕ ГАУССА ЧЕРЕЗ ОПРЕДЕЛИТЕЛЬ МАТРИЦЫ)
        public virtual double square()
        {
            double res = 0; // Инициализируется переменная для хранения результата
            double ox = p[0].getX(0); // Получаем значение координаты x первой вершины
            double oy = p[0].getX(1); // Получаем значение координаты y первой вершины
            Point2D[] t = new Point2D[n + 1]; // Создается массив для хранения вершин и добавляется место для первой вершины в конце
                                              // Копируем вершины из исходного массива в массив t
            for (int i = 0; i < n; i++)
            {
                t[i] = p[i];
            }
            t[n] = p[0];


            // Проходим по всем вершинам и вычисляем площадь
            for (int i = 1; i < n + 1; i++)
            {
                double x = t[i].getX(0);
                double y = t[i].getX(1);
                res += (x * oy - y * ox); // Добавляем текущее значение в сумму
                ox = x; // Обновляем значение координаты x
                oy = y; // Обновляем значение координаты y
            }

            return res / 2; // Возвращаем значение площади, поделенной на 2
        }

        // Определяется метод для вычисления периметра многоугольника
        public double length()
        {
            double res = 0; // Инициализируется переменная для хранения результата
                            // Проходим по всем ребрам и вычисляем длину
            for (int i = 0; i < n - 1; i++)
            {
                double dx = p[i + 1].getX(0) - p[i].getX(0); // Вычисляем разницу координат x между соседними вершинами
                double dy = p[i + 1].getX(1) - p[i].getX(1); // Вычисляем разницу координат y между соседними вершинами
                res += Math.Sqrt(dx * dx + dy * dy); // Добавляем длину ребра в сумму
            }

            // Вычисляем длину последнего ребра, соединяющего последнюю и первую вершины
            double l1 = p[n - 1].getX(0) - p[0].getX(0);
            double l2 = p[n - 1].getX(1) - p[0].getX(1);
            res += Math.Sqrt(l1 * l1 + l2 * l2);

            return res; // Возвращаем значение периметра
        }

        // Метод для перемещения фигуры на заданный вектор
        public virtual IShape shift(Point2D a)
        {
            Point2D[] res = new Point2D[n];
            // Цикл для перебора всех вершин фигуры
            for (int i = 0; i < n; i++)
            {
                // Вычисляем новое положение вершины после сдвига на вектор a
                res[i] = new Point2D(new double[] { p[i].getX(0) + a.getX(0), p[i].getX(1) + a.getX(1) });
            }
            // Возвращаем новую фигуру
            return new NGon(res);
        }

        // Метод для поворота фигуры на заданный угол
        public virtual IShape rot(double phi)
        {
            Point2D[] res = new Point2D[n];
            // Цикл для перебора всех вершин фигуры
            for (int i = 0; i < n; i++)
            {
                // Вычисляем новое положение вершины после поворота на угол phi
                res[i] = p[i].rot(phi);
            }
            // Возвращаем новую фигуру
            return new NGon(res);
        }

        // Метод для отражения фигуры относительно заданной оси симметрии
        public virtual IShape symAxis(int i)
        {
            Point2D[] res = new Point2D[n];
            // Цикл для перебора всех вершин фигуры
            for (int j = 0; j < n; j++)
            {
                // Вычисляем новое положение вершины после отражения относительно оси симметрии i
                res[j] = (Point2D)p[j].symAxis(i);
            }
            // Возвращаем новую фигуру
            return new NGon(res);
        }

        public bool cross(IShape i)
        {
            // Проверяем, что аргумент i является экземпляром класса NGon или его наследника
            if (!(i is NGon))
            {
                // Если i не является экземпляром класса NGon или его наследника, выбрасываем исключение ArgumentException
                throw new ArgumentException("Аргумент должен быть экземпляром класса NGon или наследуемого от него класса");
            }

            // Приводим аргумент i к типу NGon и сохраняем в переменную other
            NGon other = i as NGon;

            // Проходимся по всем вершинам другого многоугольника other
            for (int j = 0; j < other.getN(); j++)
            {
                // Проходимся по всем вершинам текущего многоугольника
                for (int k = 0; k < n; k++)
                {
                    // Получаем координаты текущего отрезка (a, b) и отрезка другого многоугольника (c, d)
                    var a = getP(k);
                    var b = getP((k + 1) % n);
                    var c = other.getP(j);
                    var d = other.getP((j + 1) % other.getN());

                    // Проверяем пересекаются ли отрезки a-b и c-d
                    if (new Segment(a, b).cross(new Segment(c, d)))
                    {
                        // Если отрезки пересекаются, возвращаем true
                        return true;
                    }
                }
            }
            // Если ни один отрезок не пересекается, возвращаем false
            return false;
        }

        // Переопределяем ToString
        public override string ToString()
        {
            string res = "[ " + p[0].ToString();

            for (int i = 1; i < n; i++)
            {
                res += ", " + p[i].ToString();
            }

            res += " ]";
            return res;
        }

    }
}
