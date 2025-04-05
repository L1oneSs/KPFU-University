from bresenham import bresenham
from bezier import linear_bezier, quadratic_bezier, cubic_bezier
import numpy as np


def draw_curve(image, control_points, coord_list):
    curve_points = []

    if len(control_points) == 2:
        x, y = linear_bezier(control_points[0], control_points[1])
        curve_points.extend(zip(x, y))
        if coord_list is not None:
            coord_list.extend(zip(x, y))

    elif len(control_points) == 3:
        x, y = quadratic_bezier(control_points[0], control_points[1], control_points[2])
        curve_points.extend(zip(x, y))
        if coord_list is not None:
            coord_list.extend(zip(x, y))

    elif len(control_points) == 4:
        x, y = cubic_bezier(control_points[0], control_points[1], control_points[2], control_points[3])
        curve_points.extend(zip(x, y))
        if coord_list is not None:
            coord_list.extend(zip(x, y))


    else:
        print("Unsupported number of control points. Supported: 2 (linear), 3 (quadratic), or 4 (cubic)")
        return

    # Отрисовываем кривую методом Брезенхэма
    for i in range(len(curve_points) - 1):
        x1, y1 = curve_points[i]
        x2, y2 = curve_points[i + 1]
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        if 0 <= x1 < image.shape[1] and 0 <= y1 < image.shape[0] and 0 <= x2 < image.shape[1] and 0 <= y2 < image.shape[0]:
            line_points = bresenham(x1, y1, x2, y2)

            # Преобразуем line_points в массив NumPy перед индексацией, иначе происходит ошибка
            line_points = np.array(line_points)
            # берем y,x и задаем цвет в черный
            image[line_points[:, 1], line_points[:, 0]] = 0
