"""
Модуль table_methods_test предназначен для тестирования функций работы с таблицами базы данных, используя различные методы из модуля lib.table_methods.

Функции в модуле:

1. test_get_table_columns():
   Тестирует функцию get_table_columns(), которая извлекает имена столбцов из указанной таблицы базы данных.

2. test_get_table_names():
   Проверяет функцию get_table_names(), которая возвращает список имен таблиц в текущей базе данных.

3. test_delete_all_data():
   Тестирует функцию delete_all_data(), которая удаляет все данные из указанной таблицы базы данных.

Каждая функция тестирования создает временную таблицу 'test_table' для проведения тестов.

Функции выводят сообщения о результате выполнения тестов ("test_get_table_columns passed.", "test_get_table_names passed.", "test_delete_all_data passed.") в случае успешного прохождения.

"""

from lib.connection import DatabaseConnection
from lib.table_methods import get_table_columns, get_table_names, delete_all_data

def test_get_table_columns():
    """
        Проверяет функцию get_table_columns().

        Создает временную таблицу 'test_table' в базе данных 'sandbox_mydb', извлекает имена столбцов с помощью функции get_table_columns() и сравнивает с ожидаемым результатом.

        Prints:
            Сообщение "test_get_table_columns passed." при успешном прохождении теста.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age INT);")

        columns = get_table_columns(cursor, 'test_table')
        column_names = [col[0] for col in columns]

        expected_columns = ['id', 'name', 'age']
        assert column_names == expected_columns, f"Expected columns {expected_columns}, but got {column_names}"

        cursor.execute("DROP TABLE IF EXISTS test_table;")
        print("test_get_table_columns passed.")


def test_get_table_names():
    """
        Проверяет функцию get_table_names().

        Создает временную таблицу 'test_table' в базе данных 'sandbox_mydb', вызывает функцию get_table_names() и проверяет наличие 'test_table' в полученном списке имен таблиц.

        Prints:
            Сообщение "test_get_table_names passed." при успешном прохождении теста.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age INT);")
        table_names = get_table_names(cursor)

        assert 'test_table' in table_names, "Expected 'test_table' in table names"

        print("test_get_table_names passed.")

def test_delete_all_data():
    """
        Проверяет функцию delete_all_data().

        Создает временную таблицу 'test_table' в базе данных 'sandbox_mydb', вставляет данные, удаляет все данные с помощью функции delete_all_data() и проверяет, что после удаления количество строк равно 0.

        Prints:
            Сообщение "test_delete_all_data passed." при успешном прохождении теста.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(255), age INT);")
        cursor.execute("INSERT INTO test_table (name, age) VALUES ('Alice', 30), ('Bob', 25);")

        delete_all_data(cursor, 'test_table')

        cursor.execute("SELECT COUNT(*) FROM test_table")
        count = cursor.fetchone()[0]
        assert count == 0, f"Expected 0 rows after deletion, but got {count}"

        cursor.execute("DROP TABLE IF EXISTS test_table;")
        print("test_delete_all_data passed.")


test_get_table_columns()
test_get_table_names()
test_delete_all_data()
print("All tests passed.")