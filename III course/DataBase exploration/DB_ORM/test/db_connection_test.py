import mysql.connector

from lib.db_connection import DatabaseConnection

try:
    # Открываем соединение с базой данных с использованием контекстного менеджера
    with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (cursor, connection):
        # Проверяем, что соединение успешно открыто
        if connection.is_connected():
            print("Соединение с базой данных успешно установлено.")

        # Здесь можно выполнять операции с базой данных

    # После завершения блока контекстного менеджера соединение будет автоматически закрыто

except mysql.connector.Error as err:
    print("Ошибка:", err)
