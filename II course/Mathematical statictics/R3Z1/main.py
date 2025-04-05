import openpyxl

valueX = []
sigma = 0
summ = 0

def main():
    Excel_Reader()
    Statistics()


def Excel_Reader():
    book = openpyxl.open("r3z1.xlsx", read_only="True")
    sheet = book.active
    for i in range(2, 38):
        valueX.append(sheet["A" + str(i)].value)

def Statistics():
    global summ
    for i in range(0, len(valueX)):
        summ = summ + abs(valueX[i])
    sigma = summ / len(valueX)
    print("Значение оценки: " + str(sigma))

if __name__ == "__main__":
    main()