from bresenham import bresenham
import numpy as np

# Определение градиента от красного к желтому
red = np.array([1.0, 0.0, 0.0])  # Начальный цвет (красный)
yellow = np.array([1.0, 1.0, 0.0])  # Конечный цвет (желтый)

# Функция для рисования треугольника
def draw_triangle(image, drawvertices, left_x, right_x):
    for i in range(3):

        x1, y1 = drawvertices[i]
        x2, y2 = drawvertices[(i + 1) % 3]
        points = bresenham(x1, y1, x2, y2)

        for x, y in points:
            if x == 512 // 2 or y == 512 // 2:
                image[-y, x] = np.array([1.0, 1.0, 1.0])
            else:
                # Нормализуем значение пикселя X в [0,1]
                t = (x - left_x) / (right_x - left_x)
                # Выполняем интерполяцию
                current_color = red + t * (yellow - red)

                # Устанавливаем цвет пикселя (строка, столбец)
                image[-y, x] = current_color
            if x == 512 // 2 and y == 512 // 2:
                image[-y, x] = np.array([0.0, 0.0, 1.0])
