"""
Модуль db_methods предоставляет функции для резервного копирования и восстановления базы данных MySQL.
"""

from lib.connection import DatabaseConnection
from lib.table_methods import get_table_names, delete_all_data
import mysql.connector


def backup_database(host, user, password, database, backup_file):
    """
        Создает бэкап базы данных MySQL и сохраняет его в файл.

        Параметры
        ----------
        host : str
            Хост базы данных.
        user : str
            Имя пользователя базы данных.
        password : str
            Пароль пользователя базы данных.
        database : str
            Название базы данных.
        backup_file : str
            Путь к файлу, в который будет сохранен бэкап.

        Исключения
        ----------
        mysql.connector.Error
            Если произошла ошибка при подключении к базе данных или выполнении SQL-запросов.
    """
    try:
        with open(backup_file, 'w') as file, DatabaseConnection(host, user, password, database) as (_, connection):
            cursor = connection.cursor()
            file.write(f"DATABASE: {database}\n")
            tables = get_table_names(cursor)
            for table_name in tables:
                file.write(f"TABLE: {table_name}\n")
                cursor.execute(f"SELECT * FROM {table_name}")
                for row in cursor.fetchall():
                    file.write(','.join(map(str, row)) + '\n')
            print(f"Бэкап базы данных '{database}' успешно создан в файле '{backup_file}'.")
    except mysql.connector.Error as e:
        print(f"Ошибка при создании бэкапа базы данных: {e}")


def restore_database(host, user, password, database, backup_file):
    """
        Восстанавливает базу данных MySQL из файла бэкапа и сохраняет все данные.

        Параметры
        ----------
        host : str
            Хост базы данных.
        user : str
            Имя пользователя базы данных.
        password : str
            Пароль пользователя базы данных.
        database : str
            Название базы данных.
        backup_file : str
            Путь к файлу бэкапа.

        Исключения
        ----------
        mysql.connector.Error
            Если произошла ошибка при подключении к базе данных или выполнении SQL-запросов.
    """
    try:
        with open(backup_file, 'r') as file, DatabaseConnection(host, user, password, database) as (_, connection):
            cursor = connection.cursor()
            first_line = file.readline()
            if not first_line.startswith("DATABASE: "):
                print("Ошибка: Несоответствие названия базы данных в файле бэкапа.")
                return

            backup_database_name = first_line.strip().split("DATABASE: ")[1]
            if backup_database_name != database:
                print("Ошибка: Несоответствие названия базы данных в файле бэкапа и переданной базы данных.")
                return

            current_table = None
            for line in file:
                if line.startswith("TABLE: "):
                    current_table = line.strip().split("TABLE: ")[1]
                    delete_all_data(cursor, current_table)
                else:
                    if current_table:
                        cursor.execute(f"SELECT * FROM {current_table} LIMIT 1")
                        columns = [column[0] for column in cursor.description]
                        columns_str = ', '.join(columns)
                        values = line.strip().split(",")
                        values_str = ', '.join([f'"{value}"' for value in values])
                        cursor.fetchall()
                        cursor.execute(f"INSERT INTO {current_table} ({columns_str}) VALUES ({values_str})")
            print(f"База данных '{database}' успешно восстановлена из файла '{backup_file}'.")
    except mysql.connector.Error as e:
        print(f"Ошибка при восстановлении базы данных: {e}")