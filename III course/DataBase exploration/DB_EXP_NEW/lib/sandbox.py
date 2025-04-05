"""
Модуль sandbox предоставляет функции для создания копии базы данных MySQL.
"""

from lib.connection import DatabaseConnection
from lib.table_methods import get_table_names, get_table_columns
import mysql.connector


def create_table_sandbox(table_name, columns):
    """
        Создает SQL-запрос для создания таблицы в песочнице.

        Параметры
        ----------
        table_name : str
            Название таблицы.
        columns : list
            Список столбцов таблицы, каждый столбец представлен в виде кортежа (имя, тип, nullable, ключ, default).

        Возвращает
        ----------
        str
            SQL-запрос для создания таблицы.
    """
    columns_definitions = []
    for column in columns:
        column_definition = f"{column[0]} {column[1]}"
        if column[2] == "NO":
            column_definition += " NOT NULL"
        if column[4] is not None:
            column_definition += f" DEFAULT {column[4]}"
        if column[5] == "auto_increment":
            column_definition += " AUTO_INCREMENT"
        if column[3] == "PRI":
            column_definition += " PRIMARY KEY"
        columns_definitions.append(column_definition)
    create_table_statement = f"CREATE TABLE {table_name} ({', '.join(columns_definitions)});"
    return create_table_statement


def create_sandbox():
    """
       Создает песочницу базы данных MySQL, копируя структуру таблиц из базы данных 'mydb'.

       Песочница создается как новая база данных с названием 'sandbox_mydb'.
       Все таблицы из базы данных 'mydb' будут созданы в песочнице с той же структурой.

       Исключения
       ----------
       mysql.connector.Error
           Если произошла ошибка при подключении к базе данных или выполнении SQL-запросов.
   """
    sandbox_db_name = 'sandbox_mydb'
    try:
        with DatabaseConnection('localhost', 'root', 'root', '') as (cursor, connection):
            cursor.execute(f"DROP DATABASE IF EXISTS {sandbox_db_name}")
            cursor.execute(f"CREATE DATABASE {sandbox_db_name}")
            #print(f"Песочница '{sandbox_db_name}' успешно создана.")

        with DatabaseConnection('localhost', 'root', 'root', 'mydb') as (cursor, connection):
            table_names = get_table_names(cursor)
            tables = []
            for table_name in table_names:
                columns = get_table_columns(cursor, table_name)
                create_table_statement = create_table_sandbox(table_name, columns)
                tables.append(create_table_statement)

        with DatabaseConnection('localhost', 'root', 'root', sandbox_db_name) as (cursor, connection):
            for create_table_statement in tables:
                cursor.execute(create_table_statement)
            #print("Таблицы успешно созданы в песочнице.")

    except mysql.connector.Error as e:
        print(f"Ошибка при создании песочницы: {e}")