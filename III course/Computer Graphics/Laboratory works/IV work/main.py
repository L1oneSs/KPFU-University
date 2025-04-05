import numpy as np
from drawer import draw_curve
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter, FuncAnimation

width = 1200
height = 910
coords_1 = []
coords_2 = []
coords_3 = []
coords_4 = []
background_color = np.array([1.0, 1.0, 1.0])
image = np.full((height, width, 3), background_color)

Curve_1 = [(600, 451), (375, 295), (350, 451)]
Curve_2 = [(350, 451), (375, height - 295), (600, 451)]
Curve_3 = [(600, 451), (width - 375, 295), (width - 350, 451)]
Curve_4 = [(width - 350, 451), (width - 375, height - 295), (600, 451)]

izgib_1 = [375, 295]
izgib_2 = [375, height - 295]
izgib_3 = [width - 375, 295]
izgib_4 = [width - 375, height - 295]

draw_curve(image, Curve_1, coords_1)
draw_curve(image, Curve_2, coords_2)
draw_curve(image, Curve_3, coords_3)
draw_curve(image, Curve_4, coords_4)

Left_point_X = [350, 451]
Center_point_X = [600, 451]
Right_point_X = [width - 350, 451]
Top_point_Y = min(y for x, y in coords_1)
Bottom_point_Y = max(y for x, y in coords_2)
M = np.abs((Left_point_X[0] - Center_point_X[0]))
T = np.abs((Top_point_Y - Bottom_point_Y))

fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)



def update(frame):
    global coords_1, coords_2, coords_3, coords_4, image
    image = np.full((height, width, 3), background_color)

    if frame <= 30:
        print(frame)
        move_X = (1.5 * M) // 30
        move_Y = T // 30
        coords_1 = [(coord[0] - move_X, coord[1] + move_Y) for coord in coords_1]
        coords_2 = [(coord[0] - move_X, coord[1] - move_Y) for coord in coords_2]
        coords_3 = [(coord[0] + move_X, coord[1] + move_Y) for coord in coords_3]
        coords_4 = [(coord[0] + move_X, coord[1] - move_Y) for coord in coords_4]
        Left_point_X[0] -= move_X
        Right_point_X[0] += move_X
        izgib_1[0] -= move_X
        izgib_2[0] -= move_X
        izgib_3[0] += move_X
        izgib_4[0] += move_X
        izgib_1[1] += move_Y
        izgib_2[1] -= move_Y
        izgib_3[1] += move_Y
        izgib_4[1] -= move_Y

    if frame > 30:
        print(frame)
        move_X = (1.5 * M) // 20
        move_Y = T // 20
        coords_1 = [(coord[0] + move_X, coord[1] - move_Y) for coord in coords_1]
        coords_2 = [(coord[0] + move_X, coord[1] + move_Y) for coord in coords_2]
        coords_3 = [(coord[0] - move_X, coord[1] - move_Y) for coord in coords_3]
        coords_4 = [(coord[0] - move_X, coord[1] + move_Y) for coord in coords_4]
        Left_point_X[0] += move_X
        Right_point_X[0] -= move_X
        izgib_1[0] += move_X
        izgib_2[0] += move_X
        izgib_3[0] -= move_X
        izgib_4[0] -= move_X
        izgib_1[1] -= move_Y
        izgib_2[1] += move_Y
        izgib_3[1] -= move_Y
        izgib_4[1] += move_Y

    draw_curve(image, [Center_point_X, izgib_1, Left_point_X], None)
    draw_curve(image, [Center_point_X, izgib_2, Left_point_X], None)
    draw_curve(image, [Center_point_X, izgib_3, Right_point_X], None)
    draw_curve(image, [Center_point_X, izgib_4, Right_point_X], None)

    ax.imshow(image)
    ax.axis('off')
    plt.draw()

    plt.show()


animation_frames = 50
ani = FuncAnimation(fig, update, frames=animation_frames, repeat=False)

# Сохранение анимации в формате GIF
writer = PillowWriter(fps=10)
ani.save("infinity.gif", writer=writer)

plt.show()
