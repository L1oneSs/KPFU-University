import mysql
import mysql.connector
from colorama import Fore

from lib.db_connection import DatabaseConnection
from lib.generator import generate_records

def link_table(connection, table_name):
    """
    Связывает указанную таблицу с другой таблицей по заданному столбцу.

    Args:
        connection: Объект подключения к базе данных.
        table_name (str): Имя таблицы, которую необходимо связать.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    print("Связывание таблиц:")
    try:
        with connection.cursor() as mycursor:
            mycursor.execute("SHOW TABLES")
            tables = [row[0] for row in mycursor.fetchall() if row[0] != table_name]

            if not tables:
                print("Нет других таблиц для связывания.")
                return

            print("Доступные таблицы для связывания:")
            for idx, tbl in enumerate(tables, start=1):
                print(f"{idx}. {tbl}")

            selection = input("Выберите номер таблицы для связывания: ")
            if selection.lower() == "back":
                return
            selected_table = tables[int(selection) - 1]

            mycursor.execute(f"DESCRIBE {selected_table}")
            columns = [row[0] for row in mycursor.fetchall()]

            print(f"Доступные столбцы в таблице {selected_table}:")
            for idx, col in enumerate(columns, start=1):
                print(f"{idx}. {col}")

            selected_column = input("Выберите номер столбца для связывания: ")
            if selected_column.lower() == "back":
                return
            selected_column = columns[int(selected_column) - 1]

            relationship_type = input("Выберите тип связи (Многие ко многим/Один ко многим/Один к одному): ")

            set_foreign_key(connection, table_name, selected_table, selected_column, relationship_type)

    except mysql.connector.Error as err:
        print("Ошибка при связывании таблиц:", err.msg)


def set_foreign_key(connection, table_name, selected_table, selected_column, relationship_type):
    """
    Устанавливает внешний ключ между указанными таблицами.

    Args:
        connection: Объект подключения к базе данных.
        table_name (str): Имя таблицы, для которой устанавливается внешний ключ.
        selected_table (str): Имя таблицы, с которой устанавливается связь.
        selected_column (str): Имя столбца, который будет связан с основной таблицей.
        relationship_type (str): Тип связи. Возможные значения: 'многие ко многим', 'один ко многим', 'один к одному'.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    try:
        with connection.cursor() as mycursor:
            if relationship_type.strip().lower() == "многие ко многим":
                # Создаем таблицу-посредник
                intermediate_table_name = f"{table_name}_{selected_table}"
                mycursor.execute(
                    f"CREATE TABLE {intermediate_table_name} ({table_name}_id INT, {selected_table}_id INT)")
                # Устанавливаем внешние ключи для таблицы-посредника
                mycursor.execute(
                    f"ALTER TABLE {intermediate_table_name} ADD CONSTRAINT fk_{intermediate_table_name}_{table_name} FOREIGN KEY ({table_name}_id) REFERENCES {table_name}(id)")
                mycursor.execute(
                    f"ALTER TABLE {intermediate_table_name} ADD CONSTRAINT fk_{intermediate_table_name}_{selected_table} FOREIGN KEY ({selected_table}_id) REFERENCES {selected_table}(id)")
                # Устанавливаем внешние ключи для связываемых таблиц
                mycursor.execute(
                    f"ALTER TABLE {table_name} ADD CONSTRAINT fk_{table_name}_{intermediate_table_name} FOREIGN KEY (id) REFERENCES {intermediate_table_name}({table_name}_id)")
                mycursor.execute(
                    f"ALTER TABLE {selected_table} ADD CONSTRAINT fk_{selected_table}_{intermediate_table_name} FOREIGN KEY (id) REFERENCES {intermediate_table_name}({selected_table}_id)")
                print(f"Таблицы {table_name} и {selected_table} успешно связаны (Многие ко многим).")
            elif relationship_type.strip().lower() == "один ко многим":
                mycursor.execute(
                    f"ALTER TABLE {table_name} ADD CONSTRAINT fk_{table_name}_{selected_table} FOREIGN KEY ({selected_column}) REFERENCES {selected_table}(id)")
                print(f"Таблица {table_name} успешно связана с таблицей {selected_table} (Один ко многим).")
            elif relationship_type.strip().lower() == "один к одному":
                # Проверяем, есть ли уже уникальный индекс в выбранном столбце
                mycursor.execute(
                    f"SHOW INDEX FROM {selected_table} WHERE Column_name = '{selected_column}' AND Non_unique = 0")
                unique_index = mycursor.fetchone()
                if unique_index:
                    # Если уникальный индекс уже есть, используем его
                    index_name = unique_index[2]
                    mycursor.execute(
                        f"ALTER TABLE {table_name} ADD CONSTRAINT fk_{table_name}_{selected_table} FOREIGN KEY ({selected_column}) REFERENCES {selected_table}({selected_column})")
                    print(
                        f"Таблица {table_name} успешно связана с таблицей {selected_table} (Один к одному). Использован существующий уникальный индекс '{index_name}'.")
                else:
                    # Если уникального индекса нет, создаем его и затем устанавливаем внешний ключ
                    mycursor.execute(
                        f"ALTER TABLE {selected_table} ADD UNIQUE INDEX idx_{selected_table}_{selected_column} ({selected_column})")
                    mycursor.execute(
                        f"ALTER TABLE {table_name} ADD CONSTRAINT fk_{table_name}_{selected_table} FOREIGN KEY ({selected_column}) REFERENCES {selected_table}({selected_column})")
                    print(
                        f"Таблица {table_name} успешно связана с таблицей {selected_table} (Один к одному). Создан новый уникальный индекс.")
            else:
                print("Некорректный тип связи.")

    except mysql.connector.Error as err:
        print("Ошибка при установке внешнего ключа:", err.msg)

def create_table(selected_db, host, user, password):
    """
    Создает новую таблицу в указанной базе данных.

    Args:
        selected_db (str): Имя базы данных, в которой будет создана таблица.
        host (str): Адрес хоста базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль пользователя базы данных.

    Returns:
        str: Возвращает строку 'id', если вводится некорректное имя столбца ('id').

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    with DatabaseConnection(host=host, user=user, password=password, database=selected_db) as (mycursor, connection):
        # Выбор таблицы
        mycursor.execute(f"USE {selected_db}")
        print("Создание новой таблицы:")
        table_name = input("Введите название таблицы: ")
        if table_name.lower() == "back":
            return

        # Запрос на создание таблицы
        create_table_query = f"CREATE TABLE {table_name} ("

        create_table_query += "id INT AUTO_INCREMENT PRIMARY KEY, "  # Автоматическое создание поля id

        num_columns = int(input("Введите количество столбцов (без учета id): "))

        for i in range(num_columns):
            column_name = input(f"Введите название столбца {i + 1}: ")
            column_name = column_name.lower()
            if column_name == "id":
                print(Fore.RED + "Поле id создается автоматически")
                print(Fore.RESET)
                return "id"
            column_type = input(
                f"Введите тип данных для столбца {column_name} (varchar, int, datetime, float): ").lower()
            while column_type not in ["varchar", "int", "datetime", "float"]:
                print("Некорректный тип данных.")
                column_type = input(
                    f"Введите тип данных для столбца {column_name} (varchar, int, datetime, float): ").lower()

            # Добавляем ограничения на длину для varchar
            if column_type == "varchar":
                column_length = input(f"Введите ограничение на количество символов для столбца {column_name}: ")
                create_table_query += f"{column_name} {column_type}({column_length})"
            elif column_type in ["int", "float"]:
                column_size = input(f"Введите размер для столбца {column_name} (по умолчанию 10): ")
                create_table_query += f"{column_name} {column_type}({column_size if column_size else '10'})"
            else:
                create_table_query += f"{column_name} {column_type}"

            if i < num_columns - 1:
                create_table_query += ", "

        create_table_query += ")"

        try:
            mycursor.execute(create_table_query)
            print(f"Таблица {table_name} успешно создана.")

            # Если в базе есть более одной таблицы, спрашиваем пользователя, хочет ли он связать эту таблицу с другой
            mycursor.execute("SHOW TABLES")
            num_tables = len(mycursor.fetchall())
            if num_tables > 1:
                link_tables = input("Хотите связать эту таблицу с другой? (Да/Нет): ").lower()
                if link_tables == "да":
                    link_table(connection, table_name)

        except mysql.connector.Error as err:
            print("Ошибка при создании таблицы:", err.msg)


def get_tables(connection):
    """
    Возвращает список таблиц в базе данных.

    Args:
        connection: Объект соединения с базой данных.

    Returns:
        list: Список имен таблиц в базе данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запроса к базе данных.
    """
    with connection.cursor() as cursor:
        cursor.execute("SHOW TABLES")
        tables = [table[0] for table in cursor.fetchall()]
    return tables


def get_columns(connection, table_name):
    """
    Возвращает список столбцов в указанной таблице.

    Args:
        connection: Объект соединения с базой данных.
        table_name (str): Имя таблицы, для которой требуется получить список столбцов.

    Returns:
        list: Список имен столбцов в указанной таблице.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запроса к базе данных.
    """
    with connection.cursor() as cursor:
        cursor.execute(f"DESCRIBE {table_name}")
        columns = [column[0] for column in cursor.fetchall()]
    return columns


def delete_record(selected_db, host, user, password):
    """
    Метод для удаления записи из указанной таблицы в базе данных.

    Args:
        selected_db (str): Имя базы данных, в которой находится таблица.
        host (str): Хост базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль для доступа к базе данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    try:
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

            # Вывод записей таблицы
            mycursor.execute(f"DESCRIBE {selected_table}")
            table_structure = [row[0] for row in mycursor.fetchall()]

            mycursor.execute(f"SELECT * FROM {selected_table}")
            records = mycursor.fetchall()

            print("\nДоступные записи:")
            for idx, record in enumerate(records, start=1):
                print(f"{idx}. {record}")

            record_selection = input("Выберите номер записи для удаления: ")
            if record_selection.lower() == "back":
                return
            record_index = int(record_selection) - 1

            # Получаем значение id выбранной записи
            record_id = records[record_index][table_structure.index('id')]

            # Удаление выбранной записи по первичному ключу
            mycursor.execute(f"DELETE FROM {selected_table} WHERE id = {record_id}")
            print("Запись успешно удалена.")

    except mysql.connector.Error as err:
        print("Ошибка при удалении записи:", err.msg)


def insert_record(selected_db, host, user, password):
    """
    Метод для вставки новой записи в указанную таблицу в базе данных.

    Args:
        selected_db (str): Имя базы данных, в которой находится таблица.
        host (str): Хост базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль для доступа к базе данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    try:
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

            # Вывод структуры таблицы с типами данных и ограничениями
            mycursor.execute(f"DESCRIBE {selected_table}")
            table_structure = [(row[0], row[1], row[5]) for row in mycursor.fetchall()]

            print("\nСтруктура таблицы:")
            for column_info in table_structure:
                column_name, data_type, extra_info = column_info
                if data_type == 'varchar':
                    print(f"{column_name}: {data_type}({extra_info})")
                else:
                    print(f"{column_name}: {data_type}")

            # Ввод данных для новой записи
            record_values = []
            for column_info in table_structure:
                column_name, data_type, extra_info = column_info
                if column_name.lower() == 'id' and 'auto_increment' in extra_info.lower():
                    continue  # Пропускаем автоинкрементное поле id
                value = input(f"Введите значение для столбца '{column_name}': ")
                record_values.append(value)

            # Формирование запроса на вставку записи
            # Убираем автоинкрементный столбец из списка значений
            insert_query = f"INSERT INTO {selected_table} ({', '.join([col[0] for col in table_structure if col[0].lower() != 'id'])}) VALUES ({', '.join(['%s'] * len(record_values))})"
            mycursor.execute(insert_query, record_values)
            print("Новая запись успешно добавлена.")

    except mysql.connector.Error as err:
        print("Ошибка при вставке записи:", err.msg)


def replace_record(selected_db, host, user, password):
    """
    Метод для замены существующей записи в указанной таблице в базе данных.

    Args:
        selected_db (str): Имя базы данных, в которой находится таблица.
        host (str): Хост базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль для доступа к базе данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    try:
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

            # Вывод записей таблицы
            mycursor.execute(f"SELECT * FROM {selected_table}")
            records = mycursor.fetchall()

            print("\nДоступные записи:")
            for idx, record in enumerate(records, start=1):
                print(f"{idx}. {record}")

            record_selection = input("Выберите номер записи для замены: ")
            if record_selection.lower() == "back":
                return
            record_index = int(record_selection) - 1

            # Вывод структуры таблицы
            mycursor.execute(f"DESCRIBE {selected_table}")
            table_structure = [row[0] for row in mycursor.fetchall()]

            print("\nСтруктура таблицы:")
            for column_name in table_structure:
                print(column_name)

            # Ввод новых данных для записи
            record_values = []
            for column in table_structure:
                value = input(f"Введите новое значение для столбца '{column}': ")
                record_values.append(value)

            # Формирование запроса на замену записи
            replace_query = f"UPDATE {selected_table} SET {', '.join([f'{column} = %s' for column in table_structure])} WHERE id = %s"
            id_index = next(index for index, column_info in enumerate(table_structure) if column_info == 'id')
            record_values.append(records[record_index][id_index])
            mycursor.execute(replace_query, record_values)
            print("Запись успешно заменена.")

    except mysql.connector.Error as err:
        print("Ошибка при замене записи:", err.msg)


def delete_table(selected_db, host, user, password):
    """
    Метод для удаления выбранной таблицы из указанной базы данных.

    Args:
        selected_db (str): Имя базы данных, из которой нужно удалить таблицу.
        host (str): Хост базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль для доступа к базе данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    try:
        with DatabaseConnection(host=host, user=user, password=password, database=selected_db) as (
        mycursor, connection):
            # Выбор таблицы
            mycursor.execute(f"USE {selected_db}")
            mycursor.execute("SHOW TABLES")
            tables = [row[0] for row in mycursor.fetchall()]

            print("\nДоступные таблицы:")
            for idx, tbl in enumerate(tables, start=1):
                print(f"{idx}. {tbl}")

            table_selection = input("Выберите номер таблицы для удаления: ")
            if table_selection.lower() == "back":
                return
            selected_table = tables[int(table_selection) - 1]

            # Удаление выбранной таблицы
            mycursor.execute(f"DROP TABLE {selected_table}")
            print("Таблица успешно удалена.")

    except mysql.connector.Error as err:
        print("Ошибка при удалении таблицы:", err.msg)


def replace_all_records(selected_db, host, user, password):
    """
    Метод для замены всех записей в выбранной таблице указанной базы данных.

    Args:
        selected_db (str): Имя базы данных, в которой находится таблица.
        host (str): Хост базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль для доступа к базе данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    try:
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

            mycursor.execute(f"SELECT COUNT(*) FROM {selected_table}")
            num_records = mycursor.fetchone()[0]

            # Удаление всех записей из таблицы
            delete_all_query = f"DELETE FROM {selected_table}"
            mycursor.execute(delete_all_query)

        # Генерация новых записей для таблицы
        generate_records(selected_table, selected_db, host, user, password, num_records)

        print("Все записи в таблице успешно заменены.")

    except mysql.connector.Error as err:
        print("Ошибка при замене всех записей:", err.msg)


def delete_all_records(selected_db, host, user, password):
    """
    Метод для удаления всех записей в выбранной таблице указанной базы данных.

    Args:
        selected_db (str): Имя базы данных, в которой находится таблица.
        host (str): Хост базы данных.
        user (str): Имя пользователя базы данных.
        password (str): Пароль для доступа к базе данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    try:
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

            # Удаление всех записей из выбранной таблицы
            mycursor.execute(f"DELETE FROM {selected_table}")
            print("Все записи в таблице успешно удалены.")

    except mysql.connector.Error as err:
        print("Ошибка при удалении всех записей:", err.msg)