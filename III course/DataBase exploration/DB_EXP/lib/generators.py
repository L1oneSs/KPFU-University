import random
import string
from colorama import Fore


def airlines_generator(mycursor):
    names = ["Delta Air Lines", "American Airlines", "United Airlines", "Lufthansa", "Emirates", "Southwest Airlines",
             "Southern Airlines", "Air France", "British Airways", "Qatar Airways", "Singapore Airlines",
             "Cathay Pacific Airways", "Turkish Airlines", "Ryanair", "ANA All Nippon Airways"]

    countries = ["USA", "Germany", "UAE", "China", "France", "UK", "Qatar", "Singapore", "Japan", "South Korea",
                 "Canada", "Australia", "Netherlands", "Italy", "Spain", "Brazil", "India", "Mexico", "Russia",
                 "Turkey", "Indonesia", "Switzerland", "Thailand", "Sweden", "Norway"]

    while True:
        name = random.choice(names)
        country = random.choice(countries)

        if len(name) <= 45 and len(country) <= 45:
            break

    entry = {
        "name": name,
        "code": ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=random.randint(2, 3))),
        "country": country
    }

    yield entry


def airport_generator(mycursor):
    city_country = {
        "New York": "USA",
        "London": "UK",
        "Paris": "France",
        "Tokyo": "Japan",
        "Beijing": "China",
        "Moscow": "Russia",
        "Dubai": "UAE",
        "Singapore": "Singapore",
        "Sydney": "Australia",
        "Berlin": "Germany",
        "Rome": "Italy",
        "Madrid": "Spain",
        "Toronto": "Canada",
        "Mexico City": "Mexico",
        "Seoul": "South Korea"
    }

    while True:
        code = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ', k=3))
        city, country = random.choice(list(city_country.items()))

        if len(city) <= 45 and len(country) <= 45:
            break

    entry = {
        "code": code,
        "name": ''.join(random.choices(string.ascii_uppercase, k=random.randint(5, 15))),
        "city": city,
        "country": country
    }

    yield entry


def airportstaff_generator(mycursor):
    job_titles = ["chapter", "cook", "cleaner", "manager", "pilot",
                  "flight attendant", "security officer", "dispatcher",
                  "technician", "engineer", "baggage handler",
                  "customer service agent", "ramp agent", "mechanic",
                  "inspector", "supervisor", "cashier", "administrator"]

    mycursor.execute("SELECT code FROM airport")
    airport_codes = [row[0] for row in mycursor.fetchall()]

    while True:
        first_name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 44)))
        last_name = ''.join(random.choices(string.ascii_uppercase, k=random.randint(1, 44)))
        job_title = random.choice(job_titles)
        contact_info = '8' + ''.join(random.choices(string.digits, k=11))
        airport_code = random.choice(airport_codes)

        if len(job_title) <= 45:
            break

    entry = {
        "first_name": first_name,
        "last_name": last_name,
        "job_title": job_title,
        "contact_info": contact_info,
        "airport_code": airport_code
    }

    yield entry


def baggage_generator(mycursor):
    mycursor.execute("SELECT id FROM flights")
    flight_ids = [row[0] for row in mycursor.fetchall()]

    mycursor.execute("SELECT id FROM passengers")
    passenger_ids = [row[0] for row in mycursor.fetchall()]

    while True:
        flight_id = random.choice(flight_ids)
        weight = random.randint(1, 1000)
        passenger_id = random.choice(passenger_ids)

        entry = {
            "flight_id": flight_id,
            "weight": weight,
            "passenger_id": passenger_id
        }

        yield entry


def flights_generator(mycursor):
    mycursor.execute("SELECT id FROM airlines")
    airline_ids = [row[0] for row in mycursor.fetchall()]

    mycursor.execute("SELECT code FROM airport")
    airport_codes = [row[0] for row in mycursor.fetchall()]

    while True:
        departure_time = "{:02d}:{:02d}:00".format(random.randint(0, 23), random.randint(0, 59))
        arrival_time = "{:02d}:{:02d}:00".format(random.randint(0, 23), random.randint(0, 59))
        flight_status = random.choice(["arrived", "departed", "flying"])
        airline_id = random.choice(airline_ids)
        origin_airport_code = random.choice(airport_codes)
        destination_airport_code = random.choice(airport_codes)

        entry = {
            "departure_time": departure_time,
            "arrival_time": arrival_time,
            "flight_status": flight_status,
            "airline_id": airline_id,
            "origin_airport_code": origin_airport_code,
            "destination_airport_code": destination_airport_code
        }

        yield entry


def passengers_generator(mycursor):
    while True:
        first_name = random.choice(string.ascii_uppercase) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(0, 44)))
        last_name = random.choice(string.ascii_uppercase) + ''.join(random.choices(string.ascii_lowercase, k=random.randint(0, 44)))
        passport_number = ''.join(random.choices(string.digits, k=9))
        contact_info = '8' + ''.join(random.choices(string.digits, k=10))

        entry = {
            "first_name": first_name,
            "last_name": last_name,
            "passport_number": passport_number,
            "contact_info": contact_info
        }

        yield entry


def securitycheck_generator(mycursor):
    mycursor.execute("SELECT id FROM flights")
    flight_ids = [row[0] for row in mycursor.fetchall()]

    mycursor.execute("SELECT id FROM tickets")
    ticket_ids = [row[0] for row in mycursor.fetchall()]

    while True:
        check_time = "{:02d}:{:02d}".format(random.randint(0, 23), random.randint(0, 59))
        result = random.choice(["deny", "pass"])
        flight_id = random.choice(flight_ids)
        ticket_id = random.choice(ticket_ids)

        entry = {
            "check_time": check_time,
            "result": result,
            "flight_id": flight_id,
            "tickets_id": ticket_id
        }

        yield entry


def tickets_generator(mycursor):
    """
    Генерирует данные для таблицы tickets.

    Генерирует случайные номера мест, статусы билетов, id пассажиров и id рейсов, а также случайные стоимости билетов.

    Parameters:
        mycursor (MySQLCursor): Курсор для выполнения операций с базой данных.

    Yields:
        dict: Словарь с данными для вставки в таблицу. Содержит ключи 'seat_number', 'ticket_status',
            'passenger_id', 'flight_id' и 'cost'.
    """
    while True:
        # Генерация случайного номера места
        seat_number = ''.join(random.choices(string.digits, k=random.randint(2, 3))) + random.choice(
            string.ascii_uppercase)

        # Случайный выбор статуса билета
        ticket_status = random.choice(["deny", "pass"])

        # Получение всех id пассажиров из таблицы passengers
        mycursor.execute("SELECT id FROM passengers")
        passenger_ids = [row[0] for row in mycursor.fetchall()]

        if not passenger_ids:
            print(Fore.RED + "Ошибка: Невозможно создать запись в таблице (passenger_ids).")
            print(Fore.RESET)
            return

        # Выбор случайного id пассажира
        passenger_id = random.choice(passenger_ids)

        # Получение всех id рейсов из таблицы flights
        mycursor.execute("SELECT id FROM flights")
        flight_ids = [row[0] for row in mycursor.fetchall()]

        if not flight_ids:
            print(Fore.RED + "Ошибка: Невозможно создать запись в таблице (flight_ids).")
            print(Fore.RESET)
            return

        # Выбор случайного id рейса
        flight_id = random.choice(flight_ids)

        # Генерация случайной стоимости билета
        cost = random.randint(1000, 100000)

        # Создание словаря с данными записи
        entry = {
            "seat_number": seat_number,
            "ticket_status": ticket_status,
            "passenger_id": passenger_id,
            "flight_id": flight_id,
            "cost": cost
        }

        yield entry

