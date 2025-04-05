from math import gcd


def is_prime(num, iterations=5):
    if num <= 1 or (num % 2) == 0:
        return False

    # num - 1 = 2^two_degree * d
    # Цель - найти d и two_degree, где d - нечетное, two_degree - степень 2
    d = num - 1
    two_degree = 0
    while d % 2 == 0:
        d = d // 2
        two_degree += 1

    for _ in range(iterations):
        # Выбираем случайное основание [2,n - 2]
        a = secrets.randbelow(num - 3) + 2
        res = fast_pow(a, d, num)  # a ^ d mod num
        if res == 1 or res == num - 1:  # a ^ d = 1 (mod num) или a ^ d = -1 (mod num)
            # Продолжаем итерироваться в пользу простоты числа num
            continue
        for _ in range(two_degree - 1):
            # Есть ли среди значений res^2 mod num = num - 1
            res = fast_pow(res, 2, num)
            if res == num - 1:
                break
        else:
            # Возвращается составное
            return False
    return True


def prime_generate(bits):
    while True:
        digit = secrets.randbits(bits)
        if is_prime(digit):
            return digit


def fast_pow(base, exponent, modulus):
    res = 1
    # Уменьшаем по модулю во избежании больших чисел
    base = base % modulus

    # Степени base, соответствующие ненулевым позициям в двоичной записи
    # Если степень нечетная: x^y = x * x^([y//2])
    # a^13 = a ^ (2^3 + 2^2 + 2^0) = a^8 * a^4 * a^1
    while exponent > 0:
        # Аналог exponent mod 2 == 1 (Проверка на нечетность)
        # Учитываем текущую степень двойки
        if exponent & 1:
            res = (res * base) % modulus
        # Увеличение текущей степени двойки на одну
        # Переход к следующей степени двойки
        base = (base * base) % modulus
        # Побитовый сдвиг вправо, деление на 2
        exponent >>= 1

    return res


def generate_keypair(bits):
    p = prime_generate(bits)
    q = prime_generate(bits)
    # часть открытого и закрытого ключа
    n = p * q

    # Количество целых чисел, меньших n, которые взаимно просты с n
    phi = (p - 1) * (q - 1)

    # Публичная экспонента
    e = secrets.randbelow(phi)
    # e и phi - взаимно простые числа
    # e > 1, нечетное
    while gcd(e, phi) != 1:
        e = secrets.randbelow(phi)

    # Закрытая экспонента
    # d * e = 1 (mod phi)
    d = mod_inv(e, phi)

    # c = m^e mod n
    # m = c^d mod n

    return ((e, n), (d, n))


# Мультипликативное обратное числу a по модулю b
# (a * inv) mod b == 1
# a * x + b * y = НОД(a, b)
def mod_inv(a, b):
    original_b = b
    # Начальные коэффициенты
    inv = 1 # xi-1
    x0 = 0 # xi

    while a > 1:
        # Делим предыдущий остаток на текущий остаток
        quotient = a // b
        b, a = a % b, b
        # Находим коэффициенты x и y
        # xi+1 = xi-1 - q*xi
        inv, x0 = x0, inv - quotient * x0

    if inv < 0:
        inv += original_b

    return inv


import secrets


# 00 02 [random non-zero bytes] 00 [original data]
# PKCS #1 v1.5
def extend(block, target_size):
    # Вычисление длины необходимого отступа
    # Вычитание 3 для включения начальных байтов паддинга и завершающего байта
    padding_length = target_size - len(block) - 3

    # Генерация отступа с помощью безопасных случайных байтов
    padding_start = b'\x00\x02'
    padding_middle = secrets.token_bytes(padding_length)

    # Вычисление длины дополнительного отступа для конца блока
    random_padding_length = target_size - len(block) - len(padding_start) - len(padding_middle) - 1
    padding_end = secrets.token_bytes(random_padding_length)
    assert random_padding_length == 0
    # Добавление отступа в начало и конец блока
    padded_block = padding_start + padding_middle + b'\x00' + block + padding_end

    return padded_block


def remove_extend(block):
    # Находим индекс последнего байта 0x00 перед паддингом
    padding_end_index = block.rfind(b'\x00')
    if padding_end_index == -1:
        raise ValueError("Decryption error: Invalid padding.")
    # Удаляем паддинг, включая последний байт 0x00, и возвращаем оставшуюся часть сообщения
    return block[padding_end_index + 1:]


def encrypt(plain_text, public_key):
    e, n = public_key
    m = (n.bit_length() + 7) // 8  # Длина n в байтах
    block_size = m - 11  # Размер блока на 11 байт меньше длины n для учета padding и заполнения
    encrypted_blocks = []

    for i in range(0, len(plain_text), block_size):
        block = plain_text[i:i + block_size]

        padded_block = extend(block, m)

        h = int.from_bytes(padded_block, 'big')

        # Шифруем число message^e mod n
        encrypted_block = fast_pow(h, e, n)

        encrypted_block_bytes = encrypted_block.to_bytes(m, 'big')

        encrypted_blocks.append(encrypted_block_bytes)

    encrypted_message = b''.join(encrypted_blocks)
    return encrypted_message


def decrypt(ciphertext, private_key):
    d, n = private_key
    m = (n.bit_length() + 7) // 8  # Длина n в байтах
    block_size = m
    decrypted_message = b''

    for i in range(0, len(ciphertext), block_size):
        encrypted_block = ciphertext[i:i + block_size]

        encrypted_int = int.from_bytes(encrypted_block, 'big')

        # message ^ d mod n
        decrypted_block_int = fast_pow(encrypted_int, d, n)

        decrypted_block_bytes = decrypted_block_int.to_bytes(m, 'big')

        unpadded_block = remove_extend(decrypted_block_bytes)

        decrypted_message += unpadded_block

    return decrypted_message
