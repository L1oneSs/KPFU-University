import openpyxl
import math
import numpy as np
from scipy.stats import f

valueX = []
valueY = []
dispersion_x = 0
dispersion_y = 0
dispersion_s_x = 0
dispersion_s_y = 0
dispersion_nons_x = 0
dispersion_nons_y = 0
sum_x = 0
sum_y = 0
sum_of_one_x = 0
sum_of_one_y = 0
alpha = 0.01
F = 0
middle_x = 0
middle_y = 0




def main():
    Excel_Reader()
    Values()

def Excel_Reader():
    book = openpyxl.open("r2z1.xlsx", read_only="True")
    sheet = book.active
    for i in range(2, 61):
        valueX.append(sheet["A" + str(i)].value)
    for i in range(2, 56):
        valueY.append(sheet["B" + str(i)].value)

    print(valueX)
    print(valueY)

def Values():
    global sum_x, sum_y, sum_of_one_x, sum_of_one_y
    for i in range(0, len(valueX)):               # Среднее X
        sum_x = sum_x + valueX[i]
    middle_x = sum_x / len(valueX)
    print("Среднее X: " + str(middle_x))

    for i in range(0, len(valueY)):               # Среднее Y
        sum_y = sum_y + valueY[i]
    middle_y = sum_y / len(valueY)
    print("Среднее Y: " + str(middle_y))

    for i in range(0, len(valueX)):
        sum_of_one_x = sum_of_one_x + (valueX[i] - middle_x) * (valueX[i] - middle_x)
    for i in range(0, len(valueY)):
        sum_of_one_y = sum_of_one_y + (valueY[i] - middle_y) * (valueY[i] - middle_y)
    dispersion_s_x = sum_of_one_x / len(valueX) # Смещенная дисперсия X
    dispersion_s_y = sum_of_one_y / len(valueY) # Смещенная дисперсия Y
    dispersion_nons_x = sum_of_one_x / (len(valueX) - 1) # Несмещенная дисперсия X
    dispersion_nons_y = sum_of_one_y / (len(valueY) - 1) # Несмещенная дисперсия Y
    print("Выборочная смещенная дисперсия X: " + str(dispersion_s_x))
    print("Выборочная смещенная дисперсия Y: " + str(dispersion_s_y))
    print("Выборочная несмещенная дисперсия X: " + str(dispersion_nons_x))
    print("Выборочная несмещенная дисперсия Y: " + str(dispersion_nons_y))
    # Тестовая статистика
    F = dispersion_nons_x / dispersion_nons_y
    print("Тестовая статистика критерия Фишера: " + str(F))
    # Вид критической области
    print("Вид критической облати: Правосторонняя(сигма 1-ой гр. Больше)")
    # Вычисление С(крит)
    #N = len(valueX) + len(valueY)
    k = len(valueX) - 1
    m = len(valueY) - 1
    #m = N - k
    print(k)
    print(m)
    f_crit = f.ppf(1-alpha,k,m)
    p_value = 1 - f.cdf(F,k,m)
    print("Критическая константа: " + str(f_crit))
    print("p-value: " + str(p_value))

    if F > f_crit:
        print("Принимается альтернативная гипотеза")
    else:
        print("Принимается нулевая гипотеза")

    if p_value < alpha:
        print("Принимается альтернативная гипотеза")
    else:
        print("Принимается нулевая гипотеза")

"""Имеется две группы студентов: первая группа, которая учится по стандартной
программе, и вторая группа, которая учится по новой методике. Необходимо
определить, улучшила ли новая методика обучения успеваемость студентов по сравнению
со стандартной программой. Для этого используется правосторонний критерий Фишера, 
согласно которому нулевая гипотеза заключается в том, что новая методика обучения 
не приводит к улучшению успеваемости, а альтернативная гипотеза заключается в том, 
что новая методика обучения приводит к улучшению успеваемости.
"""

if __name__ == "__main__":
    main()