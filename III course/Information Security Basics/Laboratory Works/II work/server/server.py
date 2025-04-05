import socket
import pickle
from rsa import generate_keypair, decrypt

AdressFamily = socket.AF_INET
SocketKind = socket.SOCK_STREAM

# Создаем серверный сокет (IPv4 и протокол TCP)
server_socket = socket.socket(AdressFamily, SocketKind)
# Устанавливаем адрес и порт
server_socket.bind(('localhost', 11111))
# Режим ожидания клиента (1)
server_socket.listen(1)

print("Server is waiting...")

# Генерируем ключи RSA
# Размер ключа
k = 128
public_key, private_key = generate_keypair(k)
method = 'ignore'

while True:
    # Сервер принимает входящее соединение от клиента
    client_socket, _ = server_socket.accept()
    print("Client connected.")

    # Отправляем публичный ключ клиенту
    client_socket.send(pickle.dumps(public_key))

    # Получаем зашифрованное сообщение от клиента
    while True:
        # Получение зашифрованного сообщения от клиента размером до 4096 байт
        encrypted_message = client_socket.recv(4096)
        if not encrypted_message:
            break
        decrypted_message = decrypt(pickle.loads(encrypted_message), private_key)
        print("Received Message from Client:", decrypted_message.decode('utf-8'))

    client_socket.close()
