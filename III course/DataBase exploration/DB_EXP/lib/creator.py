from lib.generators import (
    airlines_generator, airport_generator, airportstaff_generator,
    baggage_generator, flights_generator, passengers_generator,
    securitycheck_generator, tickets_generator
)


def create_table_entry(table_name, counter, mycursor):
    """
    Создает новые записи в указанной таблице базы данных.

    Функция создает новые записи в таблице, основываясь на имени таблицы и количестве записей.

    Parameters:
        table_name (str): Имя таблицы, в которую нужно добавить записи.
        counter (int): Количество записей, которое нужно создать.
        mycursor (MySQLCursor): Курсор для выполнения операций с базой данных.

    Raises:
        MySQLInterfaceError: Если произошла ошибка при выполнении запросов к базе данных.
    """
    generator_mapping = {
        "airlines": airlines_generator,
        "airport": airport_generator,
        "airportstaff": airportstaff_generator,
        "baggage": baggage_generator,
        "flights": flights_generator,
        "passengers": passengers_generator,
        "securitycheck": securitycheck_generator,
        "tickets": tickets_generator
    }

    if table_name in generator_mapping:
        generator_func = generator_mapping[table_name]
        for _ in range(counter):
            data_gen = generator_func(mycursor)
            try:
                data = next(data_gen)
            except StopIteration:
                data_gen = generator_func(mycursor)
                data = next(data_gen)

            placeholders = ', '.join(['%s'] * len(data))
            columns = ', '.join(data.keys())
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            mycursor.execute(sql, tuple(data.values()))
    else:
        raise ValueError(f"Table '{table_name}' not found in generator mapping")
