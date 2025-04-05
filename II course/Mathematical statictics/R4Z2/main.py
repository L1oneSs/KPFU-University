import math

import numpy as np
import openpyxl
import seaborn as sns
import matplotlib.pyplot as plt

valueX = []
valueY = []
valueXY = []
valueX2 = []
valueY2 = []

sum_x = 0
sum_y = 0
sum_xy = 0
sum_x2 = 0
sum_y2 = 0

delta = 0

y = 79
x = 0
r = 0
middle_x = 0
middle_y = 0
dispersion_x = 0
dispersion_y = 0
standart_deviation_x = 0
standart_deviation_y = 0


def main():
    Excel_Reader()
    Regression_Equasion()

def Excel_Reader():
    book = openpyxl.open("r4z2.xlsx", read_only="True")
    sheet = book.active
    for i in range(2, 98):
        valueX.append(sheet[i][0].value)
        valueY.append(sheet["B" + str(i)].value)
        print(sheet[i][0].value)
    print("@@@@@@@@@@@@@@@")
    for i in range(2, 98):
        print(sheet["B" + str(i)].value)

def Graphics(a, b):
    points_y_regression = []
    for i in range(0, len(valueX)):
        points_y_regression.append(a * valueX[i] + b)
    plt.plot(valueX, points_y_regression)
    plt.scatter(valueX, valueY)
    plt.show()

def Regression_Equasion():
    global sum_x, sum_y, sum_xy, sum_x2, sum_y2
    sample_size = len(valueX)
    for i in range(0, len(valueX)):
        valueXY.append(valueX[i] * valueY[i])
        valueX2.append(valueX[i]**2)
        valueY2.append(valueY[i]**2)
    for i in range(0, len(valueX)):
        sum_x += valueX[i]
        sum_y += valueY[i]
        sum_xy += valueXY[i]
        sum_x2 += valueX2[i]
        sum_y2 += valueY2[i]

        # Решаем систему a * sum(x^2) + b * sum(x) = sum(x*y)
        #                a * sum(x) + b * n = sum(y)

    delta = sum_x2 * sample_size - sum_x * sum_x
    delta_a = sum_xy * sample_size - sum_y * sum_x
    delta_b = sum_x2 * sum_y - sum_x * sum_xy
    a = delta_a / delta
    b = delta_b / delta
    print("Уравнение регрессии: y = " + str(a) + "x" + " + " + str(b))

    #   Прогноз в заданной точке
    summary_x = 0
    for i in range(0, len(valueX)):               # Выборочное среднее для X
        summary_x = summary_x + valueX[i]
    middle_x = summary_x / len(valueX)
    print("Выборочное среднее для Х: " + str(middle_x))

    summary_y = 0
    for i in range(0, len(valueY)):               # Выборочное среднее для Y
        summary_y = summary_y + valueY[i]
    middle_y = summary_y / len(valueY)
    print("Выборочное среднее для У: " + str(middle_y))

    sum_of_one = 0
    for i in range(0, len(valueX)):               # Выборочная дисперсия для Х
        sum_of_one = sum_of_one + (valueX[i] - middle_x) * (valueX[i] - middle_x)
    dispersion_x = sum_of_one / len(valueX)
    print("Выборочная дисперсия для Х: " + str(dispersion_x))

    sum_of_two = 0
    for i in range(0, len(valueY)):               # Выборочная дисперсия для Х
        sum_of_two = sum_of_two + (valueY[i] - middle_y) * (valueY[i] - middle_y)
    dispersion_y = sum_of_two / len(valueY)
    print("Выборочная дисперсия для Y: " + str(dispersion_y))

    #   Выборочное стандартное отклонение для Х

    standart_deviation_x = math.sqrt(dispersion_x)
    print("Выборочное стандартное отклонение для Х: " + str(standart_deviation_x))

    #   Выборочное стандартное отклонение для У

    standart_deviation_y = math.sqrt(dispersion_y)
    print("Выборочное стандартное отклонение для Y: " + str(standart_deviation_y))

    #   Выборочный коэффициент корреляции
    sum_corr = 0
    for i in range(0, len(valueX)):
        sum_corr = sum_corr + (valueX[i] - middle_x) * (valueY[i] - middle_y)
    r = (sum_corr / sample_size) / (standart_deviation_x * standart_deviation_y)
    print("Выборочный коэффициент корреляции: " + str(r))

    x = middle_x + r * (standart_deviation_x / standart_deviation_y) * (79 - middle_y)

    print("Прогноз регрессии при заданном значении Y = 79: " + str(x))

    Graphics(a,b)

if __name__ == "__main__":
    main()