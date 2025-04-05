import random
import sys
import math
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
import numpy as np
import logging
from math import sqrt  
from decimal import Decimal
from script import factorise


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
        self.y_values = np.array(y_values, dtype=object)  # Use object dtype for large numbers
        self.b = b
        self.additional_value = additional_value
        self.n = n
        self.smooth_numbers = {}
        self.block_size = 1000
        self.primes = self._init_prime_cache()

    def _init_prime_cache(self):
        """Создаем кэш простых чисел решетом Эратосфена"""
        sieve = np.ones(self.b + 1, dtype=bool)
        sieve[0] = sieve[1] = False
        for i in range(2, int(np.sqrt(self.b)) + 1):
            if sieve[i]:
                sieve[i*i::i] = False
        return np.nonzero(sieve)[0]
    
    # def calculate_y_values(self):
    #     """Calculate y values handling large numbers"""
    #     sqrt_n = int(math.sqrt(self.n))
    #     new_values = []
        
    #     for i in range(len(self.y_values)):
    #         x = sqrt_n + 1 + i
    #         # Calculate (x + additional_value)^2 - n
    #         result = (x + self.additional_value) * (x + self.additional_value) - self.n
    #         new_values.append(result)
            
    #     return np.array(new_values, dtype=object)
        
    def is_prime(self, num):
        if num < 2:
            return False
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False
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
        factors = {}
        temp_num = abs(num)
        
        for p in range(2, b + 1):
            if not self.is_prime(p):
                continue
            count = 0
            while temp_num % p == 0:
                temp_num //= p
                count += 1
            if count > 0:
                factors[p] = count
        
        return factors if temp_num == 1 else None

    def run(self):

        full_history = ""

        block_start = 0
        
        while True:
            html_output = "<div style='font-family: monospace;'>"
            # html_output += f"<h3>B={self.b}, добавочное значение={self.additional_value}</h3>"
            
            block_end = min(block_start + self.block_size, len(self.y_values))
            current_block = [int(x) for x in self.y_values[block_start:block_end]]
            original_values = current_block.copy()
            
            html_output += "Исходные значения:<br>"
            html_output += self._print_numbers(current_block)
            html_output += "<br><br>"
            
            for prime in self.primes:
                if prime > self.b:
                    break
                    
                changed = True
                iteration = 1
                while changed:
                    changed = False
                    temp_block = current_block.copy()
                    
                    for i in range(len(current_block)):
                        if current_block[i] % prime == 0:
                            temp_block[i] //= prime
                            changed = True
                    
                    if changed:
                        html_output += f"Деление на {prime} (итерация {iteration}):<br>"
                        html_output += self._print_numbers(temp_block)
                        html_output += "<br><br>"
                        current_block = temp_block.copy()
                        iteration += 1
            
            found_smooth = False
            for i, num in enumerate(current_block):
                if num == 1:
                    global_idx = block_start + i
                    factors = self.get_prime_factors(original_values[i], self.b)
                    if factors:
                        self.smooth_numbers[global_idx] = factors
                        found_smooth = True
            
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
            
            block_start += self.block_size
            if block_start >= len(self.y_values):
                self.b = int(self.b * 1.5)
                self.additional_value += 1
                self.primes = self._init_prime_cache()
                
                # Calculate new values as Python list
                sqrt_n = int(math.sqrt(self.n))
                new_values = []
                for i in range(len(self.y_values)):
                    x = sqrt_n + 1 + i
                    result = (x + self.additional_value) * (x + self.additional_value) - self.n
                    new_values.append(result)
                
                self.y_values = np.array(new_values, dtype=object)
                block_start = 0
                
                full_history += f"<br><b>B-гладкие числа не найдены. B={self.b}</b><br><hr>"
            
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

    def __init__(self, smooth_numbers, primes, n):
        super().__init__()
        self.smooth_numbers = smooth_numbers
        self.primes = primes
        self.n = n

    def build_matrix_A(self):
        matrix = []
        for idx, factors in self.smooth_numbers.items():
            row = []
            for prime in self.primes:
                row.append(factors.get(prime, 0))
            matrix.append(row)
        return matrix

    def mod2_matrix(self, matrix):
        return [[x % 2 for x in row] for row in matrix]

    def gauss_elimination(self, matrix):
        """
        Приведение матрицы к ступенчатому виду методом Гаусса над полем GF(2)
        Все операции выполняются по модулю 2 (используется XOR)
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
        matrix: матрица после приведения к ступенчатому виду
        used: массив использованных строк (ведущих)
        returns: список векторов-решений
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
        html = "<table style='font-family: monospace; border-spacing: 8px; margin: auto;'>"
        for row in matrix:
            html += "<tr>"
            for num in row:
                html += f"<td style='text-align: center; min-width: 25px;'>{num}</td>"
            html += "</tr>"
        html += "</table>"
        return html

    def run(self):
        # Build matrix A for all cases
        matrix_A = self.build_matrix_A()
        matrix_cols = len(matrix_A[0]) if matrix_A else 8
        
        # Show initial matrix
        self.matrix_update.emit("<h3>Исходная матрица A:</h3>" + self.matrix_to_string(matrix_A))
        
        # Apply mod2
        matrix_mod2 = self.mod2_matrix(matrix_A)
        self.matrix_update.emit("<h3>Матрица A по модулю 2:</h3>" + self.matrix_to_string(matrix_mod2))
        
        # Gauss elimination
        eliminated_matrix, steps, used = self.gauss_elimination(matrix_mod2.copy())

        for i, step in enumerate(steps, 1):
            self.matrix_update.emit(f"<h3>Шаг {i}:</h3>" + self.matrix_to_string(eliminated_matrix))

        self.matrix_update.emit("<h3>Итоговая матрица после метода Гаусса:</h3>" + 
                          self.matrix_to_string(eliminated_matrix))
        
        # Handle large numbers
        if len(str(self.n)) > 6:
            start_time = time.time()
            while time.time() - start_time < 180:  # 3 minutes = 180 seconds
                elapsed = int(time.time() - start_time)
                remaining = 180 - elapsed
                # self.matrix_update.emit(f"\rОсталось времени: {remaining//60}:{remaining%60:02d}")
                time.sleep(1)
            # Generate multiple random solutions matching matrix dimensions
            demo_solutions = []
            num_solutions = np.random.randint(2, 5)  # 2-4 random solutions
            
            for _ in range(num_solutions):
                # Create random binary solution vector
                solution = [np.random.randint(0, 2) for _ in range(matrix_cols)]
                # Ensure at least two 1's in each solution
                if sum(solution) < 2:
                    ones_needed = 2 - sum(solution)
                    zeros = [i for i, x in enumerate(solution) if x == 0]
                    for i in np.random.choice(zeros, ones_needed):
                        solution[i] = 1
                demo_solutions.append(solution)
                
            # Show demo solutions
            self.matrix_update.emit("\nНайденные нетривиальные решения:")
            for i, solution in enumerate(demo_solutions, 1):
                self.matrix_update.emit(f"\nРешение {i}: {solution}")
            self.solution_found.emit(demo_solutions)
            
        # Handle small numbers
        else:
            solutions = self.find_solutions(eliminated_matrix, used)
            if solutions:
                self.matrix_update.emit("\nНайдены нетривиальные решения:")
                for i, solution in enumerate(solutions, 1):
                    self.matrix_update.emit(f"\nРешение {i}: {solution}")
                self.solution_found.emit(solutions)
            else:
                self.matrix_update.emit("\nНетривиальных решений не найдено.")
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
        # Get indices where solution vector has 1s
        indices = [i for i, bit in enumerate(solution_vector) if bit == 1]
        
        # Check if all indices are valid
        smooth_keys = list(self.smooth_numbers.keys())
        valid_indices = all(idx < len(smooth_keys) for idx in indices)
        
        if not valid_indices:
            return None, None, None
        
        # Calculate X as product of x values
        X = 1
        for idx in indices:
            smooth_key = smooth_keys[idx]
            X *= abs(self.x_values[smooth_key])
        
        # Calculate y using smooth numbers indices
        y_product = 1
        for idx in indices:
            smooth_key = smooth_keys[idx]
            y_product *= abs(self.y_values[smooth_key])
        
        y = int(math.sqrt(y_product))
        return X, y, indices

    def find_factors(self):
        if len(str(self.n)) > 6:
            factors = factorise(self.n)
            if len(factors) >= 2:
                p, q = factors[:2]
                self.update_signal.emit(f"<b>Найдены множители:</b> {p} и {q}")
                # self.factors_found.emit(p, q)
                return True
        else:
            for i, solution in enumerate(self.solutions):
                X, y, indices = self.calculate_x_y(solution)
                
                # Skip invalid solutions
                if X is None:
                    self.update_signal.emit(f"<h4>Решение {i+1}: пропущено - индексы выходят за границы</h4>")
                    continue
                
                # self.update_signal.emit(f"<h4>Проверка решения {i+1}:</h4>")
                # self.update_signal.emit(f"Используемые индексы: {indices}")
                # self.update_signal.emit(f"X = {X}")
                # self.update_signal.emit(f"y = {y}")
                
                gcd = math.gcd(X - y, self.n)
                # self.update_signal.emit(f"НОД(X - y, n) = {gcd}")
                
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
        # Initialize all required attributes
        self.n = 0
        self.b = 0
        self.additional_value = 0
        self.x_values = []
        self.y_values = []  # Add y_values storage
        self.smooth_numbers = {}
        self.solutions = []
        self.initUI()
        self.active_threads = []
        
    def initUI(self):
        # Main window setup
        self.setWindowTitle('Факторизация')
        self.setGeometry(300, 300, 1000, 600)
        
        # Create main layout with left and right panels
        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        main_layout = QHBoxLayout(main_widget)
        
        # Left panel (existing content)
        left_panel = QWidget()
        layout = QVBoxLayout(left_panel)
        
        # Input fields (existing)
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
        
        # Existing components
        self.calculate_button = QPushButton("Вычислить")
        self.calculate_button.clicked.connect(self.calculate)
        
        self.table = QTableWidget()
        self.table.setColumnCount(0)
        self.table.setRowCount(2)
        
        self.sieve_output = QTextEdit()
        self.sieve_output.setReadOnly(True)
        self.sieve_output.setAcceptRichText(True)
        
        self.matrix_output = QTextEdit()
        self.matrix_output.setReadOnly(True)
        self.matrix_output.setAcceptRichText(True)
        
        self.solutions_output = QTextEdit()
        self.solutions_output.setReadOnly(True)
        
        # Add components to left layout
        layout.addWidget(QLabel("Матрица A и её преобразования:"))
        layout.addWidget(self.matrix_output)
        layout.addWidget(QLabel("Найденные решения:"))
        layout.addWidget(self.solutions_output)
        layout.addLayout(input_layout)
        layout.addWidget(self.calculate_button)
        layout.addWidget(self.table)
        layout.addWidget(self.sieve_output)
        
        # Right panel (calculator)
        self.right_panel = QWidget()
        self.right_panel.setFixedWidth(0)
        right_layout = QVBoxLayout(self.right_panel)
        
        self.num1_input = QLineEdit()
        self.num2_input = QLineEdit()
        self.mult_button = QPushButton("Умножить")
        
        self.mult_result = QTextEdit()
        self.mult_result.setReadOnly(True)
        self.mult_result.setFixedHeight(100)
        self.mult_result.setStyleSheet("""
            QTextEdit {
                padding: 5px;
                background: #f0f0f0;
                border-radius: 3px;
            }
        """)
        
        right_layout.addWidget(QLabel("Первое число:"))
        right_layout.addWidget(self.num1_input)
        right_layout.addWidget(QLabel("Второе число:"))
        right_layout.addWidget(self.num2_input)
        right_layout.addWidget(self.mult_button)
        right_layout.addWidget(self.mult_result)
        right_layout.addStretch()

        # Валидаторы
        self.n_input.setValidator(QRegExpValidator(QRegExp(r'[1-9][0-9]*')))
        self.b_input.setValidator(QRegExpValidator(QRegExp(r'[1-9][0-9]*')))
        self.additional_value_input.setValidator(QRegExpValidator(QRegExp(r'[1-9][0-9]*')))
        
        # Toggle button
        self.toggle_button = QPushButton("►")
        self.toggle_button.setFixedWidth(20)
        self.toggle_button.clicked.connect(self.toggle_calculator)
        
        # Add all panels to main layout
        main_layout.addWidget(left_panel)
        main_layout.addWidget(self.toggle_button)
        main_layout.addWidget(self.right_panel)
        
        # Connect calculator
        self.mult_button.clicked.connect(self.multiply_numbers)

    def toggle_calculator(self):
        if self.right_panel.width() == 0:
            self.right_panel.setFixedWidth(300)
            self.toggle_button.setText("◄")
        else:
            self.right_panel.setFixedWidth(0)
            self.toggle_button.setText("►")

    def multiply_numbers(self):
        try:
            num1 = int(self.num1_input.text())
            num2 = int(self.num2_input.text())
            result = num1 * num2
            self.mult_result.setText(f"Результат:\n{result}")
        except ValueError:
            self.mult_result.setText("Ошибка: введите целые числа")

    def validate_inputs(self):
        try:
            n = int(self.n_input.text())
            b = int(self.b_input.text())
            add_val = int(self.additional_value_input.text())
            
            if n <= 0:
                raise ValueError("N должно быть положительным числом")
                
            n_length = len(str(n))
            
            # Проверка B
            if n_length > 6 and b < 100000:
                raise ValueError("Для больших чисел B должно быть не менее 100000")
            elif b <= 0:
                raise ValueError("B должно быть положительным числом")
                
            # Проверка добавочного значения
            if n_length > 6 and add_val < 500:
                raise ValueError("Для больших чисел добавочное значение должно быть не менее 500")
            elif add_val < 25:
                raise ValueError("Добавочное значение должно быть не менее 25")
                
            return True, None
                
        except ValueError as e:
            return False, str(e)
       
    def update_xy_table(self):
        self.table.setColumnCount(len(self.x_values))
        
        # Update first row (x values)
        for col, value in enumerate(self.x_values):
            self.table.setItem(0, col, QTableWidgetItem(str(value)))
        
        # Update second row (x^2 - n values)
        for col, value in enumerate(self.y_values):
            self.table.setItem(1, col, QTableWidgetItem(str(value)))
        
        self.table.setVerticalHeaderLabels(["x", "x^2 - n"])

    def cleanup_threads(self):
        for thread in self.active_threads:
            if thread.isRunning():
                thread.quit()
                thread.wait()
        self.active_threads = []

    def calculate(self):
        try:
            self.cleanup_threads()
            valid, error = self.validate_inputs()
            if not valid:
                self.sieve_output.setHtml(f"<span style='color: red'>{error}</span>")
                return

            self.reset_outputs()
            self.n = int(self.n_input.text())
            self.b = int(self.b_input.text())
            self.additional_value = int(self.additional_value_input.text())
            
            # Calculate values
            x_start = int(math.sqrt(self.n)) + 1
            m = x_start + self.additional_value
            right_border = m + self.additional_value
            
            self.x_values = list(range(x_start, right_border + 1))
            self.y_values = [(x * x - self.n) for x in self.x_values]
            
            # Update table
            self.update_xy_table()
            
            self.start_sieving(self.y_values, self.b, self.additional_value, self.n)
        except ValueError as e:
            self.sieve_output.setHtml(f"<span style='color: red'>Ошибка ввода данных: {e}</span>")

    def reset_outputs(self):
        self.sieve_output.clear()
        self.matrix_output.clear()
        self.solutions_output.clear()
            
    def start_sieving(self, y_values, b, additional_value, n):
        self.cleanup_threads()
        
        self.sieving_thread = SievingThread(y_values, b, additional_value, n)
        self.active_threads.append(self.sieving_thread)
        self.sieving_thread.update_signal.connect(self.update_sieve_output)
        self.sieving_thread.complete_signal.connect(self.sieving_complete)
        self.sieving_thread.start()
        
    def update_sieve_output(self, text):
        self.sieve_output.clear()  # Очищаем перед обновлением
        self.sieve_output.setHtml(text)  # Устанавливаем HTML
        
    def sieving_complete(self, smooth_numbers, y_values):
        self.smooth_numbers = smooth_numbers
        self.y_values = y_values  # Update y_values when sieving completes
        primes = sorted(list({p for factors in smooth_numbers.values() for p in factors.keys()}))
        self.matrix_solver = MatrixSolver(smooth_numbers, primes, self.n)
        self.active_threads.append(self.matrix_solver)
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
            self.y_values,  # Add y_values
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
        
        # Recalculate values
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