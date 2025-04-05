"""
    Модуль table_methods предоставляет функции для работы с таблицами в базе данных:
    1) Получение информации о таблицах
    2) Замена данных
    3) Удаление данных
"""
def get_table_columns(cursor, table_name):
    """
        Получает информацию о столбцах указанной таблицы.

        Параметры
        ----------
        cursor : mysql.connector.cursor.MySQLCursor
            Курсор для выполнения операций с базой данных.
        table_name : str
            Название таблицы.

        Возвращает
        ----------
        list
            Список столбцов таблицы.

        Формат:

        [('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment'), ('name', 'varchar(255)', 'YES', '', None, '')]
    """
    cursor.execute(f"SHOW COLUMNS FROM {table_name}")
    columns = cursor.fetchall()
    return columns



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

def delete_all_data(cursor, table_name):
    """
        Удаляет все данные из указанной таблицы.

        Параметры
        ----------
        cursor : mysql.connector.cursor.MySQLCursor
            Курсор для выполнения операций с базой данных.
        table_name : str
            Название таблицы.
    """
    cursor.execute(f"DELETE FROM {table_name}")


def replace_all_data(cursor, table_name, model_class):
    """
        Заменяет все данные в указанной таблице сгенерированными данными на основе переданного класса модели.

        Параметры
        ----------
        cursor : mysql.connector.cursor.MySQLCursor
            Курсор для выполнения операций с базой данных.
        table_name : str
            Название таблицы.
        model_class : type
            Класс модели для генерации новых данных.
    """
    # Получаем количество строк в таблице
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cursor.fetchone()[0]

    # Удаляем все данные из таблицы
    delete_all_data(cursor, table_name)

    # Генерируем данные
    data = model_class.generate(row_count)

    # Вставляем сгенерированные данные обратно в таблицу
    columns = ', '.join(data[0]._fields.keys())
    values_placeholder = ', '.join(['%s'] * len(data[0]._fields))
    query = f"INSERT INTO {table_name} ({columns}) VALUES ({values_placeholder})"
    values = [tuple(getattr(item, field) for field in item._fields) for item in data]
    cursor.executemany(query, values)