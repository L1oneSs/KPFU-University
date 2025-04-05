import socket
import secrets
import math

def miller_rabin(n, k):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0:
        return False

    # Выразим n - 1 как 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = secrets.randbelow(n - 2) + 2
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime(bits):
    while True:
        p = secrets.randbits(bits)
        if miller_rabin(p, 40):
            return p

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(e, phi):
    d, x1, x2 = 0, 0, 1
    temp_phi = phi

    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - temp1 * e
        temp_phi = e
        e = temp2

        x = x2 - temp1 * x1
        y = d - temp1 * y
        x2 = x1
        x1 = x
        d = y

    if temp_phi == 1:
        return x2 + phi

def block_encrypt(text, e, n):
    m = len(bin(n)[2:]) // 8  # Размер блока в байтах
    encrypted_blocks = []

    for block in text:
        # Преобразуем блок в число
        m_block = int.from_bytes(block, byteorder='big')

        # Добавляем случайный байт в начало блока
        padded_block = secrets.randbits(8).to_bytes(1, byteorder='big') + block

        # Преобразуем блок в число h
        h = int.from_bytes(padded_block, byteorder='big')

        # Шифруем h с помощью RSA
        encrypted = pow(h, e, n)

        # Преобразуем зашифрованное число в байты длиной m
        encrypted_block = encrypted.to_bytes(m, byteorder='big')

        encrypted_blocks.append(encrypted_block)

    return encrypted_blocks

def block_decrypt(blocks, d, n):
    decrypted_text = []

    for block in blocks:
        # Расшифровываем блок
        decrypted = pow(int.from_bytes(block, byteorder='big'), d, n)

        # Удаляем случайный байт из начала блока
        unpadded_decrypted = (decrypted >> 8).to_bytes(len(block) - 1, byteorder='big')

        decrypted_text.append(unpadded_decrypted)

    return decrypted_text

def server():
    host = "127.0.0.1"
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)

    while True:
        conn, addr = s.accept()

        # Генерация ключей RSA
        p = generate_prime(512)
        q = generate_prime(512)
        n = p * q
        phi = (p - 1) * (q - 1)
        e = 65537  # Обычно используется простое число e, например, 65537
        d = mod_inverse(e, phi)

        # Отправка открытого ключа клиенту
        conn.sendall(n.to_bytes(128, byteorder='big'))
        conn.sendall(e.to_bytes(128, byteorder='big'))

        # Получение зашифрованного сообщения от клиента
        encrypted_message = conn.recv(4096)
        decrypted_blocks = block_decrypt([encrypted_message], d, n)
        decrypted_message = b''.join(decrypted_blocks).decode('utf-8')
        print("Получено от клиента:", decrypted_message)

        conn.close()


def client():
    host = "127.0.0.1"
    port = 12345

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    # Получение открытого ключа от сервера
    n_bytes = s.recv(128)
    e_bytes = s.recv(128)
    n = int.from_bytes(n_bytes, byteorder='big')
    e = int.from_bytes(e_bytes, byteorder='big')

    # Отправка зашифрованного сообщения серверу
    message = "Привет, сервер! Это зашифрованное сообщение."
    message_bytes = message.encode('utf-8')
    encrypted_blocks = block_encrypt([message_bytes], e, n)
    for block in encrypted_blocks:
        s.sendall(block)

    s.close()


import threading

if __name__ == "__main__":
    server_thread = threading.Thread(target=server)
    server_thread.start()

    # Здесь можно добавить какую-то задержку, чтобы убедиться, что сервер успел запуститься
    # например, time.sleep(1)

    client()


