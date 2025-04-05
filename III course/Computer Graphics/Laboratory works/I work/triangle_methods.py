import numpy as np

# Площадь треугольника
def triangle_area(v1, v2, v3):
    a = distance(v1, v2)
    b = distance(v2, v3)
    c = distance(v3, v1)
    p = (a + b + c) / 2
    return np.sqrt(p * (p - a) * (p - b) * (p - c))

# Полупериметр
def semiperimetr(v1, v2, v3):
    a = distance(v1, v2)
    b = distance(v2, v3)
    c = distance(v3, v1)
    return (a + b + c) / 2

# Длина вектора
def distance(v1, v2):
    x1, y1, z1 = v1
    x2, y2, z2 = v2
    return np.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

# Координаты вектора по двум точкам
def vector_coords(v1, v2):
    return [v2[0] - v1[0], v2[1] - v1[1], v2[2] - v1[2]]

# Произведение двух векторов
def vector_prod(vector1, vector2):
    return vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]

# Поиск максимального косинуса угла в треугольнике
def max_cosine(v1, v2, v3):
    coords_a = vector_coords(v1, v2)
    coords_b = vector_coords(v2, v3)
    coords_c = vector_coords(v1, v3)

    cosine_ab = vector_prod(coords_a, coords_b) / (distance(v1, v2) * distance(v2, v3))

    cosine_bc = vector_prod(coords_b, coords_c) / (distance(v2, v3) * distance(v3, v1))

    cosine_ca = vector_prod(coords_c, coords_a) / (distance(v3, v1) * distance(v1, v2))

    return max(cosine_ab, cosine_bc, cosine_ca)

