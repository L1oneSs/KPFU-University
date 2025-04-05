"""
Модуль time предоставляет функции для измерения времени выполнения различных операций с базой данных и генерацией данных.
Включает функции для измерения времени вставки данных, выполнения запросов на выборку и удаление, а также времени генерации данных.

Функции:
- measure_query_time_insert(query, data, cursor, conn): Измеряет время выполнения запроса на вставку данных.
- measure_select_delete_query_time(query, cursor): Измеряет время выполнения запроса на выборку или удаление данных.
- measure_generation_time(table_class, size): Измеряет время генерации данных.
"""

import timeit

def measure_query_time_insert(query, data, cursor, conn):
    """
        Измеряет время выполнения запроса на вставку данных.

        Параметры
        ----------
        query : str
            SQL-запрос на вставку данных.
        data : list
            Список данных для вставки.
        cursor : mysql.connector.cursor.MySQLCursor
            Курсор для выполнения операций с базой данных.
        conn : mysql.connector.connection.MySQLConnection
            Соединение с базой данных.

        Возвращает
        ----------
        float
            Время выполнения запроса в секундах.
    """
    import timeit

    def execute_query():
        cursor.executemany(query, data)
        conn.commit()

    timer = timeit.Timer(execute_query)
    number = 1
    execution_time = timer.timeit(number=number)
    return execution_time

def measure_select_delete_query_time(query, cursor):
    """
        Измеряет время выполнения запроса на выборку или удаление данных.

        Параметры
        ----------
        query : str
            SQL-запрос на выборку или удаление данных.
        cursor : mysql.connector.cursor.MySQLCursor
            Курсор для выполнения операций с базой данных.

        Возвращает
        ----------
        float
            Время выполнения запроса в секундах.
    """
    import timeit

    def execute_query():
        cursor.execute(query)
        cursor.fetchall()

    timer = timeit.Timer(execute_query)
    number = 1
    execution_time = timer.timeit(number=number)
    return execution_time

import timeit

def measure_generation_time(table_class, size):
    """
        Измеряет время генерации данных.

        Параметры
        ----------
        table_class : class
            Класс модели таблицы.
        size : int
            Количество генерируемых записей.

        Возвращает
        ----------
        float
            Время генерации данных в секундах   .
    """
    class_name = table_class.__name__
    module_name = table_class.__module__
    stmt = f"list({class_name}.generate({size}))"
    setup = f"from {module_name} import {class_name}"
    timer = timeit.Timer(stmt, setup=setup)
    time = timer.timeit(number=1)
    return time

