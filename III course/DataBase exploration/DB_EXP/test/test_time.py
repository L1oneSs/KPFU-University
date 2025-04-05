import mysql.connector
from lib.creator import create_table_entry
from lib.main import (
    query_time_generate, query_time_custom, query_time_select,
    query_time_insert, query_time_delete
)

def connect_to_db():
    return mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")

def check_table_entries(table_name, mycursor):
    mycursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = mycursor.fetchone()[0]
    return count


def test_query_time_generate():
    connection = connect_to_db()
    mycursor = connection.cursor()
    table_name = "airport"
    num_entries = 1

    try:
        initial_count = check_table_entries(table_name, mycursor)
        time_taken = query_time_generate(table_name, num_entries, mycursor, connection)
        new_count = check_table_entries(table_name, mycursor)

        assert new_count == initial_count + num_entries, f"Ожидалось {initial_count + num_entries} записей в таблице '{table_name}', но получено {new_count}"
        assert time_taken > 0, "Время выполнения должно быть положительным"

        print(f"Тест query_time_generate прошел успешно за {time_taken:.4f} секунд.")
    except Exception as e:
        print(f"Тест query_time_generate провален: {e}")
    finally:
        mycursor.close()
        connection.close()


test_query_time_generate()


def test_query_time_custom():
    connection = connect_to_db()
    mycursor = connection.cursor()
    custom_query = "SELECT * FROM airport"
    first_word = "SELECT"
    table_name = "airport"

    try:
        row_count = check_table_entries(table_name, mycursor)
        time_taken = query_time_custom(mycursor, connection, custom_query, first_word, row_count)

        assert time_taken > 0, "Время выполнения должно быть положительным"

        print(f"Тест query_time_custom прошел успешно за {time_taken:.4f} секунд.")
    except Exception as e:
        print(f"Тест query_time_custom провален: {e}")
    finally:
        mycursor.close()
        connection.close()


test_query_time_custom()


def test_query_time_select():
    connection = connect_to_db()
    mycursor = connection.cursor()
    query = "SELECT * FROM airport"
    table_name = "airport"

    try:
        row_count = check_table_entries(table_name, mycursor)
        time_taken = query_time_select(mycursor, connection, query, row_count)

        assert time_taken > 0, "Время выполнения должно быть положительным"

        print(f"Тест query_time_select прошел успешно за {time_taken:.4f} секунд.")
    except Exception as e:
        print(f"Тест query_time_select провален: {e}")
    finally:
        mycursor.close()
        connection.close()


test_query_time_select()




