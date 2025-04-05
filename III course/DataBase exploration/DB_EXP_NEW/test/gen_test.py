"""
Модуль gen_test предназначен для тестирования генерации экземпляров классов из модуля lib.class_basis.

Каждая функция тестирования проверяет корректность работы метода generate для конкретного класса.

Примеры использования:
    test_generate_airlines(): Тестирует генерацию экземпляров класса Airlines.
    test_generate_airport(): Тестирует генерацию экземпляров класса Airport.
    test_generate_airport_staff(): Тестирует генерацию экземпляров класса AirportStaff.
    test_generate_baggage(): Тестирует генерацию экземпляров класса Baggage.
    test_generate_flights(): Тестирует генерацию экземпляров класса Flights.
    test_generate_passengers(): Тестирует генерацию экземпляров класса Passengers.
    test_generate_security_check(): Тестирует генерацию экземпляров класса SecurityCheck.
    test_generate_tickets(): Тестирует генерацию экземпляров класса Tickets.

Каждая функция выводит сообщение "test_passed" в случае успешного прохождения теста.
"""

from lib.class_basis import Airlines, Airport, AirportStaff, Baggage, Flights, Passengers, SecurityCheck, Tickets

def test_generate_airlines():
    """
        Тестирует генерацию экземпляров класса Airlines.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: id, name, code, country.

        Выводит сообщение "test_generate_airlines passed." при успешном прохождении теста.
    """
    airlines_gen = Airlines.generate(1)
    airline_instance = next(airlines_gen)

    assert isinstance(airline_instance, Airlines), "Сгенерированный объект не является экземпляром Airlines."
    assert hasattr(airline_instance, 'id'), "Сгенерированный объект не содержит атрибут 'id'."
    assert hasattr(airline_instance, 'name'), "Сгенерированный объект не содержит атрибут 'name'."
    assert hasattr(airline_instance, 'code'), "Сгенерированный объект не содержит атрибут 'code'."
    assert hasattr(airline_instance, 'country'), "Сгенерированный объект не содержит атрибут 'country'."

    print("test_generate_airlines passed.")

def test_generate_airport():
    """
        Тестирует генерацию экземпляров класса Airport.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: code, name, city, country.

        Выводит сообщение "test_generate_airport passed." при успешном прохождении теста.
    """
    airport_gen = Airport.generate(1)
    airport_instance = next(airport_gen)

    assert isinstance(airport_instance, Airport), "Сгенерированный объект не является экземпляром Airport."
    assert hasattr(airport_instance, 'code'), "Сгенерированный объект не содержит атрибут 'code'."
    assert hasattr(airport_instance, 'name'), "Сгенерированный объект не содержит атрибут 'name'."
    assert hasattr(airport_instance, 'city'), "Сгенерированный объект не содержит атрибут 'city'."
    assert hasattr(airport_instance, 'country'), "Сгенерированный объект не содержит атрибут 'country'."

    print("test_generate_airport passed.")

def test_generate_airport_staff():
    """
        Тестирует генерацию экземпляров класса AirportStaff.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: id, first_name, last_name, job_title, contact_info, airport_code.

        Выводит сообщение "test_generate_airport_staff passed." при успешном прохождении теста.
    """
    airport_staff_gen = AirportStaff.generate(1)
    airport_staff_instance = next(airport_staff_gen)

    assert isinstance(airport_staff_instance, AirportStaff), "Сгенерированный объект не является экземпляром AirportStaff."
    assert hasattr(airport_staff_instance, 'id'), "Сгенерированный объект не содержит атрибут 'id'."
    assert hasattr(airport_staff_instance, 'first_name'), "Сгенерированный объект не содержит атрибут 'first_name'."
    assert hasattr(airport_staff_instance, 'last_name'), "Сгенерированный объект не содержит атрибут 'last_name'."
    assert hasattr(airport_staff_instance, 'job_title'), "Сгенерированный объект не содержит атрибут 'job_title'."
    assert hasattr(airport_staff_instance, 'contact_info'), "Сгенерированный объект не содержит атрибут 'contact_info'."
    assert hasattr(airport_staff_instance, 'airport_code'), "Сгенерированный объект не содержит атрибут 'airport_code'."

    print("test_generate_airport_staff passed.")

def test_generate_baggage():
    """
        Тестирует генерацию экземпляров класса Baggage.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: id, flight_id, weight, passenger_id.

        Выводит сообщение "test_generate_baggage passed." при успешном прохождении теста.
    """
    baggage_gen = Baggage.generate(1)
    baggage_instance = next(baggage_gen)

    assert isinstance(baggage_instance, Baggage), "Сгенерированный объект не является экземпляром Baggage."
    assert hasattr(baggage_instance, 'id'), "Сгенерированный объект не содержит атрибут 'id'."
    assert hasattr(baggage_instance, 'flight_id'), "Сгенерированный объект не содержит атрибут 'flight_id'."
    assert hasattr(baggage_instance, 'weight'), "Сгенерированный объект не содержит атрибут 'weight'."
    assert hasattr(baggage_instance, 'passenger_id'), "Сгенерированный объект не содержит атрибут 'passenger_id'."

    print("test_generate_baggage passed.")

def test_generate_flights():
    """
        Тестирует генерацию экземпляров класса Flights.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: id, departure_time, arrival_time, flight_status, airline_id, origin_airport_code, destination_airport_code.

        Выводит сообщение "test_generate_flights passed." при успешном прохождении теста.
    """
    flights_gen = Flights.generate(1)
    flights_instance = next(flights_gen)

    assert isinstance(flights_instance, Flights), "Сгенерированный объект не является экземпляром Flights."
    assert hasattr(flights_instance, 'id'), "Сгенерированный объект не содержит атрибут 'id'."
    assert hasattr(flights_instance, 'departure_time'), "Сгенерированный объект не содержит атрибут 'departure_time'."
    assert hasattr(flights_instance, 'arrival_time'), "Сгенерированный объект не содержит атрибут 'arrival_time'."
    assert hasattr(flights_instance, 'flight_status'), "Сгенерированный объект не содержит атрибут 'flight_status'."
    assert hasattr(flights_instance, 'airline_id'), "Сгенерированный объект не содержит атрибут 'airline_id'."
    assert hasattr(flights_instance, 'origin_airport_code'), "Сгенерированный объект не содержит атрибут 'origin_airport_code'."
    assert hasattr(flights_instance, 'destination_airport_code'), "Сгенерированный объект не содержит атрибут 'destination_airport_code'."

    print("test_generate_flights passed.")

def test_generate_passengers():
    """
        Тестирует генерацию экземпляров класса Passengers.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: id, first_name, last_name, passport_number, contact_info.

        Выводит сообщение "test_generate_passengers passed." при успешном прохождении теста.
    """
    passengers_gen = Passengers.generate(1)
    passengers_instance = next(passengers_gen)

    assert isinstance(passengers_instance, Passengers), "Сгенерированный объект не является экземпляром Passengers."
    assert hasattr(passengers_instance, 'id'), "Сгенерированный объект не содержит атрибут 'id'."
    assert hasattr(passengers_instance, 'first_name'), "Сгенерированный объект не содержит атрибут 'first_name'."
    assert hasattr(passengers_instance, 'last_name'), "Сгенерированный объект не содержит атрибут 'last_name'."
    assert hasattr(passengers_instance, 'passport_number'), "Сгенерированный объект не содержит атрибут 'passport_number'."
    assert hasattr(passengers_instance, 'contact_info'), "Сгенерированный объект не содержит атрибут 'contact_info'."

    print("test_generate_passengers passed.")

def test_generate_security_check():
    """
        Тестирует генерацию экземпляров класса SecurityCheck.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: id, check_time, result, flight_id, tickets_id.

        Выводит сообщение "test_generate_security_check passed." при успешном прохождении теста.
    """
    security_check_gen = SecurityCheck.generate(1)
    security_check_instance = next(security_check_gen)

    assert isinstance(security_check_instance, SecurityCheck), "Сгенерированный объект не является экземпляром SecurityCheck."
    assert hasattr(security_check_instance, 'id'), "Сгенерированный объект не содержит атрибут 'id'."
    assert hasattr(security_check_instance, 'check_time'), "Сгенерированный объект не содержит атрибут 'check_time'."
    assert hasattr(security_check_instance, 'result'), "Сгенерированный объект не содержит атрибут 'result'."
    assert hasattr(security_check_instance, 'flight_id'), "Сгенерированный объект не содержит атрибут 'flight_id'."
    assert hasattr(security_check_instance, 'tickets_id'), "Сгенерированный объект не содержит атрибут 'tickets_id'."

    print("test_generate_security_check passed.")

def test_generate_tickets():
    """
        Тестирует генерацию экземпляров класса Tickets.

        Проверяет тип сгенерированного объекта, а также наличие необходимых атрибутов: id, seat_number, passenger_id, flight_id, cost.

        Выводит сообщение "test_generate_tickets passed." при успешном прохождении теста.
    """
    tickets_gen = Tickets.generate(1)
    tickets_instance = next(tickets_gen)

    assert isinstance(tickets_instance, Tickets), "Сгенерированный объект не является экземпляром Tickets."
    assert hasattr(tickets_instance, 'id'), "Сгенерированный объект не содержит атрибут 'id'."
    assert hasattr(tickets_instance, 'seat_number'), "Сгенерированный объект не содержит атрибут 'seat_number'."
    assert hasattr(tickets_instance, 'passenger_id'), "Сгенерированный объект не содержит атрибут 'passenger_id'."
    assert hasattr(tickets_instance, 'flight_id'), "Сгенерированный объект не содержит атрибут 'flight_id'."
    assert hasattr(tickets_instance, 'cost'), "Сгенерированный объект не содержит атрибут 'cost'."

    print("test_generate_tickets passed.")


test_generate_airlines()
test_generate_airport()
test_generate_airport_staff()
test_generate_baggage()
test_generate_flights()
test_generate_passengers()
test_generate_security_check()
test_generate_tickets()
print("All tests passed")
