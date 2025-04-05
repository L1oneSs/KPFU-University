import mysql.connector
import timeit

from investigations.graphics import graph_info
from investigations.query_time import query_time_custom, query_time_insert, query_time_select

# Предположим, у вас есть соответствующие переменные для подключения к базе данных
host = "localhost"
user = "root"
password = "root"
database = "aboba3"

# Создаем соединение с базой данных и курсор
connection = mysql.connector.connect(host=host, user=user, password=password, database=database)
mycursor = connection.cursor()


def test_query_time_custom():
    custom_query = "SELECT * FROM qemqme"
    first_word = "SELECT"
    row_count = 100  # Предположим, что таблица содержит 100 записей

    # Замеряем время выполнения пользовательского запроса
    time_taken = query_time_custom(mycursor, connection, custom_query, first_word, row_count)

    assert graph_info[0][0] == first_word
    assert graph_info[0][1] == row_count
    assert isinstance(graph_info[0][2], float)

def test_query_time_select():
    query = "SELECT * FROM qemqme"
    row_count = 100  # Предположим, что таблица содержит 100 записей

    # Замеряем время выполнения запроса на выборку данных
    time_taken = query_time_select(mycursor, connection, query, row_count)

    # Удостоверяемся, что время выполнения запроса записывается корректно в глобальный список
    assert graph_info[0][0] == "SELECT"
    assert graph_info[0][1] == row_count
    assert isinstance(graph_info[0][2], float)


# Выполнение ручных тестов
test_query_time_custom()
test_query_time_select()

# Закрываем соединение с базой данных
mycursor.close()
connection.close()
