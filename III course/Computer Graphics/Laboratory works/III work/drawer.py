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
        line_points = bresenham(x1, y1, x2, y2)

        # Преобразуем line_points в массив NumPy перед индексацией, иначе происходит ошибка
        line_points = np.array(line_points)
        # берем y,x и задаем цвет в черный
        image[line_points[:, 1], line_points[:, 0]] = 0


def paint_cat(image, type, color, coord_list):
    height, width, _ = image.shape
    background_color = image[0, 0]

    def is_valid(x, y):
        return 0 <= x < height and 0 <= y < width

    def flood_fill(start_x, start_y):
        stack = [(start_x, start_y)]

        while stack:
            x, y = stack.pop()

            if is_valid(x, y) and np.array_equal(image[x, y], background_color):
                image[x, y] = color
                if coord_list is not None:
                    coord_list.append((y, x))
                stack.append((x + 1, y))
                stack.append((x - 1, y))
                stack.append((x, y + 1))
                stack.append((x, y - 1))

    if type == "body":
        flood_fill(height // 2, width // 2 - 100)
    elif type == "tail":
        flood_fill(850, 530 - 100)
    elif type == "eye_1":
        flood_fill(280, 270 - 100)
    elif type == "eye_2":
        flood_fill(275, 380 - 100)
    elif type == "pupil_1":
        flood_fill(260, 250 - 100)
    elif type == "pupil_2":
        flood_fill(250, 410 - 100)
