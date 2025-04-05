"""
Модуль time_test предназначен для тестирования функций измерения времени выполнения запросов и генерации данных в базе данных.

Функции в модуле:

1. test_measure_query_time_insert():
   Проверяет функцию measure_query_time_insert(), которая измеряет время выполнения вставки данных в таблицу базы данных.

2. test_measure_select_delete_query_time():
   Тестирует функцию measure_select_delete_query_time(), которая измеряет время выполнения выборки и удаления данных из таблицы базы данных.

3. test_measure_generation_time():
   Проверяет функцию measure_generation_time(), которая измеряет время генерации данных для заданного класса ExampleEntry.

Каждая функция тестирования временную таблицу 'test_table' для проведения тестов.

Функции выводят сообщения о результате выполнения тестов ("test_measure_query_time_insert passed.",
"test_measure_select_delete_query_time passed.", "test_measure_generation_time passed.") в случае успешного прохождения.

"""


import random
import string
from investigations.time import measure_query_time_insert, measure_select_delete_query_time, measure_generation_time
from lib.connection import DatabaseConnection


class ExampleEntry:
    """
        Пример класса, используемого для генерации данных и тестирования функций времени.
    """
    def __init__(self, identifier, field1, field2):
        self.identifier = identifier
        self.field1 = field1
        self.field2 = field2

    @classmethod
    def generate(cls, n):
        """
            Генерирует список объектов ExampleEntry случайным образом.

            Args:
                n (int): Количество объектов для генерации.

            Returns:
                list: Список объектов ExampleEntry.
        """
        entries = []
        for _ in range(n):
            identifier = random.randint(1, 10000)
            field1 = ''.join(random.choices(string.ascii_letters, k=10))
            field2 = ''.join(random.choices(string.ascii_letters, k=10))
            entries.append(cls(identifier, field1, field2))
        return entries

# Тесты функций
def test_measure_query_time_insert():
    """
        Проверяет функцию measure_query_time_insert().

        Создает временную таблицу 'test_table' в базе данных 'sandbox_mydb', вставляет случайные данные,
         измеряет время выполнения вставки и проверяет количество вставленных строк.

        Prints:
            Сообщение "test_measure_query_time_insert passed." при успешном прохождении теста.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS test_table (identifier INT PRIMARY KEY, field1 VARCHAR(255), field2 VARCHAR(255));"
        )

        data = [
            (random.randint(1, 10000), ''.join(random.choices(string.ascii_letters, k=10)), ''.join(random.choices(string.ascii_letters, k=10)))
            for _ in range(10)
        ]
        query = "INSERT INTO test_table (identifier, field1, field2) VALUES (%s, %s, %s)"

        execution_time = measure_query_time_insert(query, data, cursor, connection)
        print(f"Insert query execution time: {execution_time:.6f} seconds")

        cursor.execute("SELECT COUNT(*) FROM test_table")
        count = cursor.fetchone()[0]
        assert count == len(data), f"Expected {len(data)} rows, but got {count}"

        cursor.execute("DROP TABLE IF EXISTS test_table;")
        print("test_measure_query_time_insert passed.")

def test_measure_select_delete_query_time():
    """
        Проверяет функцию measure_select_delete_query_time().

        Создает временную таблицу 'test_table' в базе данных 'sandbox_mydb', вставляет данные, измеряет время выполнения
         выборки и удаления данных и проверяет результаты выполнения операций.

        Prints:
            Сообщение "test_measure_select_delete_query_time passed." при успешном прохождении теста.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS test_table (identifier INT PRIMARY KEY, field1 VARCHAR(255), field2 VARCHAR(255));"
        )

        data = [
            (random.randint(1, 10000), ''.join(random.choices(string.ascii_letters, k=10)), ''.join(random.choices(string.ascii_letters, k=10)))
            for _ in range(10)
        ]
        query = "INSERT INTO test_table (identifier, field1, field2) VALUES (%s, %s, %s)"
        cursor.executemany(query, data)
        connection.commit()

        select_query = "SELECT * FROM test_table"
        execution_time = measure_select_delete_query_time(select_query, cursor)
        print(f"Select query execution time: {execution_time:.6f} seconds")

        delete_query = "DELETE FROM test_table"
        execution_time = measure_select_delete_query_time(delete_query, cursor)
        print(f"Delete query execution time: {execution_time:.6f} seconds")

        cursor.execute("DROP TABLE IF EXISTS test_table;")
        print("test_measure_select_delete_query_time passed.")

def test_measure_generation_time():
    """
        Проверяет функцию measure_generation_time().

        Измеряет время генерации данных для класса ExampleEntry.

        Prints:
            Сообщение "test_measure_generation_time passed." при успешном прохождении теста.
    """
    execution_time = measure_generation_time(ExampleEntry, 100)
    print(f"Data generation time for 100 entries: {execution_time:.6f} seconds")
    print("test_measure_generation_time passed.")

# Запуск тестов
test_measure_query_time_insert()
test_measure_select_delete_query_time()
test_measure_generation_time()

print("All tests passed.")
