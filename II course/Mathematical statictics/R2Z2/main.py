import openpyxl
import matplotlib.pyplot as plt
import math
import numpy as np
from scipy.stats import expon
from scipy.stats import ks_2samp
from scipy.stats import kstwobign
from scipy.stats import kstest
from scipy.stats import kstwo
from scipy.special import smirnov


valueX = []
value_graphics_y = []
alpha = 0.1
lam = 1.5
T = []
supremum_values = []
D = 0
supremum = 0


def main():
    Excel_Reader()
    Graphics()
    Values()

def Excel_Reader():
    book = openpyxl.open("r2z2.xlsx", read_only="True")
    sheet = book.active
    for i in range(2, 76):
        valueX.append(sheet["A" + str(i)].value)

# Функция нахождения значений ЭФР
def ECDF(x):
    sum = 0
    valueX_sorted = sorted(valueX)
    for i in range(1, len(valueX)):
        if valueX_sorted[i] < x:
            sum += 1
    return 1 / len(valueX) * sum

def Graphics():
    # Вычисление значений ЭФР
    ecdf = []
    valueX_sorted = sorted(valueX)
    # ЭФР: значение = номер элемента / общее количество элементов.
    #ecdf = [i / len(valueX) for i in range(1, len(valueX) + 1)]
    for i in range(0, len(valueX_sorted)):
        ecdf.append(ECDF(valueX_sorted[i]))
    print(valueX_sorted)
    plt.step(valueX_sorted, ecdf, label='Empirical CDF')

    # Предполагаемая функция распределения

    for i in range(0, len(valueX_sorted)):
        value_graphics_y.append(expon.cdf(valueX_sorted[i], scale=1/lam))
    print(value_graphics_y)

    # Вывод графика

    plt.plot(valueX_sorted, value_graphics_y, label='Normal Distribution')

    # Настройка графика
    plt.xlabel('Value')
    plt.ylabel('Probability')
    plt.title('Empirical CDF and EXP Distribution')
    plt.legend(loc='best')
    plt.show()

def Values():
    valueX_sorted = sorted(valueX)
    for i in range(0, len(valueX_sorted)):
        supremum_values.append(abs(ECDF(valueX_sorted[i]) - (expon.cdf(valueX_sorted[i], scale=1/lam))))
    supremum = max(supremum_values)
    print("@@@@@@@")
    print(supremum_values)
    # Статистика
    D = supremum * math.sqrt(len(valueX))
    print("Статистика: " + str(D))

    # Критическая константа
    c_crit_3 = kstwo.ppf(1 - alpha/2, len(valueX))
    print("Критическая константа: " + str(c_crit_3))

    # p-значение
    p_value_2 = 1 - smirnov(len(valueX), D)
    print("p-value: " + str(p_value_2))

    if math.sqrt(len(valueX)) * D > math.sqrt(-0.5 * math.log10(alpha/2)):
        print("Нулевая гипотеза отклоняется")
    else:
        print("Нулевая гипотеза принимается")

if __name__ == "__main__":
    main()