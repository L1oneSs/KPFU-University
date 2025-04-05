import mysql.connector
from lib.main import (
    get_table_names, generate_entries, create_sandbox_database,
    replace_all_data, delete_all_data, create_table_entry
)

def connect_to_db():
    return mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")

# Функция для проверки наличия записей в таблице
def check_table_entries(table_name, mycursor):
    mycursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = mycursor.fetchone()[0]
    return count

def test_get_table_names():
    connection = connect_to_db()
    mycursor = connection.cursor()

    try:
        table_names = get_table_names(mycursor)
        assert isinstance(table_names, list), "Результат должен быть списком"
        assert all(isinstance(name, str) for name in table_names), "Все имена таблиц должны быть строками"
        print("Тест get_table_names прошел успешно.")
    except Exception as e:
        print(f"Тест get_table_names провален: {e}")
    finally:
        mycursor.close()
        connection.close()

test_get_table_names()

def test_create_sandbox_database():
    connection = connect_to_db()
    mycursor = connection.cursor()

    try:
        create_sandbox_database(mycursor)

        mycursor.execute("SHOW DATABASES")
        databases = [db[0] for db in mycursor.fetchall()]
        assert "sandbox_mydb" in databases, "База данных sandbox_mydb должна существовать"

        mycursor.execute("USE sandbox_mydb")
        mycursor.execute("SHOW TABLES")
        sandbox_tables = [table[0] for table in mycursor.fetchall()]

        mycursor.execute("USE mydb")
        original_tables = get_table_names(mycursor)

        assert set(sandbox_tables) == set(original_tables), "Все таблицы должны быть скопированы в песочницу"
        print("Тест create_sandbox_database прошел успешно.")
    except Exception as e:
        print(f"Тест create_sandbox_database провален: {e}")
    finally:
        mycursor.close()
        connection.close()

test_create_sandbox_database()


def test_replace_all_data():
    connection = connect_to_db()
    mycursor = connection.cursor()

    try:
        tables = get_table_names(mycursor)
        for table in tables:
            initial_count = check_table_entries(table, mycursor)
            replace_all_data(table)

            new_count = check_table_entries(table, mycursor)
            assert new_count == initial_count, f"Количество записей в таблице '{table}' должно быть таким же"
            print(f"Тест replace_all_data для таблицы '{table}' прошел успешно.")
    except Exception as e:
        print(f"Тест replace_all_data провален: {e}")
    finally:
        mycursor.close()
        connection.close()

test_replace_all_data()

"""
def test_delete_all_data():
    connection = connect_to_db()
    mycursor = connection.cursor()

    try:
        tables = get_table_names(mycursor)
        for table in tables:
            delete_all_data(table)
            new_count = check_table_entries(table, mycursor)
            assert new_count == 0, f"Все записи в таблице '{table}' должны быть удалены"
            print(f"Тест delete_all_data для таблицы '{table}' прошел успешно.")
    except Exception as e:
        print(f"Тест delete_all_data провален: {e}")
    finally:
        mycursor.close()
        connection.close()

test_delete_all_data()
"""

