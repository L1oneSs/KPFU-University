# Протестировать создание песочницы
from lib.database_methods import create_sandbox_database
from lib.db_connection import DatabaseConnection
import mysql.connector

try:
    # Подключаемся к базе данных
    with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (mycursor, connection):
        # Проверяем, что соединение успешно установлено
        if connection.is_connected():
            print("Соединение с базой данных успешно установлено.")

        # Здесь можно выполнять операции с базой данных, включая создание песочницы
        create_sandbox_database(host="localhost", user="root", password="root")

except mysql.connector.Error as err:
    print("Ошибка:", err)
