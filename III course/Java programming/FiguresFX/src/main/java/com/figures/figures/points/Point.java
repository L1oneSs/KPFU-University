package com.figures.figures.points;

public class Point {
    protected int dim; // Размерность пространства
    protected double[] x; // Массив координат точки

    // Конструктор класса с одним параметром - размерностью пространства
    public Point(int dim) {
        // Инициализация поля dim переданным значением
        this.dim = dim;
        // Создание массива x размерности dim
        x = new double[dim];
    }

    // Конструктор класса с двумя параметрами - размерностью пространства и массивом координат
    public Point(int dim, double[] x) {
        // Проверка соответствия размерности массива x заданной размерности пространства
        if (dim != x.length) {
            // Выброс исключения с сообщением о неправильной размерности массива
            throw new IllegalArgumentException("Размерность массива не совпадает с заданной размерностью пространства.");
        }
        // Инициализация полей dim и x переданными значениями
        this.dim = dim;
        this.x = x;
    }

    // Метод для получения значения поля dim
    public int getDim() {
        return dim;
    }

    // Метод для получения массива координат точки
    public double[] getX() {
        return x;
    }

    // Метод для получения значения i-й координаты точки
    public double getX(int i) {
        // Проверка правильности переданного индекса
        if (i < 0 || i >= dim) {
            // Выброс исключения с сообщением о неправильном индексе
            throw new IllegalArgumentException("Неверный индекс координаты.");
        }
        return x[i];
    }

    // Метод для установки нового массива координат точки
    public void setX(double[] x) {
        // Проверка соответствия размерности переданного массива x заданной размерности пространства
        if (dim != x.length) {
            // Выброс исключения с сообщением о неправильной размерности массива
            throw new IllegalArgumentException("Размерность массива не совпадает с заданной размерностью пространства.");
        }
        this.x = x;
    }

    // Метод для установки нового значения i-й координаты точки
    public void setX(double x, int i) {
        // Проверка правильности переданного индекса
        if (i < 0 || i >= dim) {
            // Выброс исключения с сообщением о неправильном индексе
            throw new IllegalArgumentException("Неверный индекс координаты.");
        }
        this.x[i] = x;
    }

    // метод для вычисления модуля точки(расстояние от начала координат)
    public double abs() {
        // инициализируем переменную суммой квадратов координат точки
        double sum = 0;
        for (int i = 0; i < dim; i++) {
            // квадрат координаты i-ой оси добавляется к сумме
            sum += x[i] * x[i];
        }
        // вычисляем корень суммы квадратов координат и возвращаем его
        return Math.sqrt(sum);
    }

    // сумма точек
    public static Point add(Point a, Point b) {
        // проверяем, что размерности точек совпадают
        if (a.dim != b.dim) {
            throw new IllegalArgumentException("Размерности точек не совпадают.");
        }
        // инициализируем массив координат результата
        double[] res = new double[a.dim];
        for (int i = 0; i < a.dim; i++) {
            // складываем координаты a и b на каждой оси и сохраняем результат в массив res
            res[i] = a.x[i] + b.x[i];
        }
        // создаем новую точку с координатами из массива res и возвращаем ее
        return new Point(a.dim, res);
    }

    public Point add(Point b) {
        // проверяем, что размерности точек совпадают
        if (dim != b.dim) {
            throw new IllegalArgumentException("Размерности точек не совпадают.");
        }
        // инициализируем массив координат результата
        double[] res = new double[dim];
        for (int i = 0; i < dim; i++) {
            // складываем координаты текущей точки и точки b на каждой оси и сохраняем результат в массив res
            res[i] = x[i] + b.x[i];
        }
        // создаем новую точку с координатами из массива res и возвращаем ее
        return new Point(dim, res);
    }

    // разность точек
    public static Point sub(Point a, Point b) {
        // проверяем, что размерности точек совпадают
        if (a.dim != b.dim) {
            throw new IllegalArgumentException("Размерности точек не совпадают.");
        }
        // инициализируем массив координат результата
        double[] res = new double[a.dim];
        for (int i = 0; i < a.dim; i++) {
            // вычитаем координаты b из координат a на каждой оси и сохраняем результат в массив res
            res[i] = a.x[i] - b.x[i];
        }
        // создаем новую точку с координатами из массива res и возвращаем ее
        return new Point(a.dim, res);
    }

    public Point sub(Point b) {
        // проверяем, что размерности точек совпадают
        if (dim != b.dim) {
            throw new IllegalArgumentException("Размерности точек не совпадают.");
        }
        // создаем массив для хранения разности координат
        double[] res = new double[dim];
        // вычисляем разность координат
        for (int i = 0; i < dim; i++) {
            res[i] = x[i] - b.x[i];
        }
        // возвращаем новую точку с полученными координатами
        return new Point(dim, res);
    }

    // умножение точки на число
    public static Point mult(Point a, double r) {
        // создаем массив для хранения результата умножения
        double[] res = new double[a.dim];
        // умножаем каждую координату на заданный коэффициент
        for (int i = 0; i < a.dim; i++) {
            res[i] = a.x[i] * r;
        }
        // возвращаем новую точку с полученными координатами
        return new Point(a.dim, res);
    }

    public Point mult(double r) {
        // создаем массив для хранения результата умножения
        double[] res = new double[dim];
        // умножаем каждую координату на заданный коэффициент
        for (int i = 0; i < dim; i++) {
            res[i] = x[i] * r;
        }
        // возвращаем новую точку с полученными координатами
        return new Point(dim, res);
    }

    public static double mult(Point a, Point b) {
        // проверяем, что размерности точек совпадают
        if (a.dim != b.dim) {
            throw new IllegalArgumentException("Размерности точек не совпадают.");
        }
        // вычисляем скалярное произведение
        double res = 0;
        for (int i = 0; i < a.dim; i++) {
            res += a.x[i] * b.x[i];
        }
        // возвращаем результат
        return res;
    }

    public double mult(Point b) {
        if (dim != b.dim) {
            throw new IllegalArgumentException("Размерности точек не совпадают.");
        }
        double res = 0;
        for (int i = 0; i < dim; i++) {
            res += x[i] * b.x[i];
        }
        return res;
    }

    // симметричное отражение относительно i-ой оси
    public static Point symAxis(Point a, int i) {
        // Создаем новый массив для точки, чтобы не изменять исходный массив.
        double[] res = new double[a.dim];
        for (int j = 0; j < a.dim; j++) {
            res[j] = a.x[j];
        }

        // Проверяем, что номер оси не выходит за границы размерности точки.
        if (i < 0 || i >= a.dim) {
            throw new IllegalArgumentException("Неверный номер оси.");
        }

        // Симметрия точки относительно оси путем инвертирования всех координат точки, кроме координаты, соответствующей оси симметрии.
        for (int k = 0; k < a.dim; k++) {
            if (k != i) {
                res[k] = -res[k];
            }
        }

        // Возвращаем новую точку, полученную после симметрии.
        return new Point(a.dim, res);
    }

    public Point symAxis(int i) {
        // Создаем новый массив для точки, чтобы не изменять исходный массив.
        double[] res = new double[dim];
        for (int j = 0; j < dim; j++) {
            res[j] = x[j];
        }

        // Проверяем, что номер оси не выходит за границы размерности точки.
        if (i < 0 || i >= dim) {
            throw new IllegalArgumentException("Неверный номер оси.");
        }

        // Симметрия точки относительно оси путем инвертирования всех координат точки, кроме координаты, соответствующей оси симметрии.
        for (int k = 0; k < dim; k++) {
            if (k != i) {
                res[k] = -res[k];
            }
        }

        // Возвращаем новую точку, полученную после симметрии.
        return new Point(dim, res);
    }

    @Override
    public String toString() {
        StringBuilder res = new StringBuilder("(").append(x[0]);
        for (int i = 1; i < dim; i++) {
            res.append(", ").append(x[i]);
        }
        res.append(")");
        return res.toString();
    }
}
