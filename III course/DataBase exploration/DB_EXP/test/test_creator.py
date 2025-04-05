# Подключение к базе данных
import mysql.connector

from lib.creator import create_table_entry

connection = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
mycursor = connection.cursor()


# Функция для проверки наличия записей в таблице
def check_table_entries(table_name, mycursor):
    mycursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = mycursor.fetchone()[0]
    return count


def test_create_table_entry():
    tables = [
        "airlines",
        "airport",
        "airportstaff",
        "baggage",
        "flights",
        "passengers",
        "securitycheck",
        "tickets"
    ]

    for table in tables:
        # Сначала получаем количество записей в таблице
        initial_count = check_table_entries(table, mycursor)

        # Создаем 10 новых записей
        create_table_entry(table, 10, mycursor)

        # Проверяем количество записей после добавления
        new_count = check_table_entries(table, mycursor)

        # Проверяем, что количество записей увеличилось на 10
        assert new_count == initial_count + 10, f"Ошибка: Ожидалось {initial_count + 10} записей в таблице '{table}', но получено {new_count}"


# Выполнение теста
test_create_table_entry()

# Закрытие соединения с базой данных
mycursor.close()
connection.close()