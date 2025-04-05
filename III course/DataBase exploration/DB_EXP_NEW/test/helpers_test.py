"""
Модуль helpers_test предназначен для тестирования функций вспомогательных функий.

Класс ExampleEntry представляет собой пример структуры данных, содержащей идентификатор и два поля (field1 и field2).
Вспомогательные функции в модуле работают с данными этого типа.

Функции тестирования:
- test_get_identifiers(): Проверяет функцию get_identifiers(), которая извлекает идентификаторы из списка объектов ExampleEntry.
- test_fetch_existing_pks(): Тестирует функцию fetch_existing_pks(),
которая извлекает существующие первичные ключи из таблицы в базе данных.
- test_ensure_unique_identifiers(): Проверяет функцию ensure_unique_identifiers(), которая гарантирует уникальность
идентификаторов при вставке данных в базу данных.
- test_format_data(): Тестирует функцию format_data(), которая форматирует данные для вставки в SQL запрос.


Функции выводят сообщения о результате выполнения тестов ("test_get_identifiers passed.", "test_fetch_existing_pks passed.", "test_ensure_unique_identifiers passed.", "test_format_data passed.") в случае успешного прохождения.

"""

import random
import string

from lib.connection import DatabaseConnection
from lib.helpers import get_identifiers, fetch_existing_pks, ensure_unique_identifiers, format_data


class ExampleEntry:
    """
        Пример структуры данных для тестирования вспомогательных функций.

        Attributes:
            identifier (int): Уникальный идентификатор.
            field1 (str): Первое поле данных.
            field2 (str): Второе поле данных.
    """
    def __init__(self, identifier, field1, field2):
        self.identifier = identifier
        self.field1 = field1
        self.field2 = field2

    @classmethod
    def generate(cls, n):
        """
            Генерирует список объектов ExampleEntry.

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
def test_get_identifiers():
    """
        Проверяет функцию get_identifiers().

        Извлекает идентификаторы из списка объектов ExampleEntry и сравнивает с ожидаемым результатом.

        Prints:
            Сообщение "test_get_identifiers passed." при успешном прохождении теста.
    """
    data = [ExampleEntry(i, 'field1', 'field2') for i in range(10)]
    identifiers = get_identifiers(data, 'identifier')
    assert identifiers == list(range(10)), f"Expected {list(range(10))}, but got {identifiers}"
    print("test_get_identifiers passed.")

def test_fetch_existing_pks():
    """
        Тестирует функцию fetch_existing_pks().

        Создает временную таблицу в базе данных, вставляет данные, извлекает существующие первичные ключи и сравнивает с ожидаемым результатом.

        Prints:
            Сообщение "test_fetch_existing_pks passed." при успешном прохождении теста.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (identifier INT PRIMARY KEY, field1 VARCHAR(255), field2 VARCHAR(255));")
        cursor.execute("INSERT INTO test_table (identifier, field1, field2) VALUES (1, 'a', 'b');")
        existing_pks = fetch_existing_pks(cursor, 'test_table', 'identifier')
        assert existing_pks == {1}, f"Expected {{1}}, but got {existing_pks}"
        cursor.execute("DROP TABLE IF EXISTS test_table;")
        print("test_fetch_existing_pks passed.")

def test_ensure_unique_identifiers():
    """
        Проверяет функцию ensure_unique_identifiers().

        Создает временную таблицу в базе данных, вставляет данные с возможным конфликтом идентификаторов, проверяет уникальность идентификаторов их исходного списка.

        Prints:
            Сообщение "test_ensure_unique_identifiers passed." при успешном прохождении теста.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute("CREATE TABLE IF NOT EXISTS test_table (identifier INT PRIMARY KEY, field1 VARCHAR(255), field2 VARCHAR(255));")
        cursor.execute("INSERT INTO test_table (identifier, field1, field2) VALUES (1, 'a', 'b');")
        data = [ExampleEntry(1, 'field1', 'field2'), ExampleEntry(2, 'field1', 'field2')]
        unique_data = ensure_unique_identifiers(data, 'identifier', 'test_table', cursor, ExampleEntry)
        unique_identifiers = get_identifiers(unique_data, 'identifier')
        assert len(set(unique_identifiers)) == len(unique_identifiers), "Identifiers are not unique."
        cursor.execute("DROP TABLE IF EXISTS test_table;")
        print("test_ensure_unique_identifiers passed.")

def test_format_data():
    """
        Тестирует функцию format_data().

        Форматирует данные из списка объектов ExampleEntry для вставки в SQL запрос и сравнивает с ожидаемым результатом.

        Prints:
            Сообщение "test_format_data passed." при успешном прохождении теста.
    """
    data = [ExampleEntry(i, 'field1', 'field2') for i in range(10)]
    query = "INSERT INTO test_table (identifier, field1, field2) VALUES (%s, %s, %s)"
    formatted = format_data(data, query)
    expected = [(i, 'field1', 'field2') for i in range(10)]
    assert formatted == expected, f"Expected {expected}, but got {formatted}"
    print("test_format_data passed.")

# Запуск тестов
test_get_identifiers()
test_fetch_existing_pks()
test_ensure_unique_identifiers()
test_format_data()

print("All tests passed.")
