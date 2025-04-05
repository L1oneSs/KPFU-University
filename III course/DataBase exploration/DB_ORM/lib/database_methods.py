import mysql
from colorama import Fore

import mysql.connector

from investigations.query_time import query_time_generate
from lib.db_connection import DatabaseConnection
from lib.table_methods import create_table, delete_record, insert_record, replace_record, delete_table, \
    replace_all_records, delete_all_records


def create_database(host, user, password):
    """
    Метод для создания новой базы данных.

    Args:
        host (str): Хост базы данных.
        user (str): Пользователь базы данных.
        password (str): Пароль пользователя базы данных.

    Returns:
        None

    Raises:
        mysql.connector.Error: Если возникает ошибка при создании базы данных.

    """
    print("Создание новой базы данных:")
    database_name = input("Введите название базы данных: ")
    if database_name.lower() == "back":
        return

    try:
        with DatabaseConnection(host=host, user=user, password=password, database="") as (mycursor, connection):
            mycursor.execute("SHOW DATABASES")
            existing_databases = [row[0] for row in mycursor.fetchall()]
            if database_name in existing_databases:
                print(Fore.RED + f"База данных {database_name} уже существует.")
                print(Fore.RESET)
                return
            else:
                mycursor.execute(f"CREATE DATABASE {database_name}")
                print(Fore.GREEN + f"База данных {database_name} успешно создана.")
                print(Fore.RESET)
                # Подключение к созданной базе данных
                connection.database = database_name

                # Спрашиваем пользователя, хочет ли он создать таблицы
                create_tables = input("Хотите создать таблицы в базе данных? (Да/Нет): ").lower()
                if create_tables == "нет":
                    return

                # Если пользователь согласен создать таблицы, спрашиваем количество
                num_tables = int(input("Введите количество таблиц для создания: "))

                for _ in range(num_tables):
                    res = create_table(database_name, host, user, password)
                    if res == "id":
                        return



    except mysql.connector.Error as err:
        print("Ошибка при создании базы данных:", err.msg)

def delete_database(host, user, password):
    """
    Метод для удаления базы данных.

    Args:
        host (str): Хост базы данных.
        user (str): Пользователь базы данных.
        password (str): Пароль пользователя базы данных.

    Returns:
        None

    Raises:
        IndexError: Если введен некорректный номер базы данных.
        ValueError: Если введен некорректный номер базы данных.
        mysql.connector.Error: Если возникает ошибка при удалении базы данных.

    """
    print("Удаление базы данных:")
    try:
        with DatabaseConnection(host=host, user=user, password=password, database="") as (mycursor, _):
            mycursor.execute("SHOW DATABASES")
            databases = [row[0] for row in mycursor.fetchall() if
                         row[0] not in ['mysql', 'mydb', 'information_schema', 'performance_schema', 'sakila', 'sys',
                                        'world']]
            for idx, db in enumerate(databases, start=1):
                print(f"{idx}. {db}")
            selection = input("Выберите номер базы данных для удаления: ")
            if selection.lower() == "back":
                return
            selected_database = databases[int(selection) - 1]
            mycursor.execute(f"DROP DATABASE {selected_database}")
            print(Fore.GREEN + f"База данных {selected_database} успешно удалена.")
            print(Fore.RESET)
    except (IndexError, ValueError):
        print(Fore.RED + "Ошибка ввода: введен некорректный номер базы данных.")
        print(Fore.RESET)
    except mysql.connector.Error as err:
        print("Ошибка при удалении базы данных:", err.msg)

def edit_database(host, user, password):
    """
    Метод для редактирования базы данных.

    Args:
        host (str): Хост базы данных.
        user (str): Пользователь базы данных.
        password (str): Пароль пользователя базы данных.

    Returns:
        None

    Raises:
        mysql.connector.Error: Если возникает ошибка при редактировании базы данных.

    """
    try:
        with DatabaseConnection(host=host, user=user, password=password, database="mysql") as (mycursor, connection):
            # Выбор базы данных
            mycursor.execute("SHOW DATABASES")
            databases = [row[0] for row in mycursor.fetchall() if
                         row[0] not in ['mysql', 'mydb', 'information_schema', 'performance_schema', 'sakila', 'sys',
                                        'world']]

            print("Доступные базы данных:")
            for idx, db in enumerate(databases, start=1):
                print(f"{idx}. {db}")

            db_selection = input("Выберите номер базы данных: ")
            if db_selection.lower() == "back":
                return
            selected_db = databases[int(db_selection) - 1]

            # Выбор действия
            actions = [
                "Удалить запись в таблице",
                "Вставить запись в таблицу",
                "Заменить запись в таблице",
                "Удалить таблицу",
                "Создать таблицу",
                "Заменить все записи в таблице",
                "Удалить все записи в таблице",
                "Сгенерировать записи в таблице"
            ]

            print("\nДоступные действия:")
            for idx, action in enumerate(actions, start=1):
                print(f"{idx}. {action}")

            action_selection = input("Выберите номер действия: ")
            if action_selection.lower() == "back":
                return
            action_index = int(action_selection) - 1

            if action_index == 0:
                delete_record(selected_db, host, user, password)
            elif action_index == 1:
                insert_record(selected_db, host, user, password)
            elif action_index == 2:
                replace_record(selected_db, host, user, password)
            elif action_index == 3:
                delete_table(selected_db, host, user, password)
            elif action_index == 4:
                create_table(selected_db, host, user, password)
            elif action_index == 5:
                replace_all_records(selected_db, host, user, password)
            elif action_index == 6:
                delete_all_records(selected_db, host, user, password)
            elif action_index == 7:
                with DatabaseConnection(host=host, user=user, password=password, database=selected_db) as (
                        mycursor, connection):
                    # Выбор таблицы
                    mycursor.execute(f"USE {selected_db}")
                    mycursor.execute("SHOW TABLES")
                    tables = [row[0] for row in mycursor.fetchall()]

                    print("\nДоступные таблицы:")
                    for idx, tbl in enumerate(tables, start=1):
                        print(f"{idx}. {tbl}")

                    table_selection = input("Выберите номер таблицы: ")
                    if table_selection.lower() == "back":
                        return
                    selected_table = tables[int(table_selection) - 1]

                    num_records = int(input("Введите количество записей для генерации: "))
                    query_time_generate(selected_table, selected_db, host, user, password, num_records, mycursor, connection)

    except mysql.connector.Error as err:
        print("Ошибка при редактировании базы данных:", err.msg)

def create_sandbox_database(host, user, password):
    """
    Создает временную базу данных для песочницы, основанную на структуре таблиц основной базы данных.

    Песочница представляет собой копию структуры таблиц из выбранной базы данных.

    Args:
        host (str): Хост базы данных.
        user (str): Пользователь базы данных.
        password (str): Пароль пользователя базы данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.

    Returns:
        None

    """
    try:
        with DatabaseConnection(host=host, user=user, password=password, database="mysql") as (mycursor, connection):
            # Выбираем базу данных
            print("Доступные базы данных:")
            mycursor.execute("SHOW DATABASES")
            databases = mycursor.fetchall()
            for idx, db in enumerate(databases, start=1):
                print(f"{idx}. {db[0]}")

            db_selection = input("Выберите номер базы данных для создания песочницы: ")
            selected_db = databases[int(db_selection) - 1][0]

            # Проверяем наличие существующей песочницы и удаляем ее, если она существует
            sandbox_db_name = f"sandbox_{selected_db}"
            if (sandbox_db_name,) in databases:
                mycursor.execute(f"DROP DATABASE {sandbox_db_name}")
                print("Удалена существующая база данных для песочницы.")

            # Создаем песочницу
            mycursor.execute(f"CREATE DATABASE {sandbox_db_name}")
            mycursor.execute(f"USE {sandbox_db_name}")

            # Получаем список таблиц без внешних ключей
            mycursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{selected_db}'")
            tables = mycursor.fetchall()

            # Создаем таблицы без внешних ключей
            for table in tables:
                table_name = table[0]
                mycursor.execute(f"SHOW TABLES LIKE '{table_name}'")
                existing_table = mycursor.fetchone()
                if not existing_table:
                    mycursor.execute(f"SHOW CREATE TABLE {selected_db}.{table_name}")
                    create_table_query = mycursor.fetchone()[1]
                    if "FOREIGN KEY" not in create_table_query:  # Проверяем, содержит ли запрос определения таблицы внешние ключи
                        mycursor.execute(create_table_query)

            # Получаем список таблиц с внешними ключами
            mycursor.execute(f"SELECT table_name FROM information_schema.tables WHERE table_schema = '{selected_db}'")
            tables_with_foreign_keys = mycursor.fetchall()

            # Создаем остальные таблицы и устанавливаем внешние ключи
            for table in tables_with_foreign_keys:
                table_name = table[0]
                mycursor.execute(f"SHOW TABLES LIKE '{table_name}'")
                existing_table = mycursor.fetchone()
                if not existing_table:
                    mycursor.execute(f"SHOW CREATE TABLE {selected_db}.{table_name}")
                    create_table_query = mycursor.fetchone()[1]
                    mycursor.execute(create_table_query)

            print("Песочница успешно создана.\n")

    except mysql.connector.Error as err:
        print("Ошибка при создании песочницы:", err)