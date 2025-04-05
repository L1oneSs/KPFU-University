import mysql.connector
from colorama import Fore


class DatabaseConnection:
    """
    Класс для управления соединением с базой данных MySQL.

    Attributes:
        host (str): Хост базы данных.
        user (str): Пользователь базы данных.
        password (str): Пароль пользователя базы данных.
        database (str): Название базы данных.
        connection: Объект подключения к базе данных.
        cursor: Объект курсора для выполнения запросов к базе данных.
    """

    def __init__(self, host, user, password, database):
        """
        Инициализирует объект DatabaseConnection с указанными параметрами подключения.

        Args:
            host (str): Хост базы данных.
            user (str): Пользователь базы данных.
            password (str): Пароль пользователя базы данных.
            database (str): Название базы данных.
        """
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def __enter__(self):
        """
        Метод контекстного менеджера для получения соединения с базой данных.

        Returns:
            tuple: Кортеж, содержащий объект курсора и соединение с базой данных.
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.cursor = self.connection.cursor()
            return self.cursor, self.connection
        except mysql.connector.Error as err:
            print(Fore.RED + "Ошибка при подключении к базе данных:", err.msg)
            print(Fore.RESET)
            raise

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Метод контекстного менеджера для закрытия соединения с базой данных.

        Args:
            exc_type: Тип исключения.
            exc_val: Значение исключения.
            exc_tb: Трассировка исключения.
        """
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.commit()
            self.connection.close()
