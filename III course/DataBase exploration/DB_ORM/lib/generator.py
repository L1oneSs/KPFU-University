import datetime
import random
import string

import mysql
import mysql.connector

from lib.db_connection import DatabaseConnection


def generate_random_value(data_type, max_length=None):
    """
    Генерирует случайное значение в соответствии с указанным типом данных.

    Args:
        data_type (str): Тип данных для генерации значения ('varchar', 'int', 'float', 'datetime').
        max_length (int, optional): Максимальная длина значения для типа данных 'varchar'.

    Returns:
        generator: Генератор, возвращающий случайные значения в соответствии с указанным типом данных.

    """
    while True:
        if data_type == "varchar":
            if max_length:
                max_length = int(max_length)
                yield ''.join(random.choices(string.ascii_letters + string.digits, k=max_length))
            else:
                yield ''.join(random.choices(string.ascii_letters + string.digits, k=10))
        elif data_type == "int":
            if max_length:
                max_length = int(max_length)
                yield random.randint(0, 10 ** max_length - 1)
            else:
                yield random.randint(0, 10000)
        elif data_type == "float":
            if max_length:
                max_length = int(max_length)
                yield round(random.uniform(0, 10 ** max_length - 1), 2)
            else:
                yield round(random.uniform(0, 1000), 2)
        elif data_type == "datetime":
            yield datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        else:
            yield None


def generate_records(selected_table, selected_db, host, user, password, fetch_num_records=None, no_run=False):
    """
    Генерирует указанное количество записей в указанной таблице базы данных.

    Args:
        selected_table (str): Имя таблицы, в которой будут генерироваться записи.
        selected_db (str): Имя базы данных, в которой находится таблица.
        host (str): Хост базы данных.
        user (str): Имя пользователя для доступа к базе данных.
        password (str): Пароль пользователя для доступа к базе данных.
        fetch_num_records (int, optional): Количество записей для генерации. По умолчанию None.
        no_run (bool, optional): Флаг, указывающий на то, следует ли выполнять SQL-запросы.
                                 Если True, метод возвращает запрос и значения записей. По умолчанию False.

    Returns:
        str or None: Если no_run=True, возвращает SQL-запрос и значения записей, иначе None.

    """
    try:
        with DatabaseConnection(host=host, user=user, password=password, database=selected_db) as (
                mycursor, connection):
            # Получение структуры таблицы
            mycursor.execute(f"DESCRIBE {selected_table}")
            table_structure = [(row[0], row[1], row[2]) for row in mycursor.fetchall()]

            num_records = fetch_num_records

            # Генерация случайных данных для каждой записи
            for _ in range(num_records):
                record_values = []
                for column in table_structure:
                    name, column_type, _ = column
                    length_or_size = None
                    if '(' in column_type and ')' in column_type:
                        # Ищем значение в скобках
                        length_or_size = column_type[column_type.find('(') + 1:column_type.find(')')]
                        # Убираем скобки и значение из column_type
                        column_type = column_type[:column_type.find('(')]
                    generator = generate_random_value(column_type, length_or_size)
                    record_values.append(next(generator))

                # Вставка сгенерированной записи
                placeholders = ', '.join(['%s'] * len(record_values))
                insert_query = f"INSERT INTO {selected_table} VALUES ({placeholders})"

                # Проверка наличия записи с таким же id и повторная генерация id в случае конфликта
                id_column_index = None
                for i, (name, _, _) in enumerate(table_structure):
                    if name.lower() == 'id':
                        id_column_index = i
                        break

                if id_column_index is not None:
                    while True:
                        try:
                            if no_run:
                                return insert_query, record_values
                            mycursor.execute(insert_query, record_values)
                            break  # Выход из цикла, если вставка выполнена успешно
                        except mysql.connector.IntegrityError as e:
                            if e.errno == 1062:  # Ошибка уникальности ключа
                                record_values[id_column_index] = next(generate_random_value('int'))  # Повторная генерация id
                            else:
                                raise e  # Пробрасываем другие ошибки
                else:
                    print("Столбец 'id' не найден в структуре таблицы.")

        print(f"Сгенерировано и вставлено {num_records} записей в таблицу {selected_table}.")

    except mysql.connector.Error as err:
        print("Ошибка при генерации записей:", err.msg)
