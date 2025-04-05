import timeit

import mysql
from colorama import Fore
import mysql.connector
from investigations.graphics import graph_info, graph_generate_info
from lib.db_connection import DatabaseConnection
from lib.generator import generate_records
from lib.table_methods import get_tables


def measure_query_time(host, user, password):
    """
    Функция для измерения времени выполнения различных типов запросов.

    Args:
        host (str): Хост базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль для доступа к базе данных.

    Raises:
        ValueError: Если номер действия не соответствует допустимому значению.

    Notes:
        - Пользователь выбирает базу данных и таблицу для выполнения запросов.
        - Затем пользователь выбирает тип запроса:
            1. Свой запрос: Пользователь может ввести собственный SQL-запрос.
            2. Вставка: Производится вставка одной записи в выбранную таблицу.
            3. Выборка: Производится выборка всех записей из выбранной таблицы.
            4. Удаление: Производится удаление всех записей из выбранной таблицы.
        - Показывается время выполнения запроса в секундах.

    """
    try:
        with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (
        mycursor, connection):
            # Получаем список баз данных
            print("Доступные базы данных:")
            mycursor.execute("SHOW DATABASES")
            databases = mycursor.fetchall()
            for idx, db in enumerate(databases, start=1):
                print(f"{idx}. {db[0]}")

            db_selection = input("Выберите номер базы данных: ")
            selected_db = databases[int(db_selection) - 1][0]

            # Выбираем базу данных
            mycursor.execute(f"USE {selected_db}")

            print("Выберите таблицу:")
            tables = get_tables(connection)
            for i, table in enumerate(tables, 1):
                print(f"{i}. {table}")

            table_index = int(input("Введите номер таблицы: ")) - 1
            if 0 <= table_index < len(tables):
                selected_table = tables[table_index]

                print("Выберите тип запроса:")
                print("1. Свой запрос")
                print("2. Вставка")
                print("3. Выборка")
                print("4. Удаление")
                action = input("Введите номер действия: ")

                if action == "1":
                    try:
                        count_query = f"SELECT COUNT(*) FROM {selected_table}"
                        mycursor.execute(count_query)
                        row_count = mycursor.fetchone()[0]
                        custom_query = input("Введите свой SQL-запрос: ")

                        if custom_query.lower().find(selected_table.lower()) == -1:
                            print(Fore.RED + "Ошибка: Ваш запрос не относится к указанной таблице.")
                            print(Fore.RESET)
                            return

                        first_word = custom_query.strip().split()[0].upper()

                        if first_word == "DROP":
                            print(Fore.RED + "Ошибка: Данный запрос не поддерживается.")
                            print(Fore.RESET)
                            return

                        time_query = query_time_custom(mycursor, connection, custom_query, first_word, row_count)

                        print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")

                    except mysql.connector.Error as err:
                        print(Fore.RED + f"Ошибка выполнения запроса: {err}")
                        print(Fore.RESET)

                elif action == "2":
                    try:
                        count_query = f"SELECT COUNT(*) FROM {selected_table}"
                        mycursor.execute(count_query)
                        row_count = mycursor.fetchone()[0]

                        query, values = generate_records(selected_table, selected_db, host, user, password, 1, True)
                        time_query = query_time_insert(mycursor, connection, query, values, row_count)

                        print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")

                    except mysql.connector.Error as err:
                        print(Fore.RED + f"Ошибка выполнения запроса: {err}")
                        print(Fore.RESET)

                elif action == "3":
                    try:
                        count_query = f"SELECT COUNT(*) FROM {selected_table}"
                        mycursor.execute(count_query)
                        row_count = mycursor.fetchone()[0]

                        select_query = f"SELECT * FROM {selected_table}"

                        time_query = query_time_select(mycursor, connection, select_query, row_count)

                        print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")

                    except mysql.connector.Error as err:
                        print(Fore.RED + f"Ошибка выполнения запроса: {err}")
                        print(Fore.RESET)

                elif action == "4":
                    try:
                        count_query = f"SELECT COUNT(*) FROM {selected_table}"
                        mycursor.execute(count_query)
                        row_count = mycursor.fetchone()[0]

                        delete_query = f"DELETE FROM {selected_table}"

                        time_query = query_time_delete(mycursor, connection, delete_query, row_count)

                        print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")

                    except mysql.connector.Error as err:
                        print(Fore.RED + f"Ошибка выполнения запроса: {err}")
                        print(Fore.RESET)

            else:
                print(Fore.RED + "Ошибка: Некорректный номер таблицы.")
                print(Fore.RESET)

    except mysql.connector.Error as err:
        print(Fore.RED + "Ошибка при выполнении запроса:", err)
        print(Fore.RESET)


def query_time_custom(mycursor, connection, custom_query, first_word, row_count):
    """
        Измеряет время выполнения пользовательского SQL-запроса.

        Args:
            mycursor: Объект курсора базы данных.
            connection: Объект подключения к базе данных.
            custom_query (str): Пользовательский SQL-запрос.
            first_word (str): Первое слово в пользовательском запросе.
            row_count (int): Количество строк в таблице.

        Returns:
            float: Время выполнения запроса в секундах.

        Notes:
            - Измеряет время выполнения пользовательского запроса с использованием времени до и после выполнения запроса.
            - Записывает информацию о типе запроса, количестве строк в таблице и времени выполнения в глобальный список.

        """
    start_time = timeit.default_timer()
    mycursor.execute(custom_query)
    _ = mycursor.fetchall()
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = [first_word, row_count, time_query]
    graph_info.append(data)
    return time_query


def query_time_insert(mycursor, connection, query, values, row_count):
    """
        Измеряет время выполнения запроса на вставку данных в таблицу.

        Args:
            mycursor: Объект курсора базы данных.
            connection: Объект подключения к базе данных.
            query (str): SQL-запрос на вставку данных.
            values (tuple): Кортеж значений для вставки.
            row_count (int): Количество строк в таблице.

        Returns:
            float: Время выполнения запроса в секундах.

        Notes:
            - Измеряет время выполнения запроса на вставку данных с использованием времени до и после выполнения запроса.
            - Записывает информацию о типе запроса (вставка), количестве строк в таблице и времени выполнения в глобальный список.

        """
    start_time = timeit.default_timer()
    mycursor.execute(query, values)
    _ = mycursor.fetchall()
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = ["INSERT", row_count, time_query]
    graph_info.append(data)
    return time_query


def query_time_select(mycursor, connection, query, row_count):
    """
        Измеряет время выполнения запроса на выборку данных из таблицы.

        Args:
            mycursor: Объект курсора базы данных.
            connection: Объект подключения к базе данных.
            query (str): SQL-запрос на выборку данных.
            row_count (int): Количество строк в таблице.

        Returns:
            float: Время выполнения запроса в секундах.

        Notes:
            - Измеряет время выполнения запроса на выборку данных с использованием времени до и после выполнения запроса.
            - Записывает информацию о типе запроса (выборка), количестве строк в таблице и времени выполнения в глобальный список.

        """
    start_time = timeit.default_timer()
    mycursor.execute(query)
    _ = mycursor.fetchall()
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = ["SELECT", row_count, time_query]
    graph_info.append(data)
    return time_query


def query_time_delete(mycursor, connection, query, row_count):
    """
        Измеряет время выполнения запроса на удаление данных из таблицы.

        Args:
            mycursor: Объект курсора базы данных.
            connection: Объект подключения к базе данных.
            query (str): SQL-запрос на удаление данных.
            row_count (int): Количество строк в таблице.

        Returns:
            float: Время выполнения запроса в секундах.

        Notes:
            - Измеряет время выполнения запроса на удаление данных с использованием времени до и после выполнения запроса.
            - Записывает информацию о типе запроса (удаление), количестве строк в таблице и времени выполнения в глобальный список.

        """
    start_time = timeit.default_timer()
    mycursor.execute(query)
    connection.commit()
    end_time = timeit.default_timer()
    time_query = end_time - start_time
    data = ["DELETE", row_count, time_query]
    graph_info.append(data)
    return time_query


def query_time_generate(table_name, selected_db, host, user, password, num_entries, mycursor, connection):
    """
        Измеряет время выполнения запроса на генерацию данных в таблице.

        Args:
            table_name (str): Название таблицы, в которой происходит генерация данных.
            selected_db (str): Название выбранной базы данных.
            host (str): Адрес хоста базы данных.
            user (str): Имя пользователя базы данных.
            password (str): Пароль пользователя базы данных.
            num_entries (int): Количество записей для генерации.
            mycursor: Объект курсора базы данных.
            connection: Объект подключения к базе данных.

        Returns:
            float: Время выполнения запроса в секундах.

        Notes:
            - Измеряет время выполнения запроса на генерацию данных с использованием времени до и после выполнения запроса.
            - Записывает информацию о типе запроса (генерация), количестве сгенерированных записей и времени выполнения в глобальный список.

    """
    count_query = f"SELECT COUNT(*) FROM {table_name}"
    mycursor.execute(count_query)
    row_count = mycursor.fetchone()[0]

    start_time = timeit.default_timer()
    generate_records(table_name, selected_db, host, user, password, num_entries, False)
    connection.commit()
    end_time = timeit.default_timer()

    time_query = end_time - start_time

    data = ["GENERATE", num_entries, time_query]
    graph_generate_info.append(data)
    return time_query