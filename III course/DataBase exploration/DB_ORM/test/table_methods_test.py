import mysql.connector

from lib.table_methods import get_tables, get_columns, delete_record, insert_record, replace_record, \
    replace_all_records, delete_all_records

# Подготовим данные для подключения к базе данных
host = "localhost"
user = "root"
password = "root"
selected_db = "aboba3"

try:
    # Открываем соединение с базой данных
    with mysql.connector.connect(host=host, user=user, password=password, database=selected_db) as connection:
        # Тест get_tables
        tables = get_tables(connection)
        print("Tables in the database:")
        for table in tables:
            print(table)

        # Тест get_columns
        selected_table = "qemqme"
        columns = get_columns(connection, selected_table)
        print(f"Columns in table {selected_table}:")
        for column in columns:
            print(column)

        # Тест insert_record
        print("Тест вставки записи\n")
        insert_record(selected_db, host, user, password)

        # Тест replace_record
        print("Тест замены записи\n")
        replace_record(selected_db, host, user, password)

        # Тест replace_all_records
        print("Тест замены всех записей\n")
        replace_all_records(selected_db, host, user, password)

        # Тест delete_all_records
        print("Тест удаления всех записей\n")
        delete_all_records(selected_db, host, user, password)


except mysql.connector.Error as err:
    print("Error:", err)
