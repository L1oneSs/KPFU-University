import mysql.connector
from investigations.graphics import create_graphics
from investigations.query_time import query_time_generate, query_time_select, query_time_custom, query_time_insert, \
    query_time_delete
from lib.creator import create_table_entry
from colorama import init, Fore

init()

class DatabaseConnection:
    """
        Класс для управления соединением с базой данных MySQL.

        Attributes:
            host (str): Хост базы данных.
            user (str): Имя пользователя базы данных.
            password (str): Пароль пользователя базы данных.
            database (str): Имя базы данных.
            connection: Объект соединения с базой данных.
            cursor: Объект курсора для выполнения операций с базой данных.
        """

    def __init__(self, host, user, password, database):
        """
                Инициализирует объект DatabaseConnection с указанными параметрами подключения.

                Args:
                    host (str): Хост базы данных.
                    user (str): Имя пользователя базы данных.
                    password (str): Пароль пользователя базы данных.
                    database (str): Имя базы данных.
                """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
                Метод контекстного менеджера для получения соединения с базой данных.

                Returns:
                    cursor: Объект курсора для выполнения операций с базой данных.
                    connection: Объект соединения с базой данных.
                """
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor, self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
                Метод контекстного менеджера для закрытия соединения с базой данных.

                Args:
                    exc_type: Тип исключения (если есть).
                    exc_val: Значение исключения (если есть).
                    exc_tb: Трассировка исключения (если есть).
                """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.commit()
            self.connection.close()


def main():
    """
    Главная функция программы, обеспечивающая основную логику выполнения операций с базой данных.

    Эта функция обеспечивает выполнение следующих действий:
    - Генерация записей в базе данных.
    - Создание временной базы данных.
    - Замена данных в таблицах.
    - Удаление данных из таблиц.
    - Выполнение пользовательских SQL-запросов.
    - Генерация графиков зависимости времени выполнения от количества записей.

    Примечание:
    Для хранения информации о времени выполнения запросов и генерации записей используются глобальные переменные
    graph_info и graph_generate_info соответственно.

    """
    with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (mycursor, _):
        tables = get_table_names(mycursor)

    while True:
        print("Доступные команды: Генерация, Песочница, Заменить, Удалить, Время, График")
        type_in = input("Введите команду: ")

        if type_in == "Генерация":
            with DatabaseConnection(host="localhost", user="root", password="root", database="mydb"):
                generate_entries(tables)
        elif type_in == "Песочница":
            with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (mycursor, _):
                create_sandbox_database(mycursor)
        elif type_in == "Заменить":
            print("Выберите таблицу для замены данных:")
            for i, table in enumerate(tables, 1):
                print(f"{i}. {table}")
            table_index = int(input("Введите номер таблицы: ")) - 1
            table_name = tables[table_index]
            replace_all_data(table_name)
        elif type_in == "Удалить":
            print("Выберите таблицу для удаления данных:")
            for i, table in enumerate(tables, 1):
                print(f"{i}. {table}")
            table_index = int(input("Введите номер таблицы: ")) - 1
            table_name = tables[table_index]
            delete_all_data(table_name)
        elif type_in == "Время":
            with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (
                    mycursor, connection):
                print("Выберите действие:")
                print("1. Свой запрос")
                print("2. Insert")
                print("3. Select")
                print("4. Delete")
                action = input("Введите номер действия: ")

                if action == "1":
                    table_name = input("Введите название таблицы: ")
                    try:
                        count_query = f"SELECT COUNT(*) FROM {table_name}"
                        mycursor.execute(count_query)
                        row_count = mycursor.fetchone()[0]
                        custom_query = input("Введите свой SQL-запрос: ")

                        if custom_query.lower().find(table_name.lower()) == -1:
                            print(Fore.RED + "Ошибка: Ваш запрос не относится к указанной таблице.")
                            print(Fore.RESET)
                            continue

                        first_word = custom_query.strip().split()[0].upper()

                        if first_word == "DROP":
                            print(Fore.RED + "Ошибка: Данный запрос не поддерживается.")
                            print(Fore.RESET)
                        else:
                            try:
                                time_query = query_time_custom(mycursor, connection, custom_query, first_word, row_count)
                                print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")
                            except mysql.connector.Error as err:
                                print(Fore.RED + f"Ошибка выполнения запроса: {err}")
                                print(Fore.RESET)
                    except mysql.connector.Error as err:
                        print(Fore.RED + f"Ошибка выполнения запроса для подсчета количества строк: {err}")
                        print(Fore.RESET)

                elif action == "2":
                    tables = get_table_names(mycursor)
                    print("Доступные таблицы:")
                    for i, table in enumerate(tables, 1):
                        print(f"{i}. {table}")
                    try:
                        table_index = int(input("Введите номер таблицы: ")) - 1
                        if 0 <= table_index < len(tables):
                            selected_table = tables[table_index]
                            count_query = f"SELECT COUNT(*) FROM {selected_table}"
                            mycursor.execute(count_query)
                            row_count = mycursor.fetchone()[0]

                            if selected_table.lower() == "airlines":
                                values = ("Airline1", "ABC", "Country1")
                                fields = ("name", "code", "country")
                            elif selected_table.lower() == "airport":
                                values = ("XYZ", "Airport1", "City1", "Country2")
                                fields = ("code", "name", "city", "country")
                            elif selected_table.lower() == "airportstaff":
                                values = ("John", "Doe", "Manager", "123-456-7890", "XYZ")
                                fields = ("first_name", "last_name", "job_title", "contact_info", "airport_code")
                            elif selected_table.lower() == "baggage":
                                values = (123, 20.5, 456)
                                fields = ("flight_id", "weight", "passenger_id")
                            elif selected_table.lower() == "flights":
                                values = ("10:00:00", "12:00:00", "Scheduled", 1, "ABC", "XYZ")
                                fields = (
                                    "departure_time", "arrival_time", "flight_status", "airline_id",
                                    "origin_airport_code",
                                    "destination_airport_code")
                            elif selected_table.lower() == "passengers":
                                values = ("Alice", "Smith", "AB123456", "alice@example.com")
                                fields = ("first_name", "last_name", "passport_number", "contact_info")
                            elif selected_table.lower() == "securitycheck":
                                values = ("09:00:00", "Pass", 123, 1)
                                fields = ("check_time", "result", "flight_id", "tickets_id")
                            elif selected_table.lower() == "tickets":
                                values = ("A12", "Valid", 1, 123, 100.0)
                                fields = ("seat_number", "ticket_status", "passenger_id", "flight_id", "cost")

                            placeholders = ', '.join(['%s'] * len(fields))
                            fields_str = ', '.join(fields)
                            query = f"INSERT INTO {selected_table} ({fields_str}) VALUES ({placeholders})"

                            try:
                                time_query = query_time_insert(mycursor, connection, query, values, row_count)
                                print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")
                            except mysql.connector.Error as err:
                                print(Fore.RED + f"Ошибка вставки данных: {err}")
                                print(Fore.RESET)
                        else:
                            print(Fore.RED + "Ошибка: Некорректный номер таблицы.")
                            print(Fore.RESET)
                    except ValueError:
                        print(Fore.RED + "Ошибка: Некорректный ввод.")
                        print(Fore.RESET)


                elif action == "3":
                    tables = get_table_names(mycursor)
                    print("Доступные таблицы:")
                    for i, table in enumerate(tables, 1):
                        print(f"{i}. {table}")
                    try:
                        table_index = int(input("Введите номер таблицы: ")) - 1
                        if 0 <= table_index < len(tables):
                            selected_table = tables[table_index]
                            select_query = f"SELECT * FROM {selected_table}"

                            count_query = f"SELECT COUNT(*) FROM {selected_table}"
                            mycursor.execute(count_query)
                            row_count = mycursor.fetchone()[0]
                            try:
                                time_query = query_time_select(mycursor, connection, select_query, row_count)
                                print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")
                            except mysql.connector.Error as err:
                                print(Fore.RED + f"Ошибка выполнения запроса: {err}")
                                print(Fore.RESET)
                        else:
                            print(Fore.RED + "Ошибка: Некорректный номер таблицы.")
                            print(Fore.RESET)
                    except ValueError:
                        print(Fore.RED + "Ошибка: Некорректный ввод.")
                        print(Fore.RESET)

                elif action == "4":
                    tables = get_table_names(mycursor)
                    print("Доступные таблицы:")
                    for i, table in enumerate(tables, 1):
                        print(f"{i}. {table}")
                    try:
                        table_index = int(input("Введите номер таблицы: ")) - 1
                        if 0 <= table_index < len(tables):
                            selected_table = tables[table_index]
                            count_query = f"SELECT COUNT(*) FROM {selected_table}"
                            mycursor.execute(count_query)
                            row_count = mycursor.fetchone()[0]

                            query = f"DELETE FROM {selected_table}"

                            try:
                                time_query = query_time_delete(mycursor, connection, query, row_count)
                                print(f"Запрос выполнен успешно. Время выполнения: {time_query} секунд.")
                            except mysql.connector.Error as err:
                                print(Fore.RED + f"Ошибка удаления данных: {err}")
                                print(Fore.RESET)
                        else:
                            print(Fore.RED + "Ошибка: Некорректный номер таблицы.")
                            print(Fore.RESET)
                    except ValueError:
                        print(Fore.RED + "Ошибка: Некорректный ввод.")
                        print(Fore.RESET)

        elif type_in == "График":
            type_in = input("Выберите номер действия:\n1. Запросы\n2. Генерация\n")
            if type_in != '1' and type_in != '2':
                print(Fore.RED + "Ошибка: Неподдерживаемая команда.")
                print(Fore.RESET)
            else:
                create_graphics(type_in)
        else:
            print(Fore.RED + "Ошибка: Неподдерживаемая команда.")
            print(Fore.RESET)


def get_table_names(mycursor):
    """
        Получает список имен таблиц из базы данных.

        Parameters:
            mycursor (MySQLCursor): Курсор для выполнения операций с базой данных.

        Returns:
            list: Список имен таблиц в базе данных.

        Raises:
            MySQLInterfaceError: Если произошла ошибка при выполнении операции SHOW TABLES.

        """
    mycursor.execute("SHOW TABLES")
    tables = [table[0] for table in mycursor.fetchall()]
    return tables


def generate_entries(tables):
    """
        Генерирует записи в указанной таблице базы данных.

        Пользователь сначала выбирает таблицу из списка доступных. Затем указывает количество записей,
        которое необходимо сгенерировать для этой таблицы.

        Parameters:
            tables (list): Список имен таблиц в базе данных.

        Raises:
            ValueError: Если введен некорректный номер таблицы или количество записей.
            MySQLInterfaceError: Если произошла ошибка при выполнении запроса на подсчет количества строк.

        """
    print("Выберите название таблицы: ")
    for i, table in enumerate(tables, 1):
        print(f"{i}. {table}")

    while True:
        try:
            table_index = int(input("Введите номер таблицы: ")) - 1
            if table_index < 0 or table_index >= len(tables):
                raise ValueError("Неверный номер таблицы.")
            break
        except ValueError:
            print(Fore.RED + "Некорректный номер таблицы")
            print(Fore.RESET)

    table_name = tables[table_index]

    while True:
        try:
            num_entries = int(input("Сколько записей вы хотите создать? "))
            if num_entries <= 0:
                raise ValueError("Введите положительное число записей.")
            elif num_entries > 100:
                raise ValueError("Слишком много записей (не более 100).")
            break
        except ValueError:
            print(Fore.RED + "Некорректное количество записей")
            print(Fore.RESET)

    with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (mycursor, connection):
        query_time_generate(table_name, num_entries, mycursor, connection)
    print("Записи успешно созданы!\n")


def create_sandbox_database(mycursor):
    """
        Создает временную базу данных для песочницы, основанную на структуре таблиц основной базы данных.

        Песочница представляет собой копию структуры таблиц из основной базы данных mydb.

        Parameters:
            mycursor (MySQLCursor): Курсор для выполнения операций с базой данных.

        Raises:
            MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.

        """
    sandbox_db_name = 'sandbox_mydb'

    try:
        mycursor.execute("SHOW DATABASES")
        databases = mycursor.fetchall()
        if (sandbox_db_name,) in databases:
            mycursor.execute(f"DROP DATABASE {sandbox_db_name}")
            print("Удалена существующая база данных для песочницы.")

        mycursor.execute(f"CREATE DATABASE {sandbox_db_name}")
        mycursor.execute(f"USE {sandbox_db_name}")

        mycursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'mydb'")
        tables = mycursor.fetchall()

        for table in tables:
            table_name = table[0]
            mycursor.execute(f"SHOW CREATE TABLE mydb.{table_name}")
            create_table_query = mycursor.fetchone()[1]
            mycursor.execute(create_table_query)

        print("Песочница успешно создана.\n")

    except mysql.connector.Error as err:
        print("Ошибка при создании песочницы:", err)
        return


def replace_all_data(table_name):
    """
        Заменяет все данные в указанной таблице новыми данными.

        Функция удаляет все записи из указанной таблицы и затем создает новые записи с использованием функции create_table_entry.

        Parameters:
            table_name (str): Имя таблицы, в которой нужно заменить данные.

        Raises:
            MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.

        """
    with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (mycursor, _):
        try:
            mycursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            count = mycursor.fetchone()[0]

            sql_delete_all = f"DELETE FROM {table_name}"
            mycursor.execute(sql_delete_all)

            create_table_entry(table_name, count, mycursor)

            print(f"Все данные в таблице {table_name} успешно заменены.\n")
        except mysql.connector.Error as err:
            print(f"Ошибка при замене данных в таблице {table_name}: {err}")


def delete_all_data(table_name):
    """
        Удаляет все данные из указанной таблицы.

        Parameters:
            table_name (str): Имя таблицы, из которой нужно удалить данные.

        Raises:
            MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.

        """
    with DatabaseConnection(host="localhost", user="root", password="root", database="mydb") as (mycursor, _):
        try:
            sql_delete_all = f"DELETE FROM {table_name}"
            mycursor.execute(sql_delete_all)

            print(f"Все данные в таблице {table_name} успешно удалены.\n")
        except mysql.connector.Error as err:
            print(f"Ошибка при удалении данных из таблицы {table_name}: {err}")


if __name__ == "__main__":
    main()
