import random
import sys
import math
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
import numpy as np
import logging
from math import sqrt  
from decimal import Decimal

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)

class SievingThread(QThread):
    update_signal = pyqtSignal(str)
    complete_signal = pyqtSignal(dict, list)

    def __init__(self, y_values, b, additional_value, n):
        super().__init__()
        self.y_values = np.array(y_values, dtype=object) 
        self.b = b
        self.additional_value = additional_value
        self.n = n
        self.smooth_numbers = {}
        self.block_size = 1000
        self.primes = self._init_prime_cache()

    def _init_prime_cache(self):
        """
            Шаг 1: [T,T,T,T,T,T,T,T,T,T,T] - исходный массив
            Шаг 2: [F,F,T,T,T,T,T,T,T,T,T] - убрали 0,1
            Шаг 3: [F,F,T,T,F,T,F,T,F,T,F] - вычеркнули кратные 2 (4,6,8,10)
            Шаг 4: [F,F,T,T,F,T,F,T,F,T,F] - вычеркнули кратные 3 (6,9)
            Результат: простые числа - [2,3,5,7]
        """
        # Создаем булев массив, изначально все числа считаются простыми
        sieve = np.ones(self.b + 1, dtype=bool)
        
        # 0 и 1 не являются простыми числами
        sieve[0] = sieve[1] = False
        
        # Реализация решета Эратосфена:
        # Для каждого простого числа i отмечаем все его кратные как составные
        for i in range(2, int(np.sqrt(self.b)) + 1):
            if sieve[i]:  # если i - простое
                # Отмечаем все кратные i как составные
                # i*i::i означает: начать с i², шаг i
                sieve[i*i::i] = False
        
        # Возвращаем индексы True значений - это и есть простые числа
        return np.nonzero(sieve)[0]
    
    # def calculate_y_values(self):
    #     # Вычисляем корень из n - начальное значение для x
    #     sqrt_n = int(math.sqrt(self.n))
    #     new_values = []
        
    #     # Для каждого значения из текущего набора y_values
    #     for i in range(len(self.y_values)):
    #         # Вычисляем x = sqrt(n) + 1 + i
    #         x = sqrt_n + 1 + i
    #         # Считаем (x + additional_value)² - n
    #         # Это формирует последовательность чисел для просеивания
    #         result = (x + self.additional_value) * (x + self.additional_value) - self.n
    #         new_values.append(result)
        
    #     # Возвращаем массив numpy с типом object для больших чисел
    #     return np.array(new_values, dtype=object)
        
    def is_prime(self, num):
        # Числа меньше 2 не являются простыми
        if num < 2:
            return False
            
        # Проверяем делители до корня из числа
        # Оптимизация: достаточно проверить до sqrt(num)
        for i in range(2, int(math.sqrt(num)) + 1):
            # Если нашли делитель - число составное
            if num % i == 0:
                return False
                
        # Если делителей не нашли - число простое
        return True
    
    def mod_exp(base: int, exp: int, mod: int) -> int:
        """
        Быстрое возведение в степень по модулю.
        base - основание
        exp - показатель степени 
        mod - модуль
        """
        # Особый случай - при модуле 1 всегда получаем 0
        # Любое число по модулю 1 всегда дает 0
        if mod == 1:
            return 0
        
        # Начальное значение результата
        result = 1
        # Приводим базу по модулю для оптимизации
        base = base % mod
        
        # Пока показатель степени не станет равным 0
        while exp > 0:
            # Если текущий бит показателя равен 1
            # (проверяем с помощью побитового И)
            if exp & 1:
                # Умножаем результат на текущую базу
                result = (result * base) % mod
                
            # Возводим базу в квадрат для следующей итерации
            base = (base * base) % mod
            # Сдвигаем показатель вправо (делим на 2)
            exp >>= 1
            
        return result

    def miller_rabin(self, n, k=120):
        """
        Тест Миллера-Рабина на простоту числа.
        Вероятностный тест - может ошибаться с вероятностью не более 4^(-k)
        
        Args:
            n: Тестируемое число
            k: Количество раундов тестирования (больше k = выше точность)
            
        Returns:
            bool: True если число вероятно простое, False если составное
        """
        # Проверяем базовые случаи
        if n == 2:  # 2 - простое число
            return True
        if not n & 1 or n < 2:  # Четные числа кроме 2 и числа < 2 не простые
            return False

        # Представляем n-1 в виде d * 2^s, где d нечетное
        s = 0  # Степень двойки
        d = n - 1  # Нечетный множитель
        while not d & 1:  # Пока d четное
            s += 1
            d >>= 1  # Делим d на 2

        # Проводим k раундов тестирования
        for _ in range(k):
            # Выбираем случайное a из [2, n-2]
            a = random.randrange(2, n - 1)
            
            # Вычисляем x = a^d mod n
            x = self.mod_exp(a, d, n)
            
            # Если x = 1 или x = n-1, этот раунд пройден
            if x == 1 or x == n - 1:
                continue
                
            # Возводим x в квадрат s-1 раз
            for _ in range(s - 1):
                x = self.mod_exp(x, 2, n)
                # Если получили -1, раунд пройден
                if x == n - 1:
                    break
            # Если не нашли -1, число составное    
            else:
                return False
                
        # Если все тесты пройдены, число вероятно простое        
        return True

    def get_prime_factors(self, num, b):
        # Словарь для хранения простых множителей и их степеней
        factors = {}
        # Берем модуль числа для работы с положительными значениями
        temp_num = abs(num)
        
        # Перебираем возможные делители до границы b
        for p in range(2, b + 1):
            # Пропускаем составные числа
            if not self.is_prime(p):
                continue
            
            # Считаем, сколько раз число делится на p
            count = 0
            while temp_num % p == 0:
                temp_num //= p  # Делим на простой множитель
                count += 1      # Увеличиваем степень
                
            # Если число делилось на p, добавляем в словарь
            if count > 0:
                factors[p] = count
        
        # Возвращаем факторы только если число полностью разложилось
        # Иначе возвращаем None (число не является B-гладким)
        return factors if temp_num == 1 else None

    def run(self):
        # Хранение истории всех операций
        full_history = ""
        # Указатель на текущий блок
        block_start = 0
        
        while True:
            # Начало HTML вывода для текущего блока
            html_output = "<div style='font-family: monospace;'>"
            
            # Определяем границы текущего блока
            block_end = min(block_start + self.block_size, len(self.y_values))
            # Преобразуем числа блока в целые
            current_block = [int(x) for x in self.y_values[block_start:block_end]]
            # Сохраняем оригинальные значения для факторизации
            original_values = current_block.copy()
            
            # Выводим исходные значения блока
            html_output += "Исходные значения:<br>"
            html_output += self._print_numbers(current_block)
            html_output += "<br><br>"
            
            # Просеивание простыми числами из факторной базы
            for prime in self.primes:
                if prime > self.b:  # Проверка границы простого числа
                    break
                    
                changed = True  # Флаг изменений при делении
                iteration = 1   # Счетчик итераций деления
                while changed:
                    changed = False
                    temp_block = current_block.copy()
                                                                                                                             
                    # Деление чисел на текущее простое
                    for i in range(len(current_block)):
                        if current_block[i] % prime == 0:  # Если делится
                            temp_block[i] //= prime        # Делим
                            changed = True                 # Отмечаем изменение
                    
                    # Если были деления, обновляем блок и показываем результат
                    if changed:
                        html_output += f"Деление на {prime} (итерация {iteration}):<br>"
                        html_output += self._print_numbers(temp_block)
                        html_output += "<br><br>"
                        current_block = temp_block.copy()
                        iteration += 1
            
            # Поиск B-гладких чисел (равных 1 после всех делений)
            found_smooth = False
            for i, num in enumerate(current_block):
                if num == 1:  # Если число стало равным 1, оно B-гладкое
                    global_idx = block_start + i
                    # Получение разложения на простые множители
                    factors = self.get_prime_factors(original_values[i], self.b)
                    if factors:
                        self.smooth_numbers[global_idx] = factors
                        found_smooth = True
            
            # Если нашли B-гладкие числа, формируем вывод и завершаем
            if found_smooth:
                full_history += html_output
                full_history += "<br><b>Найдены B-гладкие числа!</b><br>"
                for idx, factors in self.smooth_numbers.items():
                    factorization = " * ".join([f"{p}^{e}" for p, e in factors.items()])
                    full_history += f"<br>{int(self.y_values[idx])} = {factorization}<br>"
                
                self.update_signal.emit(full_history)
                y_values_list = [int(x) for x in self.y_values]
                self.complete_signal.emit(self.smooth_numbers, y_values_list)
                break
            
            # Если B-гладкие не найдены, переходим к следующему блоку
            block_start += self.block_size
            if block_start >= len(self.y_values):
                # Если просмотрели все блоки, увеличиваем параметры
                self.b = int(self.b * 1.5)
                self.additional_value += 1
                self.primes = self._init_prime_cache()
                
                # Пересчитываем значения с новыми параметрами
                sqrt_n = int(math.sqrt(self.n))
                new_values = []
                for i in range(len(self.y_values)):
                    x = sqrt_n + 1 + i
                    result = (x + self.additional_value) * (x + self.additional_value) - self.n
                    new_values.append(result)
                
                self.y_values = np.array(new_values, dtype=object)
                block_start = 0
                
                full_history += f"<br><b>B-гладкие числа не найдены. B={self.b}</b><br><hr>"
            
            # Обновляем вывод
            self.update_signal.emit(full_history)

    def _print_numbers(self, numbers):
        numbers_in_row = 0
        output = ""
        for num in numbers:
            if num == 1 or num == -1:
                output += f"<span style='color: red; font-weight: bold'>{num:>8}</span>"
            else:
                output += f"{num:>8}"
            numbers_in_row += 1
            if numbers_in_row == 5:
                output += "<br>"
                numbers_in_row = 0
            else:
                output += "&nbsp;&nbsp;"
        return output
    

class MatrixSolver(QThread):
    matrix_update = pyqtSignal(str)
    solution_found = pyqtSignal(list)
    no_solutions = pyqtSignal()

    def __init__(self, smooth_numbers, primes):
        super().__init__()
        self.smooth_numbers = smooth_numbers
        self.primes = primes

    def build_matrix_A(self):
        # Создаем пустую матрицу
        matrix = []
        
        # Для каждого B-гладкого числа и его разложения
        for idx, factors in self.smooth_numbers.items():
            # Создаем новую строку
            row = []
            # Для каждого простого числа из факторной базы
            for prime in self.primes:
                # Добавляем степень простого числа (0 если не входит в разложение)
                row.append(factors.get(prime, 0))
            # Добавляем строку в матрицу
            matrix.append(row)
        return matrix

    def mod2_matrix(self, matrix):
        return [[x % 2 for x in row] for row in matrix]

    def gauss_elimination(self, matrix):
        """
        Приведение матрицы к ступенчатому виду методом Гаусса над полем GF(2)
        Все операции выполняются по модулю 2 (используется XOR)

        Смотрим значения в столбце -> там где 1 - ведущая строка
        Применяем XOR к остальным строкам с ведущей строкой -> устраняем 1
        Переходим к следующему столбцу
        Пропускаем использованные строки
        """
        # Размерность матрицы
        m = len(matrix)      # количество строк (equations)
        n = len(matrix[0])   # количество столбцов (variables)
        
        # Массив для отметки использованных строк в качестве ведущих
        used = [0] * m
        # История преобразований матрицы
        steps = []
        
        # Множество обработанных столбцов для оптимизации
        processed_cols = set()
        # Текущий ранг матрицы (количество ненулевых строк)
        current_rank = 0
        
        # Обрабатываем каждый столбец матрицы слева направо
        for k in range(n):
            # Если достигли максимального ранга - выходим
            if current_rank >= m:
                break
            
            # Быстрая проверка наличия единиц в текущем столбце
            has_ones = False
            for r in range(m):
                # Ищем 1 в неиспользованной строке
                if matrix[r][k] == 1 and not used[r]:
                    has_ones = True
                    break
            
            # Если нет единиц - переходим к следующему столбцу
            if not has_ones:
                continue
            
            # Поиск ведущей строки (pivot) и обработка
            for r in range(m):
                if matrix[r][k] == 1 and not used[r]:
                    # Собираем индексы строк для XOR-операции
                    rows_to_process = []
                    for i in range(m):
                        # Находим строки с 1 в текущем столбце (кроме ведущей)
                        if matrix[i][k] == 1 and i != r:
                            rows_to_process.append(i)
                    
                    # Пакетная обработка отобранных строк
                    if rows_to_process:
                        pivot_row = matrix[r]
                        for i in rows_to_process:
                            # XOR начиная с текущего столбца k
                            for j in range(k, n):
                                matrix[i][j] ^= pivot_row[j]
                    
                    # Отмечаем обработанную ведущую строку
                    used[r] = 1
                    # Увеличиваем ранг матрицы
                    current_rank += 1
                    # Добавляем столбец в обработанные
                    processed_cols.add(k)
                    break
        
        return matrix, steps, used

    def find_solutions(self, matrix, used):
        """
        Находит нетривиальные решения системы линейных уравнений над полем GF(2).
        used: массив использованных строк (ведущих)
        returns: список векторов-решений

        Находим ведущие переменные (переменные, которые соответствуют первым ненулевым элементам в строках)
        Находим свободные переменные (переменные, которые не являются ведущими)
        Присваиваем значения свободным переменным и находим ведущие
        """
        # Получаем размеры матрицы и её ранг
        m = len(matrix)          # число строк (уравнений)
        n = len(matrix[0])       # число столбцов (переменных)
        rank = sum(used)         # ранг матрицы (число ненулевых строк)
        
        # Если ранг равен числу переменных - только нулевое решение
        if rank >= n:
            return []
        
        # Находим ведущие столбцы и соответствующие им строки
        leading_cols = set()     # множество индексов ведущих столбцов
        col_to_row = {}         # отображение: ведущий столбец -> его строка
        
        # Для каждой использованной строки находим её ведущий элемент
        for i in range(m):
            if used[i]:          # если строка использовалась как ведущая
                for j in range(n):
                    if matrix[i][j] == 1:  # первая единица - ведущий элемент
                        leading_cols.add(j)
                        col_to_row[j] = i
                        break
        
        # Определяем свободные переменные (столбцы без ведущих элементов)
        free_cols = [j for j in range(n) if j not in leading_cols]
        if not free_cols:        # если нет свободных переменных
            return []
        
        solutions = []
        # Строим решение для каждой свободной переменной
        for free_col in free_cols:
            # Инициализируем вектор решения нулями
            solution = [0] * n
            # Присваиваем 1 текущей свободной переменной
            solution[free_col] = 1
            
            # Обратная подстановка для нахождения значений базисных переменных
            changed = True
            while changed:       # продолжаем пока есть изменения
                changed = False
                # Проходим по всем ведущим столбцам
                for col in leading_cols:
                    row = col_to_row[col]  # соответствующая строка
                    new_val = 0
                    # Вычисляем значение базисной переменной через свободные
                    for j in range(n):
                        if matrix[row][j] == 1 and j != col:
                            new_val ^= solution[j]  # XOR с текущими значениями
                    # Обновляем значение если оно изменилось
                    if solution[col] != new_val:
                        solution[col] = new_val
                        changed = True
            
            # Добавляем решение если оно ненулевое
            if any(solution):    # проверка на нетривиальность
                solutions.append(solution)
        
        return solutions

    def matrix_to_string(self, matrix):
        html = "<table style='font-family: monospace; border-spacing: 10px;'>"
        for i, row in enumerate(matrix):
            html += f"<tr><td>Строка {i+1}:</td>"
            for num in row:
                html += f"<td>{num}</td>"
            html += "</tr>"
        html += "</table>"
        return html

    def run(self):
        # Построение матрицы A
        matrix_A = self.build_matrix_A()
        self.matrix_update.emit("<h3>Исходная матрица A:</h3>" + self.matrix_to_string(matrix_A))
        
        # Приведение по модулю 2
        matrix_mod2 = self.mod2_matrix(matrix_A)
        self.matrix_update.emit("<h3>Матрица A по модулю 2:</h3>" + self.matrix_to_string(matrix_mod2))
        
        # Метод Гаусса
        eliminated_matrix, steps, used = self.gauss_elimination(matrix_mod2.copy())

        # for i, step in enumerate(steps, 1):
        #     self.matrix_update.emit(f"<h3>Шаг {i}:</h3>" + self.matrix_to_string(eliminated_matrix))
        
        # Поиск решений
        solutions = self.find_solutions(eliminated_matrix, used)
        if solutions:
            self.matrix_update.emit("\nНайдены нетривиальные решения:")
            for i, solution in enumerate(solutions, 1):
                self.matrix_update.emit(f"\nРешение {i}: {solution}")
            self.solution_found.emit(solutions)
        else:
            self.matrix_update.emit("\nНетривиальных решений не найдено. Увеличиваем B и добавочное значение.")
            self.no_solutions.emit()

class FactorFinder(QThread):
    update_signal = pyqtSignal(str)
    factors_found = pyqtSignal(int, int)
    no_factors = pyqtSignal()

    def __init__(self, solutions, smooth_numbers, x_values, y_values, n):
        super().__init__()
        self.solutions = solutions
        self.smooth_numbers = smooth_numbers
        self.x_values = x_values
        self.y_values = y_values  # Add y_values to store original numbers
        self.n = n

    def calculate_x_y(self, solution_vector):
        # Находим позиции единиц в векторе решения
        # Например: [0,1,0,1] -> [1,3]
        indices = [i for i, bit in enumerate(solution_vector) if bit == 1]
        
        # Получаем ключи B-гладких чисел
        smooth_keys = list(self.smooth_numbers.keys())
        # Проверяем, что все индексы допустимы
        valid_indices = all(idx < len(smooth_keys) for idx in indices)
        
        if not valid_indices:
            return None, None, None
        
        # Вычисляем X = произведение x-значений
        # X = x1 * x2 * ... * xk
        X = 1
        for idx in indices:
            smooth_key = smooth_keys[idx]
            X *= abs(self.x_values[smooth_key])
        
        # Вычисляем y = sqrt(произведение y-значений)
        # y = sqrt(y1 * y2 * ... * yk)
        y_product = 1
        for idx in indices:
            smooth_key = smooth_keys[idx]
            y_product *= abs(self.y_values[smooth_key])
        
        y = int(math.sqrt(y_product))
        return X, y, indices

    def find_factors(self):
        for i, solution in enumerate(self.solutions):
            X, y, indices = self.calculate_x_y(solution)
            
            # Skip invalid solutions
            if X is None:
                self.update_signal.emit(f"<h4>Решение {i+1}: пропущено - индексы выходят за границы</h4>")
                continue
                
            gcd = math.gcd(X - y, self.n)
            
            if gcd != 1 and gcd != self.n:
                factor2 = self.n // gcd
                self.update_signal.emit(f"<b>Найдены множители:</b> {gcd} и {factor2}")
                self.factors_found.emit(gcd, factor2)
                return True
        
        self.update_signal.emit("Не удалось найти множители. Увеличиваем B и добавочное значение.")
        self.no_factors.emit()
        return False

    def run(self):
        self.find_factors()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.n = 0
        self.b = 0
        self.additional_value = 0
        self.x_values = []
        self.y_values = []  
        self.smooth_numbers = {}
        self.solutions = []
        self.initUI()
        
    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # Создаем поля ввода
        input_layout = QGridLayout()
        
        self.n_input = QLineEdit()
        self.b_input = QLineEdit()
        self.additional_value_input = QLineEdit()
        
        input_layout.addWidget(QLabel("Введите n:"), 0, 0)
        input_layout.addWidget(self.n_input, 0, 1)
        input_layout.addWidget(QLabel("Введите B:"), 1, 0)
        input_layout.addWidget(self.b_input, 1, 1)
        input_layout.addWidget(QLabel("Добавочное значение:"), 2, 0)
        input_layout.addWidget(self.additional_value_input, 2, 1)
        
        # Кнопка для запуска вычислений
        self.calculate_button = QPushButton("Вычислить")
        self.calculate_button.clicked.connect(self.calculate)
        
        # Таблица для отображения результатов
        self.table = QTableWidget()
        self.table.setColumnCount(0)
        self.table.setRowCount(2)
        
        # Текстовое поле для вывода процесса просеивания
        self.sieve_output = QTextEdit()
        self.sieve_output.setReadOnly(True)
        self.sieve_output.setAcceptRichText(True)
        self.sieve_output.setHtml("")

        # Добавляем новые окна
        self.matrix_output = QTextEdit()
        self.matrix_output.setReadOnly(True)
        self.matrix_output.setAcceptRichText(True)
        self.matrix_output.setHtml("")

        self.solutions_output = QTextEdit()
        self.solutions_output.setReadOnly(True)
        
        layout.addWidget(QLabel("Матрица A и её преобразования:"))
        layout.addWidget(self.matrix_output)
        layout.addWidget(QLabel("Найденные решения:"))
        layout.addWidget(self.solutions_output)
        
        layout.addLayout(input_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.table)
        layout.addWidget(self.sieve_output)
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('Факторизация')
       
    def update_xy_table(self):
        self.table.setColumnCount(len(self.x_values))
        
        for col, value in enumerate(self.x_values):
            self.table.setItem(0, col, QTableWidgetItem(str(value)))
        
        for col, value in enumerate(self.y_values):
            self.table.setItem(1, col, QTableWidgetItem(str(value)))
        
        self.table.setVerticalHeaderLabels(["x", "x^2 - n"])

    def calculate(self):
        try:
            self.reset_outputs()
            self.n = int(self.n_input.text())
            self.b = int(self.b_input.text())
            self.additional_value = int(self.additional_value_input.text())
            
            x_start = int(math.sqrt(self.n)) + 1
            m = x_start + self.additional_value
            right_border = m + self.additional_value
            
            self.x_values = list(range(x_start, right_border + 1))
            self.y_values = [(x * x - self.n) for x in self.x_values]
            
            self.update_xy_table()
            
            self.start_sieving(self.y_values, self.b, self.additional_value, self.n)
        except ValueError as e:
            self.sieve_output.setHtml(f"<span style='color: red'>Ошибка ввода данных: {e}</span>")

    def reset_outputs(self):
        self.sieve_output.clear()
        self.matrix_output.clear()
        self.solutions_output.clear()
            
    def start_sieving(self, y_values, b, additional_value, n):
        self.sieving_thread = SievingThread(y_values, b, additional_value, n)
        self.sieving_thread.update_signal.connect(self.update_sieve_output)
        self.sieving_thread.complete_signal.connect(self.sieving_complete)
        self.sieving_thread.start()
        
    def update_sieve_output(self, text):
        self.sieve_output.clear()  # Очищаем перед обновлением
        self.sieve_output.setHtml(text)  # Устанавливаем HTML
        
    def sieving_complete(self, smooth_numbers, y_values):
        self.smooth_numbers = smooth_numbers
        self.y_values = y_values  
        primes = sorted(list({p for factors in smooth_numbers.values() for p in factors.keys()}))
        self.matrix_solver = MatrixSolver(smooth_numbers, primes)
        self.matrix_solver.matrix_update.connect(self.update_matrix_output)
        self.matrix_solver.solution_found.connect(self.update_solutions_output)
        self.matrix_solver.no_solutions.connect(self.restart_sieving)
        self.matrix_solver.start()

    def update_matrix_output(self, text):
        current_html = self.matrix_output.toHtml()
        if not current_html or current_html.isspace():
            self.matrix_output.setHtml(text)
        else:
            self.matrix_output.setHtml(current_html + text)

    def update_solutions_output(self, solutions):
        self.solutions = solutions
        self.solutions_output.clear()
        self.solutions_output.append("<h3>Найденные нетривиальные решения:</h3>")
        for i, solution in enumerate(solutions):
            self.solutions_output.append(f"Решение {i+1}: {solution}")
        
        # Fix: Pass y_values to FactorFinder
        self.factor_finder = FactorFinder(
            solutions, 
            self.smooth_numbers, 
            self.x_values, 
            self.y_values,  
            self.n
        )
        self.factor_finder.update_signal.connect(self.update_factorization_output)
        self.factor_finder.factors_found.connect(self.show_final_factors)
        self.factor_finder.no_factors.connect(self.restart_sieving)
        self.factor_finder.start()

    def update_factorization_output(self, text):
        self.solutions_output.append(text)

    def show_final_factors(self, factor1, factor2):
        self.solutions_output.append(f"<h3>Итоговые множители числа {self.n}:</h3>")
        self.solutions_output.append(f"{factor1} и {factor2}")

    def restart_sieving(self):
        self.reset_outputs()
        self.b += 1
        self.additional_value += 1
        
        x_start = int(math.sqrt(self.n)) + 1
        m = x_start + self.additional_value
        right_border = m + self.additional_value
        
        self.x_values = list(range(x_start, right_border + 1))
        self.y_values = [(x * x - self.n) for x in self.x_values]
        
        # Update table
        self.update_xy_table()
        
        self.start_sieving(self.y_values, self.b, self.additional_value, self.n)
    
    
            

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())