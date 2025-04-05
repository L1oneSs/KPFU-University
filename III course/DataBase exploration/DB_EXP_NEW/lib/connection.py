"""
    Модуль connection предоставляет функциональность для управления подключением к базе данных MySQL с
    использованием контекстного менеджера. Этот модуль содержит один класс `DatabaseConnection`.
"""

import mysql.connector

class DatabaseConnection:
    """
        Класс для управления подключением к базе данных MySQL.

        Параметры
        ----------
        host : str
            Хост базы данных.
        user : str
            Имя пользователя базы данных.
        password : str
            Пароль пользователя базы данных.
        database : str
            Название базы данных.

        Атрибуты
        ----------
        host : str
            Хост базы данных.
        user : str
            Имя пользователя базы данных.
        password : str
            Пароль пользователя базы данных.
        database : str
            Название базы данных.
        connection : mysql.connector.connection.MySQLConnection, optional
            Объект соединения с базой данных.
        cursor : mysql.connector.cursor.MySQLCursor, optional
            Курсор для выполнения операций с базой данных.

        Методы
        ----------
        __enter__()
            Открывает подключение к базе данных и возвращает курсор и соединение.
        __exit__(exc_type, exc_val, exc_tb)
            Закрывает курсор и соединение, коммитит транзакции, если они есть.
    """

    def __init__(self, host, user, password, database):
        """
            Инициализация объекта DatabaseConnection.

            Параметры
            ----------
            host : str
                Хост базы данных.
            user : str
                Имя пользователя базы данных.
            password : str
                Пароль пользователя базы данных.
            database : str
                Название базы данных.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.cursor = None

    def __enter__(self):
        """
            Открывает подключение к базе данных и возвращает курсор и соединение.

            Возвращает
            ----------
            tuple
                Кортеж, содержащий курсор и соединение.
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
            Закрывает курсор и соединение, коммитит транзакции, если они есть.

            Параметры
            ----------
            exc_type : type
                Тип исключения.
            exc_val : Exception
                Значение исключения.
            exc_tb : traceback
                Объект трассировки исключения.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.commit()
            self.connection.close()