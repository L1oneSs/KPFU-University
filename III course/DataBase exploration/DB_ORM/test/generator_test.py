# Тесты для generate_random_value
from lib.generator import generate_records, generate_random_value

# Генерация случайной строки длиной 10 символов
# Тесты для generate_random_value

# Тестирование генерации случайных строк
print("Random Strings:")
for _ in range(5):
    random_string_10 = next(generate_random_value('varchar', 10))
    print(random_string_10)

# Тестирование генерации случайных целых чисел
print("\nRandom Integers:")
for _ in range(5):
    random_int = next(generate_random_value('int'))
    print(random_int)

# Тестирование генерации случайных чисел с плавающей точкой
print("\nRandom Floats:")
for _ in range(5):
    random_float = next(generate_random_value('float'))
    print(random_float)

# Тестирование генерации текущей даты и времени
print("\nCurrent Datetimes:")
for _ in range(5):
    current_datetime = next(generate_random_value('datetime'))
    print(current_datetime)



# Тесты для generate_records
selected_table = "qemqme"
selected_db = "aboba3"
host = "localhost"
user = "root"
password = "root"
fetch_num_records = 5  # Генерация 5 записей
no_run = True  # Только получить запрос и значения, не выполнять их

# Вызов функции generate_records для получения SQL-запроса и значений записей
insert_query, record_values = generate_records(selected_table, selected_db, host, user, password, fetch_num_records, no_run)

# Вывод SQL-запроса
print("Generated SQL Query:")
print(insert_query)

# Вывод значений записей
print("Generated Record Values:")
for record in record_values:
    print(record)
