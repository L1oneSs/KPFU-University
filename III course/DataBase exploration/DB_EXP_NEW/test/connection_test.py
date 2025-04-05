"""
Модуль `connection_test` предоставляет функции для тестирования подключения к базе данных MySQL.

Функции:
- `test_database_connection()`: Проверяет соединение с базой данных `sandbox_mydb`.
"""

import mysql.connector
from mysql.connector import errorcode
from lib.connection import DatabaseConnection

def test_database_connection():
    """
        Проверяет соединение с базой данных MySQL.

        Подключается к базе данных `sandbox_mydb` на локальном хосте, используя
        указанные учетные данные. Выполняет запрос `SELECT DATABASE();` для проверки
        успешности подключения.

        Если подключение прошло успешно и база данных `sandbox_mydb` доступна, функция
        выводит сообщение "Тест пройден: Успешное подключение к базе данных.".

        Raises:
            mysql.connector.Error: Если возникает ошибка MySQL.
            Exception: Если возникает непредвиденная ошибка.
    """
    try:
        with DatabaseConnection(host='localhost', user='root', password='root', database='sandbox_mydb') as (cursor, connection):
            cursor.execute("SELECT DATABASE();")
            result = cursor.fetchone()
            if result and result[0] == 'sandbox_mydb':
                print("Тест пройден: Успешное подключение к базе данных.")
            else:
                print("Тест не пройден: Не удалось подключиться к базе данных.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Тест не пройден: Неверное имя пользователя или пароль.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Тест не пройден: База данных не существует.")
        else:
            print(f"Тест не пройден: Произошла ошибка: {err}")
    except Exception as e:
        print(f"Тест не пройден: Произошла непредвиденная ошибка: {e}")

# Запускаем тест
test_database_connection()
