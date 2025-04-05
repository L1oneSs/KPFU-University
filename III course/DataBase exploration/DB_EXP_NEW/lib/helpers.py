"""
Модуль helpers предоставляет вспомогательные функции для работы с данными и взаимодействием с базой данных.
"""

def get_identifiers(data, identifier):
    """
        Возвращает список значений указанного идентификатора(pk) для каждого элемента в данных.

        Параметры
        ----------
        data : list
            Список объектов данных.
        identifier : str
            Имя идентификатора для извлечения значений.

        Возвращает
        ----------
        list
            Список значений идентификатора.
    """
    return [getattr(entry, identifier) for entry in data]

def fetch_existing_pks(cursor, table, identifier):
    """
        Извлекает существующие первичные ключи из указанной таблицы.

        Параметры
        ----------
        cursor : mysql.connector.cursor.MySQLCursor
            Курсор для выполнения операций с базой данных.
        table : str
            Название таблицы.
        identifier : str
            Имя столбца идентификатора.

        Возвращает
        ----------
        set
            Множество значений существующих первичных ключей.
    """
    cursor.execute(f"SELECT {identifier} FROM {table}")
    return {row[0] for row in cursor.fetchall()}

def ensure_unique_identifiers(data, identifier, table, cursor, model_class):
    """
        Обеспечивает уникальность идентификаторов в данных путем их перегенерации, если они уже существуют в таблице.

        Параметры
        ----------
        data : list
            Список объектов данных.
        identifier : str
            Имя идентификатора для проверки уникальности.
        table : str
            Название таблицы.
        cursor : mysql.connector.cursor.MySQLCursor
            Курсор для выполнения операций с базой данных.
        model_class : type
            Класс модели для генерации новых объектов.

        Возвращает
        ----------
        list
            Список объектов данных с уникальными идентификаторами.
    """
    existing_pks = fetch_existing_pks(cursor, table, identifier)
    unique_pks = set(get_identifiers(data, identifier))

    new_data = []

    for entry in data:
        pk = getattr(entry, identifier)
        while pk in unique_pks or pk in existing_pks:
            entry = model_class.generate(1)[0]  # Перегенерация объекта
            pk = getattr(entry, identifier)
        unique_pks.add(pk)
        new_data.append(entry)

    return new_data

def format_data(data, query):
    """
        Форматирует данные в соответствии с количеством плейсхолдеров %s в SQL-запросе.

        Параметры
        ----------
        data : list
            Список объектов данных.
        query : str
            SQL-запрос с плейсхолдерами (%s).

        Возвращает
        ----------
        list
            Список отформатированных данных в виде кортежей.

        Исключения
        ----------
        ValueError
            Если количество данных не соответствует количеству плейсхолдеров в запросе.
    """
    placeholders = query.count("%s")
    formatted = []
    for entry in data:
        entry_data = tuple(getattr(entry, field) for field in entry.__dict__.keys() if not field.startswith('_'))
        if len(entry_data) == placeholders:
            formatted.append(entry_data)
        else:
            print(f"Expected {placeholders} fields, but got {len(entry_data)}: {entry_data}")
            raise ValueError("Data length does not match placeholders in query")
    return formatted

