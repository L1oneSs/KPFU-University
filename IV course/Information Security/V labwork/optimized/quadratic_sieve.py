# -*- coding: utf-8 -*-
import numpy as np
import math
from itertools import chain
from gmpy2 import gmpy2

from common import *


def prime_range(start, end):
    """Генерация простых чисел в заданном диапазоне с использованием метода Миллера-Рабина"""
    primes = []
    for i in range(start, end + 1):
        if miller_rabin_test(i, int(np.log2(end))):
            primes.append(i)
    return primes


def is_quad_residue(a, p):
    """Проверка, является ли a квадратичным вычетом по модулю p"""
    if p < 2:
        raise ValueError("Модуль p должен быть простым числом больше 2")
    if quad_residue(a, p) == 1:
        return True
    return False


def quad_residue(a, n):
    """Вычисление символа Лежандра (a / n)"""
    a = a % n  # Сначала берем остаток от деления a на n
    q = (n - 1) // 2  # Вычисляем q
    result = 1  # Инициализируем результат как 1

    # Если q равно 0, то оно всегда квадратичный вычет
    if q == 0:
        return 1

    # Алгоритм для проверки квадратичности вычета
    while q > 0:
        if q % 2 == 0:  # Если степень четная
            a = (a ** 2) % n  # Возводим a в квадрат по модулю n
            q //= 2  # Разделяем q на 2
        else:  # Если степень нечетная
            q -= 1
            result = (result * a) % n  # Умножаем результат на a и берем остаток по модулю n

    return result


def generate_factor_base(N, B):
    """Генерация факторной базы"""
    primes = list(prime_range(2, B + 1))
    factor_base = [p for p in primes if is_quad_residue(N, p)]
    return factor_base


def get_sieve_sequence(N, I, root):
    """Генерация последовательности чисел вида x^2 - N"""
    return [x ** 2 - N for x in range(root, root + I)]


def sieve_for_smooth_numbers(sieve_list, factor_base, root, N):
    """Проcеивание решета для нахождения B-гладких чисел"""
    if factor_base[0] == 2:
        sieve_list = process_for_two(sieve_list)
    for p in factor_base[1:]:
        process_prime_factor(sieve_list, p, root, N)
    return sieve_list


def process_for_two(sieve_list):
    """Обработка числа 2"""
    i = 0
    while sieve_list[i] % 2 != 0:
        i += 1
    for j in range(i, len(sieve_list), 2):
        while sieve_list[j] % 2 == 0:
            sieve_list[j] //= 2
    return sieve_list


def process_prime_factor(sieve_list, p, root, N):
    """Обработка простого числа p для решета"""
    residues = solve_modular_square_root(N, p)  # решения x^2 = n (mod p)

    for residue in residues:
        # Индексы чисел, которые будут делиться на p
        start_index = (residue - root) % p
        for i in range(start_index, len(sieve_list), p):
            while sieve_list[i] % p == 0:
                sieve_list[i] //= p


def solve_modular_square_root(n, p):
    """Решение квадратного корня по модулю p с помощью алгоритма Тонелли-Шенкса"""
    # Проверяем, является ли n квадратичным вычетом по модулю p
    if not is_quad_residue(n, p):
        raise ValueError("Число не является квадратичным вычетом (mod p)")

    # Шаг 1: Найдем q и s, такие что p - 1 = q * 2^s
    q, s = p - 1, 0
    while q % 2 == 0:
        q //= 2
        s += 1

    # Шаг 2: Если s = 1, то используем быстрый метод для нахождения корня
    if s == 1:
        root = pow(n, (p + 1) // 4, p)
        return root, p - root

    # Шаг 3: Находим подходящее z, такое что z^2 ≡ -1 (mod p)
    z = find_non_residue(p)

    # Шаг 4: Инициализация переменных
    c = pow(z, q, p)
    r = pow(n, (q + 1) // 2, p)
    t = pow(n, q, p)
    m = s

    # Шаг 5: Основной цикл поиска корня
    while t != 1:
        t2 = (t * t) % p
        i = 1
        while t2 != 1:
            t2 = (t2 * t2) % p
            i += 1
        b = pow(c, 1 << (m - i - 1), p)
        r = (r * b) % p
        c = (b * b) % p
        t = (t * c) % p
        m = i

    return r, p - r


def find_non_residue(p):
    """Поиск подходящего z, такого что z^2 ≡ -1 (mod p)"""
    for z in range(2, p):
        if is_quad_residue(z, p) == 0:
            return z


def find_smooth_numbers_in_sieve(sieve_list, sieve_seq, root, factor_base):
    """Поиск B-гладких чисел в решете"""
    smooth_numbers = []
    x_list = []
    indices = []

    for i in range(len(sieve_list)):
        if len(smooth_numbers) >= len(factor_base):
            break
        if sieve_list[i] == 1:
            smooth_numbers.append(sieve_seq[i])
            x_list.append(i + root)
            indices.append(i)

    return smooth_numbers, x_list, indices


def find_b_smooth_numbers(factor_base, N, first, I):
    """Поиск B-гладких чисел"""
    sieve_seq = get_sieve_sequence(N, I, first)
    sieve_list = sieve_seq.copy()

    sieve_list = sieve_for_smooth_numbers(sieve_list, factor_base, first, N)
    smooth_numbers, x_list, indices = find_smooth_numbers_in_sieve(sieve_list, sieve_seq, first, factor_base)

    return smooth_numbers, x_list, indices


def factorize_with_base(n, factor_base):
    """Факторизация числа n с использованием факторной базы"""
    factors = []
    if n < 0:
        factors.append(-1)
    for p in factor_base:
        if p != -1:
            while n % p == 0:
                factors.append(p)
                n //= p
    return factors


def build_exponent_vector(factors, factor_base):
    """Строит вектор показателей степени по модулю 2 на основе факторов числа"""
    exp_vector = [0] * len(factor_base)
    for i, p in enumerate(factor_base):
        if p in factors:
            exp_vector[i] = factors.count(p) % 2
    return exp_vector


def build_matrix(smooth_nums, factor_base):
    """Строит матрицу экспонент по модулю 2 из гладких чисел"""
    factor_base = [-1] + factor_base
    matrix = []
    factorized_nums = [factorize_with_base(n, factor_base) for n in smooth_nums]

    # Проверка на квадрат и построение матрицы
    for n, factors in zip(smooth_nums, factorized_nums):
        exp_vector = build_exponent_vector(factors, factor_base)

        # Если вектор экспонент не содержит единиц, то число является квадратом
        if 1 not in exp_vector:
            return True, n

        matrix.append(exp_vector)

    matrix_np = np.array(matrix, dtype=int)
    return False, matrix_np.T


def solve_row(sol_rows, M, marks, K=0):
    """Находит строки матрицы M, которые зависят от свободной строки sol_rows[K]."""
    solution_vector, indices = [], []
    free_row = sol_rows[K][0]
    for i in range(len(free_row)):
        if free_row[i] == 1:
            indices.append(i)
    # Строки с 1 в одном столбце будут зависимыми
    for r in range(len(M)):
        for i in indices:
            if M[r][i] == 1 and marks[r]:
                solution_vector.append(r)
                break

    solution_vector.append(sol_rows[K][1])
    return solution_vector


def solve(solution_vector, smooth_nums, xlist, N):
    """Вычисляет нетривиальный делитель числа N на основе найденных B-гладких чисел и соответствующих им значений x"""
    solution_nums = [smooth_nums[i] for i in solution_vector]
    x_nums = [xlist[i] for i in solution_vector]

    product = gmpy2.mpz(1)
    for n in solution_nums:
        product *= gmpy2.mpz(n)

    X = gmpy2.mpz(1)
    for n in x_nums:
        X *= gmpy2.mpz(n)

    y = gmpy2.isqrt(product)
    factor = gmpy2.gcd(X - y, N)

    return int(factor)


def gauss_elimination(M):
    """Выполняет метод Гаусса для приведения матрицы M к ступенчатому виду по модулю 2"""
    marks = [False] * len(M[0])
    M = np.array(M, dtype=np.uint8)

    for i in range(len(M)):
        row = M[i]
        pivot_idx = np.argmax(row) if 1 in row else -1

        if pivot_idx != -1:  # Если нашли опорный элемент
            marks[pivot_idx] = True

            # Исключаем 1-цы в других строках с тем же столбцом
            for k in chain(range(0, i), range(i + 1, len(M))):
                if M[k, pivot_idx] == 1:
                    M[k] = (M[k] + row) % 2

    M = M.T

    sol_rows = []
    for i, mark in enumerate(marks):
        if not mark:
            sol_rows.append([M[i].tolist(), i])

    if not sol_rows:
        return "Решений не найдено. Необходимо больше B-гладких чисел"

    return sol_rows, marks, M.tolist()


alphabet = {
    16: 'А', 17: 'Б', 18: 'В', 19: 'Г', 20: 'Д', 21: 'Е', 22: 'Ж', 23: 'З', 24: 'И', 25: 'Й',
    26: 'К', 27: 'Л', 28: 'М', 29: 'Н', 30: 'О', 31: 'П', 32: 'Р', 33: 'С', 34: 'Т', 35: 'У',
    36: 'Ф', 37: 'Х', 38: 'Ц', 39: 'Ч', 40: 'Ш', 41: 'Щ', 42: 'Ъ', 43: 'Ы', 44: 'Ь', 45: 'Э',
    46: 'Ю', 47: 'Я', 48: 'а', 49: 'б', 50: 'в', 51: 'г', 52: 'д', 53: 'е', 54: 'ж', 55: 'з',
    56: 'и', 57: 'й', 58: 'к', 59: 'л', 60: 'м', 61: 'н', 62: 'о', 63: 'п', 64: 'р', 65: 'с',
    66: 'т', 67: 'у', 68: 'ф', 69: 'х', 70: 'ц', 71: 'ч', 72: 'ш', 73: 'щ', 74: 'ъ', 75: 'ы',
    76: 'ь', 77: 'э', 78: 'ю', 79: 'я'
}


def find_d(e, phi):
    d = 0
    while (e * d) % phi != 1:
        d += 1
    return d


def decrypt(y, d, N):
    return pow(y, d, N)


def decode_word(n):
    word = ""
    while n > 0:
        pair = n % 100
        if pair in alphabet:
            word = alphabet[pair] + word
        else:
            word = "?" + word
        n //= 100
    return word


def factorize(N):
    length = len(str(N))
    print(f"Факторизация {length}-значного числа {N}...")

    if length <= 20:
        B = 10000
        I = 1000000
    else:
        B = 50000
        I = 10000000

    x = int(math.sqrt(N))
    print("Первое число (x): ", x)
    print("Последнее число (M): ", x + I)
    print("Граница гладкости (B): ", B)

    print("Вычисление элементов факторной базы...")
    factor_base = generate_factor_base(N, B)
    print("Факторная база:", factor_base)

    factor_base_size = len(factor_base)
    print(f"Поиск {factor_base_size} {B}-гладких чисел...")
    smooth_nums, xlist, indices = find_b_smooth_numbers(factor_base, N, x, I)
    print(f"Найдено {len(smooth_nums)} {B}-гладких чисел: ", np.array(smooth_nums))

    if len(smooth_nums) < factor_base_size:
        print("Недостаточно В-гладких чисел. Увеличьте интервал просеивания или размер факторной базы")
        return None

    print("Построение матрицы A степеней по модулю 2...")
    is_square, binary_matrix = build_matrix(smooth_nums, factor_base)
    print("Матрица A: ", np.array(binary_matrix))

    if is_square:
        index = smooth_nums.index(binary_matrix)
        factor = gcd(xlist[index] + np.sqrt(binary_matrix), N)
        print("Найден квадрат!")
        print("Делители: ", factor, N / factor)
        return int(factor), int(N / factor),  factor_base_size, 0

    print("Поиск нетривиальных решений уравнения Ax = 0 (алгоритм гауссова исключения неизвестных)...")
    sol_rows, marks, M_transposed = gauss_elimination(binary_matrix)
    solutions_count = len(sol_rows)
    print(f"Найдено {solutions_count} потенциальных решений")

    print("Вычисление вектора решения...")
    solution_vector = solve_row(sol_rows, M_transposed, marks, 0)
    print("Вектор решения:", solution_vector)

    print("Решение равенства квадратов...")
    factor = solve(solution_vector, smooth_nums, xlist, N)
    print("Найденный делитель: ", factor)

    for K in range(1, len(sol_rows)):
        if factor == 1 or factor == N:
            print("Делитель тривиален. Пробуем другой вектор решения...")
            solution_vector = solve_row(sol_rows, M_transposed, marks, K)
            print("Вектор решения:", solution_vector)
            factor = solve(solution_vector, smooth_nums, xlist, N)
            print("Найденный делитель", factor)
        else:
            print("Делитель нетривиален. Множители числа найдены!")
            print("Результат: ", factor, int(N / factor))
            break

    if factor == 1 or factor == N:
        return None

    return factor, int(N / factor), factor_base_size, solutions_count


def decode_secret_word(N, E, Sw):
    result = factorize(N)

    if not result:
        return None, None, None, None

    p = result[0]
    q = result[1]

    phi = (p - 1) * (q - 1)

    d = find_d(E, phi)
    print(f"Секретный ключ d: {d}")

    decrypted_number = decrypt(Sw, d, N)
    print(f"Расшифрованное число: {decrypted_number}")

    word = decode_word(decrypted_number)
    print(f"Расшифрованное слово: {word.lower()}")

    return p, q, d, word.lower()


if __name__ == '__main__':
    number = 82226843075939372862059256271
    public_key = 39574931997271565078938293107
    secret_word = 72299210235764206342642689453
    _, _, _, _ = decode_secret_word(number, public_key, secret_word)
