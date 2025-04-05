import socket
import pickle
from rsa import encrypt

AdressFamily = socket.AF_INET
SocketKind = socket.SOCK_STREAM
# Создаем клиентский сокет
client_socket = socket.socket(AdressFamily, SocketKind)
client_socket.connect(('localhost', 11111))

public_key = pickle.loads(client_socket.recv(4096))

while True:

    message = input("Enter your message (type 'exit' to quit): ").encode()

    if message.lower() == b'exit':
        break

    # Шифруем сообщение и отправляем его серверу
    encrypted_blocks = encrypt(message, public_key)
    client_socket.send(pickle.dumps(encrypted_blocks))

client_socket.close()