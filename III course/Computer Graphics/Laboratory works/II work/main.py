import numpy as np
import matplotlib.pyplot as plt
from drawer import draw_triangle
from win32api import GetSystemMetrics


file_path = "teapot.txt"

vertices = []  # Вершины
edges = []  # Грани

# Размеры монитора
width_monitor = GetSystemMetrics(0)
height_monitor = GetSystemMetrics(1)

M = height_monitor // 3
N = width_monitor // 3


# Создаем матрицу для пикселей изображения и заполняем ее светло-синим цветом
background_color = np.array([0.5, 0.5, 1.0])  # Светло-синий
image = np.full((N, N, 3), background_color)

# Считывание граней и вершин в массивы
with open(file_path, 'r') as file:
    for line in file:
        if not line:
            continue
        if line.startswith('v '):
            data = line.split()
            vertices.append((float(data[1]), float(data[2])))
        elif line.startswith('f '):
            data = line.split()
            edges.append((int(data[1]), int(data[2]), int(data[3])))

# Масштабные коэффициенты для X и Y
ratio = (M / (max(y for x, y in vertices) - min(y for x, y in vertices))) / (N / (max(x for x, y in vertices) - min(x for x, y in vertices)))
scale_x = N / (max(x for x, y in vertices) - min(x for x, y in vertices)) / ratio
scale_y = M / (max(y for x, y in vertices) - min(y for x, y in vertices)) / ratio

#minx = min(x for x, y in vertices)
#miny = min(y for x, y in vertices)
#vector = np.array([N // 2 - math.sqrt(N // 2), N // 2 - N // 2 // 8])
# Отмасштабированные значения вершин с инвертированной координатой Y
# Вычитаем minX и minY для корректировки координат и начала с (0,0)
# Координата Y вычитается из N для адаптации
# Создание матрицы масштабирования
scaling_matrix = np.array([[scale_x, 0], [0, scale_y]]) # матрица масштабирования
vector = np.array([N // 2, N // 2]) # смещение на вектор
scaled_vertices = [scaling_matrix @ vertice + vector for vertice in vertices]
scaled_vertices = [(int(x), int(y)) for x, y in scaled_vertices]
print(scaled_vertices)



# Проверка и коррекция координат, чтобы они не выходили за пределы изображения
for i in range(len(scaled_vertices)):
    x, y = scaled_vertices[i]
    if x >= N:
        x = N - 1
    if y >= N:
        y = N - 1
    scaled_vertices[i] = (x, y)



# Определение координат левой и правой границы модели
left_x = min(vertex[0] for vertex in scaled_vertices)
right_x = max(vertex[0] for vertex in scaled_vertices)

# Проходимся по списку граней и отрисуем их
for edge in edges:
    vertices_to_draw = [scaled_vertices[edge[0] - 1], scaled_vertices[edge[1] - 1], scaled_vertices[edge[2] - 1]]
    draw_triangle(image, vertices_to_draw, left_x, right_x)


plt.figure(figsize=(8, 8), dpi=80)
plt.imshow(image)
plt.axis('off')
plt.tight_layout(pad=0)
plt.savefig("img.png")
plt.show()

