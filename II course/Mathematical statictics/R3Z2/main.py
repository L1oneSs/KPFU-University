import openpyxl
import math
from scipy.stats import t

valueX = []
Q = 0.975
middle_X = 0
sum = 0
sum_of_one = 0
m = 0
down_border = 0
up_border = 0
standart_diviation = 0

def main():
    Excel_Reader()
    Statistics()


def Excel_Reader():
    book = openpyxl.open("r3z2.xlsx", read_only="True")
    sheet = book.active
    for i in range(2, 56):
        valueX.append(sheet["A" + str(i)].value)

def Statistics():
    global sum, sum_of_one
    print("Объем выборки: " + str(len(valueX)))

    for i in range(0, len(valueX)):  # Среднее
        sum = sum + valueX[i]
    middle_X = sum / len(valueX)
    print("Выборочное среднее: " + str(middle_X))

    for i in range(0, len(valueX)):               # Выборочная дисперсия
        sum_of_one = sum_of_one + (valueX[i] - middle_X) * (valueX[i] - middle_X)
    dispersion_s = sum_of_one / len(valueX)
    #dispersion_non_s = sum_of_one / (len(valueX) - 1)
    #print("Выборочная дисперсия: " + str(dispersion_s))
    #print("Выборочная несмещенная дисперсия: " + str(dispersion_non_s))
    standart_diviation = math.sqrt(dispersion_s)
    print("Стандартное отклонение: " + str(standart_diviation))

    # Стандартная ошибка среднего
    m = standart_diviation / (math.sqrt(len(valueX) - 1))
    print("Стандартная ошибка среднего: " + str(m))

    alpha = 1 - Q
    down_border = middle_X - (standart_diviation * t.ppf(1 - alpha/2, len(valueX) - 1)
                              / math.sqrt(len(valueX) - 1))
    up_border = middle_X + (standart_diviation * t.ppf(1 - alpha/2, len(valueX) - 1)
                              / math.sqrt(len(valueX) - 1))


    print("Доверительный интервал: " + str("(") + str(down_border) + " , "
          + str(up_border) + ")")

if __name__ == "__main__":
    main()

