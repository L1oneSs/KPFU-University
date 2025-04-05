import numpy as np
import matplotlib.pyplot as plt
from drawer import draw_curve, paint_cat
from matplotlib.animation import PillowWriter, FuncAnimation

width = 766
height = 980
body_coords = []
tail_coords = []
eye1_coords = []
eye2_coords = []
pupil1_coords = []
pupil2_coords = []
background_color = np.array([0.5, 0.5, 1.0])  # Светло-синий
image = np.full((height, width, 3), background_color)
CST = 100
# Body
Curve1 = [(260 - CST, 119), (190 - CST, 31), (110 - CST, 0)]
Curve2 = [(110 - CST, 0), (155 - CST, 116), (166 - CST, 182)]

curves = [Curve1, Curve2]

for curve in curves:
    draw_curve(image, curve, body_coords)

# Body
Curve1 = [(166 - CST, 182), (153 - CST, 196), (154 - CST, 197)]
Curve2 = [(154 - CST, 197), (141 - CST, 219), (142 - CST, 220)]
Curve3 = [(142 - CST, 220), (136 - CST, 238), (136 - CST, 241)]
Curve4 = [(136 - CST, 241), (133 - CST, 259), (133 - CST, 260)]
Curve5 = [(133 - CST, 260), (135 - CST, 284), (137 - CST, 288)]
Curve6 = [(137 - CST, 288), (145 - CST, 316), (150 - CST, 320)]
Curve7 = [(150 - CST, 320), (172 - CST, 349), (173 - CST, 348)]
Curve8 = [(173 - CST, 348), (222 - CST, 382), (223 - CST, 379)]
Curve9 = [(223 - CST, 379), (253 - CST, 392), (259 - CST, 393)]

curves = [Curve1, Curve2, Curve3, Curve4, Curve5, Curve6, Curve7, Curve8, Curve9]

for curve in curves:
    draw_curve(image, curve, body_coords)

# Body
Curve1 = [(259 - CST, 393), (259 - CST, 393), (301 - CST, 392), (310 - CST, 429)]
Curve2 = [(310 - CST, 429), (318 - CST, 448), (271 - CST, 477), (235 - CST, 503)]
Curve3 = [(235 - CST, 503), (230 - CST, 565), (223 - CST, 631), (232 - CST, 653)]
Curve4 = [(232 - CST, 653), (230 - CST, 664), (212 - CST, 655), (180 - CST, 660)]
Curve5 = [(180 - CST, 660), (143 - CST, 677), (87 - CST, 730), (143 - CST, 834)]
Curve6 = [(143 - CST, 834), (186 - CST, 897), (221 - CST, 901)]
Curve7 = [(221 - CST, 901), (225 - CST, 913), (215 - CST, 912)]
Curve8 = [(215 - CST, 912), (187 - CST, 907), (172 - CST, 926)]
Curve9 = [(172 - CST, 926), (330 - CST, 927)]

curves = [Curve1, Curve2, Curve3, Curve4, Curve5, Curve6, Curve7, Curve8, Curve9]
for curve in curves:
    draw_curve(image, curve, body_coords)

###########################################################
# Body
CONST = 110
Curve1 = [(-260 - CONST - CST, 119), (-190 - CONST - CST, 31), (-110 - CONST - CST, 0)]
Curve2 = [(-110 - CONST - CST, 0), (-155 - CONST - CST, 116), (-166 - CONST - CST, 182)]

curves = [Curve1, Curve2]

for curve in curves:
    draw_curve(image, curve, body_coords)

# Body
Curve1 = [(-166 - CONST - CST, 182), (-153 - CONST - CST, 196), (-154 - CONST - CST, 197)]
Curve2 = [(-154 - CONST - CST, 197), (-141 - CONST - CST, 219), (-142 - CONST - CST, 220)]
Curve3 = [(-142 - CONST - CST, 220), (-136 - CONST - CST, 238), (-136 - CONST - CST, 241)]
Curve4 = [(-136 - CONST - CST, 241), (-133 - CONST - CST, 259), (-133 - CONST - CST, 260)]
Curve5 = [(-133 - CONST - CST, 260), (-135 - CONST - CST, 284), (-137 - CONST - CST, 288)]
Curve6 = [(-137 - CONST - CST, 288), (-145 - CONST - CST, 316), (-150 - CONST - CST, 320)]
Curve7 = [(-150 - CONST - CST, 320), (-172 - CONST - CST, 349), (-173 - CONST - CST, 348)]
Curve8 = [(-173 - CONST - CST, 348), (-222 - CONST - CST, 382), (-223 - CONST - CST, 379)]
Curve9 = [(-223 - CONST - CST, 379), (-253 - CONST - CST, 392), (-259 - CONST - CST, 393)]

curves = [Curve1, Curve2, Curve3, Curve4, Curve5, Curve6, Curve7, Curve8, Curve9]

for curve in curves:
    draw_curve(image, curve, body_coords)

# Body
Curve1 = [(-259 - CONST - CST, 393), (-259 - CONST - CST, 393), (-301 - CONST - CST, 392), (-310 - CONST - CST, 429)]
Curve2 = [(-310 - CONST - CST, 429), (-318 - CONST - CST, 448), (-271 - CONST - CST, 477), (-235 - CONST - CST, 503)]
Curve3 = [(-235 - CONST - CST, 503), (-230 - CONST - CST, 565), (-223 - CONST - CST, 631), (-232 - CONST - CST, 653)]
Curve4 = [(-232 - CONST - CST, 653), (-230 - CONST - CST, 664), (-212 - CONST - CST, 655), (-180 - CONST - CST, 660)]
Curve5 = [(-180 - CONST - CST, 660), (-143 - CONST - CST, 677), (-87 - CONST - CST, 730), (-143 - CONST - CST, 834)]
Curve6 = [(-143 - CONST - CST, 834), (-186 - CONST - CST, 897), (-221 - CONST - CST, 901)]
Curve7 = [(-221 - CONST - CST, 901), (-225 - CONST - CST, 913), (-215 - CONST - CST, 912)]
Curve8 = [(-215 - CONST - CST, 912), (-187 - CONST - CST, 907), (-172 - CONST - CST, 926)]
Curve9 = [(-172 - CONST - CST, 926), (-330 - CONST - CST, 927)]

curves = [Curve1, Curve2, Curve3, Curve4, Curve5, Curve6, Curve7, Curve8, Curve9]

for curve in curves:
    draw_curve(image, curve, body_coords)

# Top Head
Curve_head_top = [(260 - CST, 119), (338 - CST, 97), (396 - CST, 120)]
draw_curve(image, Curve_head_top, body_coords)

# TAIL
Curve_tail_1 = [(470 - CST, 884), (656 - CST, 895), (666 - CST, 748)]
Curve_tail_2 = [(666 - CST, 748), (681 - CST, 690), (638 - CST, 597)]
Curve_tail_3 = [(638 - CST, 597), (541 - CST, 409), (670 - CST, 360)]
Curve_tail_4 = [(670 - CST, 360), (744 - CST, 347), (755 - CST, 427)]
Curve_tail_5 = [(755 - CST, 426), (762 - CST, 436), (763 - CST, 426)]
Curve_tail_6 = [(763 - CST, 426), (760 - CST, 352), (696 - CST, 340)]
Curve_tail_7 = [(696 - CST, 340), (649 - CST, 328), (617 - CST, 365)]
Curve_tail_8 = [(617 - CST, 365), (566 - CST, 404), (575 - CST, 511)]
Curve_tail_9 = [(575 - CST, 511), (591 - CST, 583), (601 - CST, 602)]
Curve_tail_10 = [(601 - CST, 602), (640 - CST, 721), (623 - CST, 747)]
Curve_tail_11 = [(623 - CST, 747), (617 - CST, 820), (520 - CST, 826)]

Curve_tail = [Curve_tail_1, Curve_tail_2, Curve_tail_3, Curve_tail_4, Curve_tail_5, Curve_tail_6,
              Curve_tail_7, Curve_tail_8, Curve_tail_9, Curve_tail_10, Curve_tail_11]
for curve in Curve_tail:
    draw_curve(image, curve, tail_coords)

# EYES
Curve_eye1 = [(190 - CST, 203), (161 - CST, 218), (190 - CST, 278)]
Curve_eye2 = [(190 - CST, 278), (224 - CST, 328), (253 - CST, 319)]
Curve_eye3 = [(253 - CST, 319), (301 - CST, 319), (311 - CST, 269)]
Curve_eye4 = [(311 - CST, 269), (271 - CST, 196), (190 - CST, 203)]

Curve_eye = [Curve_eye1, Curve_eye2, Curve_eye3, Curve_eye4]
for curve in Curve_eye:
    draw_curve(image, curve, eye1_coords)

Curve_eye1 = [(-190 - CONST - CST, 203), (-161 - CONST - CST, 218), (-190 - CONST - CST, 278)]
Curve_eye2 = [(-190 - CONST - CST, 278), (-224 - CONST - CST, 328), (-253 - CONST - CST, 319)]
Curve_eye3 = [(-253 - CONST - CST, 319), (-301 - CONST - CST, 319), (-311 - CONST - CST, 269)]
Curve_eye4 = [(-311 - CONST - CST, 269), (-271 - CONST - CST, 196), (-190 - CONST - CST, 203)]

Curve_eye = [Curve_eye1, Curve_eye2, Curve_eye3, Curve_eye4]
for curve in Curve_eye:
    draw_curve(image, curve, eye2_coords)

# PUPILS
Curve_pupil_1 = [(246 - CST, 212), (219 - CST, 256), (249 - CST, 297)]
Curve_pupil_2 = [(249 - CST, 297), (280 - CST, 256), (246 - CST, 212)]
Curve_pupil = [Curve_pupil_1, Curve_pupil_2]
for curve in Curve_pupil:
    draw_curve(image, curve, pupil1_coords)

Curve_pupil_1 = [(-246 - CONST - CST, 212), (-219 - CONST - CST, 256), (-249 - CONST - CST, 297)]
Curve_pupil_2 = [(-249 - CONST - CST, 297), (-280 - CONST - CST, 256), (-246 - CONST - CST, 212)]
Curve_pupil = [Curve_pupil_1, Curve_pupil_2]
for curve in Curve_pupil:
    draw_curve(image, curve, pupil2_coords)

# DRAWING
paint_cat(image, 'body', [0, 0, 0], body_coords)
paint_cat(image, 'tail', [0, 0, 0], tail_coords)
paint_cat(image, 'eye_1', [1, 1, 0], eye1_coords)
paint_cat(image, 'eye_2', [1, 1, 0], eye2_coords)
paint_cat(image, 'pupil_1', [0, 0, 0], pupil1_coords)
paint_cat(image, 'pupil_2', [0, 0, 0], pupil2_coords)


def rotation_matrix(angle):
    angle_rad = np.radians(angle)
    return np.array([[np.cos(angle_rad), -np.sin(angle_rad)],
                     [np.sin(angle_rad), np.cos(angle_rad)]])


fig, ax = plt.subplots(figsize=(width / 100, height / 100), dpi=100)


def update(frame):
    global pupil1_coords, pupil2_coords, tail_coords, image, old_tail_coords, body_coords

    old_pupil1_coords = pupil1_coords.copy()
    old_pupil2_coords = pupil2_coords.copy()
    old_tail_coords = tail_coords.copy()

    step = np.array([1, -1])

    if frame < 8:
        pupil1_coords = [pupil - step for pupil in pupil1_coords]
        pupil2_coords = [pupil - step for pupil in pupil2_coords]
    elif 8 <= frame < 16:
        pupil1_coords = [pupil - (-1) * step for pupil in pupil1_coords]
        pupil2_coords = [pupil - (-1) * step for pupil in pupil2_coords]
    elif 16 <= frame < 24:
        pupil1_coords = [pupil + np.array([1, 1]) for pupil in pupil1_coords]
        pupil2_coords = [pupil + np.array([1, 1]) for pupil in pupil2_coords]
    elif 24 <= frame <= 32:
        pupil1_coords = [pupil + (-1) * step for pupil in pupil1_coords]
        pupil2_coords = [pupil + (-1) * step for pupil in pupil2_coords]

    pupil1_coords = [(int(x), int(y)) for x, y in pupil1_coords]
    pupil2_coords = [(int(x), int(y)) for x, y in pupil2_coords]

    tail_rotation_angle = 2  # Уменьшил угол поворота хвоста

    if frame < 16:
        rotation_matrix_left = rotation_matrix(-tail_rotation_angle)
        tail_coords = np.round(
            np.dot(tail_coords - np.mean(tail_coords, axis=0), rotation_matrix_left) + np.mean(tail_coords,
                                                                                               axis=0))

    elif 16 <= frame <= 32:
        rotation_matrix_right = rotation_matrix(tail_rotation_angle)
        tail_coords = np.round(
            np.dot(tail_coords - np.mean(tail_coords, axis=0), rotation_matrix_right) + np.mean(tail_coords,
                                                                                                axis=0))

    tail_coords = [(int(x), int(y)) for x, y in tail_coords]

    for coord in old_tail_coords:
        if 0 <= coord[0] < image.shape[1] and 0 <= coord[1] < image.shape[0]:
            image[coord[1], coord[0]] = [0.5, 0.5, 1.0]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= coord[0] + i < image.shape[1] and 0 <= coord[1] + j < image.shape[0]:
                        image[coord[1] + j, coord[0] + i] = [0.5, 0.5, 1.0]

    for coord in tail_coords:
        if 0 <= coord[0] < image.shape[1] and 0 <= coord[1] < image.shape[0]:
            image[coord[1], coord[0]] = [0, 0, 0]
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= coord[0] + i < image.shape[1] and 0 <= coord[1] + j < image.shape[0]:
                        image[coord[1] + j, coord[0] + i] = [0, 0, 0]

    for coord in old_pupil1_coords:
        image[coord[1], coord[0]] = [1, 1, 0]

    for coord in old_pupil2_coords:
        image[coord[1], coord[0]] = [1, 1, 0]

    for coord in pupil1_coords:
        image[coord[1], coord[0]] = [0, 0, 0]

    for coord in pupil2_coords:
        image[coord[1], coord[0]] = [0, 0, 0]

    for coord in body_coords:
        image[coord[1], coord[0]] = [0, 0, 0]

    ax.imshow(image)

    # Отключаем оси
    ax.axis('off')

    plt.draw()
    print("Кадр сделан")


animation_frames = 32
ani = FuncAnimation(fig, update, frames=animation_frames, repeat=False)

# Сохранение анимации в формате GIF
writer = PillowWriter(fps=32)
ani.save("cat.gif", writer=writer)

plt.show()
