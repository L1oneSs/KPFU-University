"""
Данный модуль использует функцию research для проведения исследования

Функции:
- research(): Проводит исследования и строит графики времени выполнения различных операций.
- generate_all_data(size): Генерирует данные для всех таблиц и сохраняет их в базу данных.
- generate_all_tables(): Создает все таблицы в базе данных.
"""

import os
from investigations.graphics import PlotBuilder
from investigations.time import measure_generation_time, measure_query_time_insert, measure_select_delete_query_time
from lib.class_basis import Airlines, AirportStaff, Airport, Passengers, Flights, Baggage, Tickets, SecurityCheck
from lib.connection import DatabaseConnection
from lib.helpers import ensure_unique_identifiers, format_data
from lib.sandbox import create_sandbox
from lib.table_methods import delete_all_data

def research():
    """
    Функция для проведения ИССЛЕДОВАНИЯ

    ------------

    ИССЛЕДОВАНИЕ

    В данной функции исследуются:

    1) Время генерации данных для одиночной таблицы
    2) Время генерации данных для связанных таблиц
    3) Время выполнения трех вариаций запроса INSERT на трех различных таблицах
    4) Время выполнения трех вариаций запроса SELECT(каждая вариация на трех таблицах)
    5) Время выполнения трех вариаций запроса DELETE(каждая вариация на трех таблицах)
    6) Время выполнения трех вариаций запроса UPDATE (каждая вариация на трех таблицах)


    ------------

    1. Время генерации данных для одиночной таблицы

    - Создается новая пустая песочница и предварительно заполняется данными.
    - Создается список размерностей, по которым генерируются данные и запоминается время.
    - Зависимость величины данных для генерации и времени генерации показывается на графике.
    - Измерения производятся для таблицы Airlines.

    ------------

    2. Время генерации данных для связанных таблиц

    - Создается новая пустая песочница и предварительно заполняется данными.
    - Создается список размерностей, по которым генерируются данные и запоминается время.
    - На каждой итерации времена генерации для двух таблиц суммируются.
    - Зависимость величины данных для генерации и времени генерации показывается на графике.
    - Измерения производятся на таблицах Flights и Airport

    ------------

    3. Время выполнения трех вариаций запроса INSERT на трех различных таблицах

    - Создаются три различных типа запроса INSERT:
        - INSERT INTO airlines (id, name, code, country) VALUES (%s, %s, %s, %s)", "airlines", "id"),
        - ("INSERT INTO passengers (id, first_name, last_name, passport_number, contact_info) SELECT %s, %s, %s, %s, %s WHERE NOT EXISTS (SELECT 1 FROM passengers WHERE id = %s)", "passengers", "id"),
        - ("INSERT INTO baggage (id, flight_id, weight, passenger_id) VALUES (%s, %s, REVERSE(%s), %s)", "baggage", "id"
    - Запросы создаются для таблиц Airlines, Passengers и Baggage

    - Первый запрос используется для простой вставки данных в таблицу Airlines
    - Второй запрос используется для вставки данных в таблицу Passengers при условии, что запись с заданным `id` еще не существует
    - Третий запрос используется для вставки данных в таблицу Baggage с применением функции `REVERSE`

    - Данные разбиваются на различные размерности
    - Для каждой размерности генерируются данные и вставляются с помощью запросов в таблицу
    - Зависимость времени выполнения запросов от величины вставляемых данных показывается на графике.

    ------------

    4. Время выполнения трех вариаций запроса SELECT(каждая вариация на трех таблицах)

    - Создаются три различных запроса типа SELECT:
        - SELECT * FROM
        - SELECT * FROM WHERE LIKE
        - SELECT * FROM WHERE (УСЛОВИЕ)

    - Запросы создаются группами для таблиц Airlines, Passengers и Baggage
    - На каждой итерации по количеству данных измеряется время выполнения запросов для трех таблиц
    - Для каждого типа запроса на одном графике отображается зависимость между количеством данных и
    временем выполнения запроса для трех таблиц.
    - На графике каждый отдельный запрос из отдельного типа представлен как QUERY 1, QUERY 2, QUERY 3
    - На каждой итерации данные удаляются и предварительно генерируются заново

    5. Время выполнения трех вариаций запроса DELETE(каждая вариация на трех таблицах)

    - Создаются три различных запроса типа SELECT:
        - DELETE * FROM
        - DELETE * FROM WHERE LIKE
        - DELETE * FROM WHERE (УСЛОВИЕ)

    - Запросы создаются группами для таблиц Airlines, Passengers и Baggage
    - На каждой итерации по количеству данных измеряется время выполнения запросов для трех таблиц
    - Для каждого типа запроса на одном графике отображается зависимость между количеством данных и
    временем выполнения запроса для трех таблиц.
    - На графике каждый отдельный запрос из отдельного типа представлен как QUERY 1, QUERY 2, QUERY 3
    - Запросы DELETE на каждой итерации выполняются после запросов SELECT

    ------------

    6. Время выполнения трех вариаций запроса UPDATE (каждая вариация на трех таблицах)

    - Создаются три различных запроса типа UPDATE:
        - UPDATE SET
        - UPDATE SET WHERE LIKE
        - UPDATE SET WHERE (УСЛОВИЕ)

    - Запросы создаются группами для таблиц Airlines, Passengers и Baggage.
    - На каждой итерации по количеству данных измеряется время выполнения запросов для трех таблиц.
    - Для каждого типа запроса на одном графике отображается зависимость между количеством данных и временем выполнения запроса для трех таблиц.
    - На графике каждый отдельный запрос из отдельного типа представлен как QUERY 1, QUERY 2, QUERY 3.
    - Запросы UPDATE на каждой итерации выполняются после запросов SELECT и DELETE.

    ------------

    - Все графики выводятся по мере выполнения исследования
    - Все графики сохраняются с соответствующими именами и доступны в папке images
    """
    def get_class_by_name(name, tables):
        """
            Возвращает класс таблицы по имени таблицы.

            Параметры
            ----------
            name : str
                Имя таблицы в нижнем регистре.

            tables : list
                Список классов таблиц для поиска.

            Возвращает
            ----------
            class
                Класс таблицы, соответствующий заданному имени.

            Исключения
            ----------
            ValueError
                Если класс таблицы с заданным именем не найден в списке tables.
        """
        for table in tables:
            if table.__name__.lower() == name:
                return table
        raise ValueError(f"Table class for {name} not found.")

    tables = [Airlines, Airport, AirportStaff, Passengers, Flights, Baggage, Tickets, SecurityCheck]
    '''
    create_sandbox()
    

    for table in tables:
        entries = table.generate(100)
        for entry in entries:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)

    # Исследуем время генерации данных для таблицы Airlines
    airlines_generation_times = []
    sizes = [5, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 150]  # Размеры для исследования
    for size in sizes:
        generation_time = measure_generation_time(Airlines, size)  # Измеряем время генерации данных для таблицы Airlines
        airlines_generation_times.append(generation_time)

    # Построение графика времени генерации данных для таблицы Airlines
    airlines_plot = PlotBuilder("Время генерации данных для таблицы Airlines", "Количество записей", "Время (секунды)")
    airlines_plot.add_line(sizes, airlines_generation_times, "Airlines")
    airlines_plot.save(os.path.join('images', "airlines_generation_time"))

    # Исследуем время генерации данных для связанных таблиц Flights и Airport
    flights_airport_generation_times = []
    for size in sizes:
        generation_time = measure_generation_time(Flights, size) + measure_generation_time(Airport, size)
        flights_airport_generation_times.append(generation_time)

    # Построение графика времени генерации данных для связанных таблиц Flights и Airport
    flights_airport_plot = PlotBuilder("Время генерации данных для таблиц Flights и Airport(FK)", "Количество записей", "Время (секунды)")
    flights_airport_plot.add_line(sizes, flights_airport_generation_times, "Flights and Airport")
    flights_airport_plot.save(os.path.join('images', "flights_airport_generation_time"))
    '''

    create_sandbox()

    for table in tables:
        entries = table.generate(100)
        for entry in entries:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)



    query_sizes = [50, 100, 200, 300, 500, 1000, 1500, 2000, 2500, 3000]  # Размеры запросов (количество строк)



    """
    select_queries = [
        ("SELECT * FROM airlines", "airlines", "id"),
        ("SELECT * FROM passengers", "passengers", "id"),
        ("SELECT * FROM baggage", "baggage", "id"),

        ("SELECT * FROM airlines WHERE name LIKE 'A%'", "airlines", "id"),
        ("SELECT * FROM passengers WHERE first_name LIKE 'J%'", "passengers", "id"),
        ("SELECT * FROM baggage WHERE flight_id LIKE 'FL%'", "baggage", "id"),

        ("SELECT * FROM airlines WHERE LENGTH(country) > 20", "airlines", "id"),
        ("SELECT * FROM baggage WHERE weight > 20", "baggage", "id"),
        ("SELECT * FROM passengers WHERE LENGTH(last_name) > 20", "passengers", "id")
    ]

    delete_queries = [
        ("DELETE FROM airlines", "airlines"),
        ("DELETE FROM passengers", "passengers"),
        ("DELETE FROM baggage", "baggage"),

        ("DELETE FROM airlines WHERE name LIKE 'A%'", "airlines"),
        ("DELETE FROM passengers WHERE first_name LIKE 'J%'", "passengers"),
        ("DELETE FROM baggage WHERE flight_id LIKE 'FL%'", "baggage"),

        ("DELETE FROM airlines WHERE LENGTH(country) > 20", "airlines"),
        ("DELETE FROM baggage WHERE weight > 20", "baggage"),
        ("DELETE FROM passengers WHERE LENGTH(last_name) > 20", "passengers")
    ]

    # Три группы запросов
    select_query_groups = [select_queries[:3], select_queries[3:6], select_queries[6:]]
    delete_query_groups = [delete_queries[:3], delete_queries[3:6], delete_queries[6:]]

    # Подготавливание для хранения всех времен выполнения запросов для разных размеров данных
    all_select_execution_times = {idx: {i: [] for i in range(len(group))} for idx, group in
                                  enumerate(select_query_groups, start=1)}
    all_delete_execution_times = {idx: {i: [] for i in range(len(group))} for idx, group in
                                  enumerate(delete_query_groups, start=1)}

    for size in query_sizes:
        # Удаление всех данных из таблиц
        with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
            delete_all_data(cursor, "airlines")
            delete_all_data(cursor, "passengers")
            delete_all_data(cursor, "baggage")

        # Генерация и сохранение новых данных
        entries_airlines = Airlines.generate(size)
        for entry in entries_airlines:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)
        entries_passengers = Passengers.generate(size)
        for entry in entries_passengers:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)
        entries_baggage = Baggage.generate(size)
        for entry in entries_baggage:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)

        with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
            # Выполнение и измерение времени выполнения SELECT запросов
            for idx, queries in enumerate(select_query_groups, start=1):
                for query_index, (query, table, identifier) in enumerate(queries):
                    #data = ensure_unique_identifiers(data, identifier, table, cursor, model_class)

                    # Получаем количество строк в таблице
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    row_count = cursor.fetchone()[0]

                    execution_time = measure_select_delete_query_time(query, cursor)

                    all_select_execution_times[idx][query_index].append((size, execution_time))

            # Выполнение и измерение времени выполнения DELETE запросов
            for idx, queries in enumerate(delete_query_groups, start=1):
                for query_index, (query, table) in enumerate(queries):
                    #data = ensure_unique_identifiers(data, identifier, table, cursor, model_class)

                    # Получаем количество строк в таблице
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    row_count_before = cursor.fetchone()[0]

                    execution_time = measure_select_delete_query_time(query, cursor)

                    # Получаем количество строк в таблице после выполнения запроса
                    cursor.execute(f"SELECT COUNT(*) FROM {table}")
                    row_count_after = cursor.fetchone()[0]

                    all_delete_execution_times[idx][query_index].append((size, execution_time))

    # Построение графиков для SELECT запросов
    k = 0
    for idx, query_results in all_select_execution_times.items():
        if k == 0:
            query_plot = PlotBuilder(f"Время выполнения запроса SELECT * FROM", "Количество запрашиваемых строк", "Время (секунды)")
        elif k == 1:
            query_plot = PlotBuilder(f"Время выполнения запроса SELECT * FROM WHERE LIKE", "Количество запрашиваемых строк", "Время (секунды)")
        elif k == 2:
            query_plot = PlotBuilder(f"Время выполнения запроса SELECT * FROM WHERE (Условие)", "Количество запрашиваемых строк", "Время (секунды)")
        for query_index, results in query_results.items():
            sizes, execution_times = zip(*results)
            table_name = select_query_groups[idx - 1][query_index][1]  # Получаем название таблицы
            query_plot.add_line(sizes, execution_times, table_name)

        query_plot.save(os.path.join('images', f"select_group_{idx}_queries_execution_time.png"))
        query_plot.show()
        k += 1

    k = 0
    # Построение графиков для DELETE запросов
    for idx, query_results in all_delete_execution_times.items():
        if k == 0:
            query_plot = PlotBuilder(f"Время выполнения запроса DELETE * FROM", "Количество удаляемых строк",
                                     "Время (секунды)")
        elif k == 1:
            query_plot = PlotBuilder(f"Время выполнения запроса DELETE * FROM WHERE LIKE",
                                     "Количество удаляемых строк", "Время (секунды)")
        elif k == 2:
            query_plot = PlotBuilder(f"Время выполнения запроса DELETE * FROM WHERE (Условие)",
                                     "Количество удаляемых строк", "Время (секунды)")
        for query_index, results in query_results.items():
            sizes, execution_times = zip(*results)
            table_name = delete_query_groups[idx - 1][query_index][1]  # Получаем название таблицы
            query_plot.add_line(sizes, execution_times, table_name)

        query_plot.save(os.path.join('images', f"delete_group_{idx}_queries_execution_time.png"))
        query_plot.show()
        k += 1
    """
    update_queries = [
        ("UPDATE airlines SET country = 'UpdatedCountry'", "airlines"),
        ("UPDATE passengers SET contact_info = 'updated@example.com'", "passengers"),
        ("UPDATE baggage SET weight = weight + 1", "baggage"),

        ("UPDATE airlines SET country = 'UpdatedCountry' WHERE name LIKE 'A%'", "airlines"),
        ("UPDATE passengers SET contact_info = 'updated@example.com' WHERE first_name LIKE 'J%'", "passengers"),
        ("UPDATE baggage SET weight = weight + 1 WHERE flight_id LIKE 'FL%'", "baggage"),

        ("UPDATE airlines SET country = 'UpdatedCountry' WHERE LENGTH(country) > 20", "airlines"),
        ("UPDATE passengers SET contact_info = 'updated@example.com' WHERE LENGTH(last_name) > 20", "passengers"),
        ("UPDATE baggage SET weight = weight + 1 WHERE weight > 20", "baggage")
    ]

    update_query_groups = [update_queries[:3], update_queries[3:6], update_queries[6:]]

    all_update_execution_times = {idx: {i: [] for i in range(len(group))} for idx, group in
                                  enumerate(update_query_groups, start=1)}

    for size in query_sizes:
        # Удаление всех данных из таблиц и их предварительное заполнение
        with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
            delete_all_data(cursor, "airlines")
            delete_all_data(cursor, "passengers")
            delete_all_data(cursor, "baggage")

        # Генерация и сохранение новых данных
        entries_airlines = Airlines.generate(size)
        for entry in entries_airlines:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)
        entries_passengers = Passengers.generate(size)
        for entry in entries_passengers:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)
        entries_baggage = Baggage.generate(size)
        for entry in entries_baggage:
            with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                entry.save(cursor)

        with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
            # Выполнение и измерение времени выполнения UPDATE запросов
            for idx, queries in enumerate(update_query_groups, start=1):
                for query_index, (query, table) in enumerate(queries):
                    execution_time = measure_select_delete_query_time(query, cursor)
                    all_update_execution_times[idx][query_index].append((size, execution_time))

    k = 0
    # Построение графиков для UPDATE запросов
    for idx, query_results in all_update_execution_times.items():
        if k == 0:
            query_plot = PlotBuilder(f"Время выполнения запроса UPDATE", "Количество обновляемых строк",
                                     "Время (секунды)")
        elif k == 1:
            query_plot = PlotBuilder(f"Время выполнения запроса UPDATE WHERE LIKE",
                                     "Количество обновляемых строк", "Время (секунды)")
        elif k == 2:
            query_plot = PlotBuilder(f"Время выполнения запроса UPDATE WHERE (Условие)",
                                     "Количество обновляемых строк", "Время (секунды)")
        for query_index, results in query_results.items():
            sizes, execution_times = zip(*results)
            table_name = update_query_groups[idx - 1][query_index][1]
            query_plot.add_line(sizes, execution_times, table_name)

        query_plot.save(os.path.join('images', f"update_group_{idx}_queries_execution_time.png"))
        query_plot.show()
        k += 1


#research()



# with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
#      cursor.execute(Tickets.create_table())

#with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
#   delete_all_data(cursor, 'airport')

# with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
#    replace_all_data(cursor, 'airport', Airport)

#backup_database('localhost', 'root', 'root', 'sandbox_mydb', 'backup.sql')
#restore_database('localhost', 'root', 'root', 'sandbox_mydb', 'backup.sql')

def generate_all_data(size):
    """
        Функция генерирует данные для всех таблиц и сохраняет их в базу данных.

        Параметры
        ----------
        size : int
            Количество записей для генерации в каждой таблице.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = Airlines.generate(size)
        for entry in entries:
            entry.save(cursor)

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = Airport.generate(size)
        for entry in entries:
            entry.save(cursor)

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = AirportStaff.generate(size)
        for entry in entries:
            entry.save(cursor)

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = Passengers.generate(size)
        for entry in entries:
            entry.save(cursor)

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = Flights.generate(size)
        for entry in entries:
            entry.save(cursor)

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = Baggage.generate(size)
        for entry in entries:
            entry.save(cursor)

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = Tickets.generate(size)
        for entry in entries:
            entry.save(cursor)

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        entries = SecurityCheck.generate(size)
        for entry in entries:
            entry.save(cursor)


def generate_all_tables():
    """
        Функция создает все таблицы в базе данных.
    """
    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(Airlines.create_table())

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(Airport.create_table())

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(AirportStaff.create_table())

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(Passengers.create_table())

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(Flights.create_table())

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(Baggage.create_table())

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(Tickets.create_table())

    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
        cursor.execute(SecurityCheck.create_table())

#generate_all_tables()
#generate_all_data(20)
#research()

# entries = Airlines.generate(5)
# for entry in entries:
#     entry.save()

# entries = AirportStaff.generate(5)
# for entry in entries:
#     entry.save()

# entries = Passengers.generate(5)
# for entry in entries:
#     entry.save()

# entries = Flights.generate(5)
# for entry in entries:
#     entry.save()

# entries = Baggage.generate(5)
# for entry in entries:
#     entry.save()

# entries = Tickets.generate(5)
# for entry in entries:
#     entry.save()

# entries = SecurityCheck.generate(5)
# for entry in entries:
#     entry.save()


# with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
#     cursor.execute(SecurityCheck.create_table())
# a, b = Tickets.create_table()
# with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
#     cursor.execute(a)
#     cursor.execute(b)


#create_sandbox()