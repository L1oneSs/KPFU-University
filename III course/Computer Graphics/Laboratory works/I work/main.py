import numpy as np
from triangle_methods import triangle_area
from triangle_methods import semiperimetr
from triangle_methods import max_cosine

file_path = "teapot.txt"

vertices = []  # Вершины
edges = []  # Грани


def radians_to_degrees(rad):
    return round(rad * 180 / np.pi, 2)


# Считывание граней и вершин в массивы
with open(file_path, 'r') as file:
    for line in file:
        if not line:
            continue  # Пропускаем пустые строки
        if line.startswith('v '):
            data = line.split()
            vertices.append((float(data[1]), float(data[2]), float(data[3])))
        elif line.startswith('f '):
            data = line.split()
            edges.append((int(data[1]), int(data[2]), int(data[3])))

total_area = 0  # Суммарная площадь всех вписанных окружностей
max_cos = -1  # Максимальный косинус
vertices_of_max_cos_triangle = None  # Вершины треугольника с максимальным косинусом

for edge in edges:
    v1, v2, v3 = [vertices[i - 1] for i in edge]
    S = triangle_area(v1, v2, v3)
    p = semiperimetr(v1, v2, v3)

    total_area += np.pi * (S / p) ** 2
    cos = max_cosine(v1, v2, v3)
    if cos > max_cos:
        max_cos = cos
        vertices_of_max_cos_triangle = (v1, v2, v3)

print(f"\nСуммарная площадь всех вписанных окружностей: {total_area}\n")
print(f"Максимальный косинус угла Rad: {max_cos}, Deg: {radians_to_degrees(max_cos)}. Треугольник с вершинами: {vertices_of_max_cos_triangle}")
