import mysql.connector

from lib.generators import airlines_generator, airport_generator, airportstaff_generator, baggage_generator, \
    flights_generator, passengers_generator, securitycheck_generator, tickets_generator

# Создаем соединение с базой данных
connection = mysql.connector.connect(host="localhost", user="root", password="root", database="mydb")
mycursor = connection.cursor()


def test_airlines_generator():
    generator = airlines_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "name" in entry
    assert "code" in entry
    assert "country" in entry


def test_airport_generator():
    generator = airport_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "code" in entry
    assert "name" in entry
    assert "city" in entry
    assert "country" in entry


def test_airportstaff_generator():
    generator = airportstaff_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "first_name" in entry
    assert "last_name" in entry
    assert "job_title" in entry
    assert "contact_info" in entry
    assert "airport_code" in entry


def test_baggage_generator():
    generator = baggage_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "flight_id" in entry
    assert "weight" in entry
    assert "passenger_id" in entry


def test_flights_generator():
    generator = flights_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "departure_time" in entry
    assert "arrival_time" in entry
    assert "flight_status" in entry
    assert "airline_id" in entry
    assert "origin_airport_code" in entry
    assert "destination_airport_code" in entry


def test_passengers_generator():
    generator = passengers_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "first_name" in entry
    assert "last_name" in entry
    assert "passport_number" in entry
    assert "contact_info" in entry


def test_securitycheck_generator():
    generator = securitycheck_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "check_time" in entry
    assert "result" in entry
    assert "flight_id" in entry
    assert "tickets_id" in entry


def test_tickets_generator():
    generator = tickets_generator(mycursor)
    entry = next(generator)
    assert isinstance(entry, dict)
    assert "seat_number" in entry
    assert "ticket_status" in entry
    assert "passenger_id" in entry
    assert "flight_id" in entry
    assert "cost" in entry


# Выполнение ручных тестов
test_airlines_generator()
test_airport_generator()
test_airportstaff_generator()
test_baggage_generator()
test_flights_generator()
test_passengers_generator()
test_securitycheck_generator()
test_tickets_generator()
print("Все тесты успешно пройдены")

# Закрываем соединение с базой данных
mycursor.close()
connection.close()
