import mysql.connector
from colorama import Fore
from investigations.graphics import create_graphics
from investigations.query_time import measure_query_time
from lib.database_methods import create_database, delete_database, edit_database, create_sandbox_database
from lib.db_connection import DatabaseConnection

# Глобальные переменные для хранения параметров подключения
host = None
user = None
password = None

def main():
    """
    Основная функция для управления программой.

    Функция дает пользователю выбор команды
    """
    global host, user, password
    print("Подключение\n")
    host = input("Введите хост: ")
    user = input("Введите пользователя: ")
    password = input("Введите пароль: ")

    try:
        with DatabaseConnection(host=host, user=user, password=password, database="mysql") as (_, connection):
            print("Подключение к базе данных успешно.")
    except mysql.connector.Error:
        print(Fore.RESET)
        return

    while True:
        print(Fore.YELLOW + "<== Вы всегда можете отменить первую команду, написав в консоль back для возврата в меню "
                            "==>\n")
        print(Fore.RESET)
        print("""Доступные команды:
        1. Создать базу данных
        2. Удалить базу данных
        3. Редактировать базу данных
        4. Песочница
        5. Время
        6. График
        7. Меню
        """)
        type_in = input("Выберите номер команды: ")

        if type_in == "1":
            create_database(host, user, password)
        elif type_in == "2":
            delete_database(host, user, password)
        elif type_in == "3":
            edit_database(host, user, password)
        elif type_in == "4":
            create_sandbox_database(host, user, password)
        elif type_in == "5":
            measure_query_time(host, user, password)
        elif type_in == "6":
            type_in_graph = input("Выберите номер действия:\n1. Запросы\n2. Генерация\n")
            if type_in_graph != '1' and type_in_graph != '2':
                print(Fore.RED + "Ошибка: Неподдерживаемая команда.")
                print(Fore.RESET)
            else:
                create_graphics(type_in_graph)
        elif type_in == "7" or type_in == "back":
            continue
        else:
            print(Fore.RED + "Некорректная команда")
            print(Fore.RESET)

if __name__ == "__main__":
    main()
