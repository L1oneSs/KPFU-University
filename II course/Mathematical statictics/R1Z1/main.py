import math
from typing import List, Any
import matplotlib.pyplot as plt
import numpy as np
import openpyxl
from statsmodels.distributions.empirical_distribution import ECDF
import matplotlib as mpl

data: list[Any] = []
pointsX: list[Any] = []
pointsY: list[Any] = []
min = 0
max = 0
scope = 0
sum = 0
middle = 0
sum_of_one = 0
sum_of_two = 0
sum_of_three = 0
dispersion_s = 0
dispersion_non_s = 0
standart_deviation = 0
asymmetry = 0
k_excess = 0
median = 0
interq_width_one = 0
interq_width_two = 0
interq_width = 0
interval = 0


def main():
    Excel_Reader()
    Sample_Charasteristics()
    Empirical_Distribution(data)

def Excel_Reader():
    book = openpyxl.open("r1z1.xlsx", read_only = "True")
    sheet = book.active
    for i in range(2, 114):
        data.append(sheet[i][0].value)
        print(sheet[i][0].value)


def Sample_Charasteristics():
    global sum, sum_of_one, sum_of_two, sum_of_three
    sample_size = len(data)
    print("Объем выборки: " + str(sample_size))     # Объем выборки

    min = data[0]
    for i in range(0, len(data)):               # Минимум
        if min > data[i]:
            min = data[i]
    print("Минимум: " + str(min))

    max = data[0]
    for i in range(0, len(data)):               # Максимум
        if max < data[i]:
            max = data[i]
    print("Максимум: " + str(max))

    scope = max - min                           # Размах
    print("Размах: " + str(scope))

    for i in range(0, len(data)):               # Среднее
        sum = sum + data[i]
    middle = sum / len(data)
    print("Среднее: " + str(middle))

    for i in range(0, len(data)):               # (Не)смещенная дисперсия
        sum_of_one = sum_of_one + (data[i] - middle) * (data[i] - middle)
    dispersion_s = sum_of_one / len(data)
    dispersion_non_s = sum_of_one / (len(data) - 1)
    print("Выборочная смещенная дисперсия: " + str(dispersion_s))
    print("Выборочная несмещенная дисперсия: " + str(dispersion_non_s))

    standart_deviation = math.sqrt(dispersion_s)    # Стандартное отклонение
    print("Стандартное отклонение: " + str(standart_deviation))

    for i in range(0, len(data)):                   # Коэффициент асимметрии
        sum_of_two = sum_of_two + (data[i] - middle)**3
    asymmetry = (sum_of_two / sample_size) / standart_deviation**3
    print("Коэффициент асимметрии: " + str(asymmetry))

    for i in range(0, len(data)):                   # Коэффициент эксцесса
        sum_of_three = sum_of_three + (data[i] - middle)**4
    k_excess = ((sum_of_three / sample_size) / standart_deviation**4) - 3
    print("Коэффициент эксцесса: " + str(k_excess))

    data2 = []
    for i in range(0, len(data)):
        data2.append(data[i])

    data2 = sorted(data2)

    if (sample_size - 1) / 2 + 1 == round((sample_size - 1) / 2 + 1):   # Медиана
        median = data2[int((sample_size - 1) / 2 + 1)]
    else:
        median = (data2[int(round((sample_size - 1) / 2) + 1)] + data2[int(round((sample_size - 1) / 2) + 2)]) / 2
    print("Медиана: " + str(median))
    '''
    if sample_size % 2 == 0:
        print("Медиана: " + str((data2[sample_size//2 - 1] + data2[sample_size//2])/2))
    else:
        print("Медиана: " + str(data2[sample_size // 2]))
    '''
    print(data2[55])
    print(data2[56])
    #   Интерквартильная широта

    if (sample_size - 1)*(3 / 4) == round((sample_size - 1)*(3 / 4)):
        interq_width_one = data2[int((sample_size - 1)*(3 / 4) + 1)]
    else:
        interq_width_one = (data2[int(round((sample_size - 1)*(3 / 4)) + 1)] + data2[int(round((sample_size - 1) * (3 / 4)) + 2)]) / 2
    if (sample_size - 1) / 4 == round((sample_size - 1) / 4):
        interq_width_two = data2[int((sample_size - 1) / 4 + 1)]
    else:
        interq_width_two = (data2[int(round((sample_size - 1) / 4) + 1)] + data2[int(round((sample_size - 1) / 4) + 2)]) / 2
    interq_width = interq_width_one - interq_width_two
    print("Интерквартильная широта: ", interq_width)
    Histogram(standart_deviation, middle, dispersion_s, data, min, max, scope)


def Histogram(standart_deviation, middle, dispersion_s, data, min, max, scope):
    sample_size = len(data)
    data2 = sorted(data)

    #   нормальное распределение
    points_notmal = []
    for i in range(0, len(data2)):
        points_notmal.append(
            (1 / (standart_deviation * math.sqrt(2 * math.pi))) * math.exp(-((data2[i] - middle) * (data2[i] - middle) / (2 * dispersion_s))))
    #   нормальное распределение

    intervals = round(sample_size / 10)
    a = []
    delt = scope / (intervals - 1)
    a.append(100)   # Минимальная граница a0
    a.append(min + delt / 2)  # a1
    for i in range(1, intervals - 1):
        a.append(a[i] + delt)
    a.append(max - delt / 2)  # a(k-1)
    a.append(140)   # Максимальная граница ak

    h = []  # Высоты
    sum = 0
    for j in range(1, len(a)):
        for i in range(0, len(data)):
            if data[i] >= a[j - 1] and data[i] < a[j]:
                sum += 1
        h.append(sum / (sample_size * (a[j] - a[j - 1])))
        sum = 0
    plt.plot(data2, points_notmal)
    plt.stairs(h, a, fill=True)
    plt.show()

def Empirical_Distribution(data):
    data2 = sorted(data)
    sample_size = len(data)
    F = []
    sum = 0
    for i in range(0, len(data2)):
        for j in range(0, len(data2)):
            if data2[j] < data2[i]:
                sum += 1
        F.append(sum / sample_size)
        sum = 0
    plt.plot(data2, F, color="red")
    plt.show()


    ecdf = ECDF(data)
    plt.step(ecdf.x, ecdf.y)
    plt.show()
    





if __name__ == "__main__":
    main()



