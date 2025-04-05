"""
    Этот модуль предоставляет основу для управления моделями базы данных с использованием метаклассов. Он включает
    следующие компоненты:

    Классы:
    -------
    - ModelMeta:
        Метакласс, управляющий полями моделей.
        Атрибуты:
        - fields: dict
            Словарь, содержащий поля модели.
        Методы:
        - __new__(cls, name, bases, attrs):
            Создает новый класс модели и инициализирует его поля на основе переданных атрибутов и документации класса.

    - Model:
        Базовый класс для всех моделей, использующий метакласс ModelMeta.
        Атрибуты:
        - _fields: dict
            Словарь, содержащий поля модели.
        - _many_to_many_fields: defaultdict
            Словарь для управления полями ManyToManyField.
        Методы:
        - __init__(self, **kwargs):
            Инициализирует объект модели с переданными значениями полей.
        - create_table(cls):
            Создает SQL-запрос для создания таблицы модели.
        - save(self, cursor):
            Сохраняет объект модели в базе данных.
        - generate(cls, n):
            Генерирует n объектов модели со случайными значениями полей.

    - DatabaseSchema:
        Класс для управления схемой базы данных.
        Атрибуты:
        - models: list
            Список моделей, составляющих схему базы данных.
        Методы:
        - create_tables(tables, cursor):
            Создает таблицы для всех моделей в схеме базы данных.
"""

import inspect
import random
import string
from collections import defaultdict

from lib.connection import DatabaseConnection
from lib.fields import Field, CharField, IntegerField, ForeignKey, ManyToManyField, TimeField


class ModelMeta(type):
    """
    Метакласс для управления полями моделей.

    Атрибуты
    --------
    fields : dict
        Словарь, содержащий поля модели.

    Методы
    ------
    __new__(cls, name, bases, attrs)
        Создает новый класс модели и инициализирует его поля на основе переданных атрибутов и документации класса.
    """
    def __new__(cls, name, bases, attrs):
        """
            Создает новый класс модели и инициализирует его поля на основе переданных атрибутов и документации класса.

            Параметры
            ---------
            cls : type
                Метакласс.
            name : str
                Имя создаваемого класса.
            bases : tuple
                Кортеж базовых классов.
            attrs : dict
                Словарь атрибутов класса.

            Возвращает
            ----------
            type
                Созданный класс.

            Описание
            --------
            Метод проходит по атрибутам создаваемого класса и инициализирует поля,
            которые являются экземплярами класса Field. Также, если у класса есть
            документация, метод анализирует её для инициализации полей на основе описания в документации.
        """
        fields = {}
        for key, value in attrs.items():
            if isinstance(value, Field):
                fields[key] = value
                value.name = key

        if '__doc__' in attrs and attrs['__doc__']:
            doc = attrs['__doc__'].strip().split('\n')
            for line in doc:
                line = line.strip()
                if line:
                    parts = line.split(':')
                    field_name = parts[0].strip()
                    field_type = parts[1].strip()
                    field_params = {}
                    if len(parts) > 2:
                        field_params = dict(param.split('=') for param in parts[2].strip().split(','))
                    if field_type == 'CharField':
                        fields[field_name] = CharField(**field_params)
                    elif field_type == 'IntegerField':
                        fields[field_name] = IntegerField(**field_params)
                    elif field_type == 'ForeignKey':
                        fields[field_name] = ForeignKey(**field_params)
                    elif field_type == 'ManyToManyField':
                        fields[field_name] = ManyToManyField(**field_params)
                    elif field_type == 'TimeField':
                        fields[field_name] = TimeField(**field_params)

        attrs['_fields'] = fields
        return super().__new__(cls, name, bases, attrs)


"""
    Базовый класс для всех моделей, использующий метакласс ModelMeta.

    Атрибуты
    --------
    _fields : dict
        Словарь, содержащий поля модели.
    _many_to_many_fields : defaultdict
        Словарь для управления полями ManyToManyField.

    Методы
    ------
    __init__(self, **kwargs)
        Инициализирует объект модели с переданными значениями полей.
    create_table(cls)
        Создает SQL-запрос для создания таблицы модели.
    save(self, cursor)
        Сохраняет объект модели в базе данных.
    generate(cls, n)
        Генерирует n объектов модели с случайными значениями полей.
"""
class Model(metaclass=ModelMeta):

    def __init__(self, **kwargs):
        """
            Инициализирует объект модели с переданными значениями полей.

            Параметры
            ---------
            kwargs : dict
                Словарь значений для инициализации полей модели. Ключи должны соответствовать именам полей.

            Исключения
            ----------
            ValueError
                Выбрасывается, если значение поля не проходит валидацию.

            Описание
            --------
            Метод устанавливает значения переданных полей в объекте модели.
            Проверяет валидацию для всех полей, кроме ForeignKey и TimeField.
            Если значение не проходит валидацию, выбрасывается ValueError.
            Также метод инициализирует и управляет полями ManyToManyField.
        """
        for key, value in kwargs.items():
            if key in self._fields:
                setattr(self, key, value)
                field = self._fields[key]
                if not isinstance(field, ForeignKey):
                    if not isinstance(field, TimeField):
                        if not field.validate(value):
                            raise ValueError(
                                f"Validation error: {key} field value '{value}' does not meet the criteria.")

        # Управление ManyToManyField
        self._many_to_many_fields = defaultdict(list)
        for field_name, field in self._fields.items():
            if isinstance(field, ManyToManyField):
                setattr(self, field_name, [])
                self._many_to_many_fields[field_name] = []

    @classmethod
    def create_table(cls):
        """
        Создает SQL-запрос для создания таблицы модели в базе данных.

        Возвращает
        ----------
        str
            SQL-запрос для создания таблицы модели и связанных таблиц ManyToMany.

        Исключения
        ----------
        ValueError
            Выбрасывается, если не удалось найти первичный ключ в таблице, на которую есть внешний ключ.

        Описание
        --------
        Метод генерирует SQL-запрос для создания таблицы на основе полей модели.
        Для каждого поля определяется тип столбца в таблице, используя информацию из поля.
        Для CharField задается VARCHAR с максимальной длиной.
        Для ForeignKey создается внешний ключ, который ссылается на таблицу, указанную в поле.
        Если у поля задано значение primary_key, оно устанавливается в качестве первичного ключа.
        При обнаружении ManyToManyField создается дополнительная таблица связей между моделью и связанными объектами.
        Все собранные определения столбцов и внешних ключей добавляются в SQL-запрос создания таблицы.
        """
        import inspect

        columns = []
        foreign_keys = []
        many_to_many_tables = []

        for field_name, field in cls._fields.items():
            column_definition = f"{field_name} {field.type}"

            if isinstance(field, CharField):
                column_definition = f"{field_name} VARCHAR({field.max_length})"

            if isinstance(field, ForeignKey):
                referenced_table_name = field.to
                if referenced_table_name in globals():
                    referenced_table_class = globals()[referenced_table_name]
                    referenced_field_name = None
                    referenced_field_type = None
                    referenced_field_constraints = None

                    for name, attr in inspect.getmembers(referenced_table_class):
                        if isinstance(attr, Field) and attr.primary_key:
                            referenced_field_name = name
                            referenced_field_type = attr.type
                            referenced_field_constraints = attr.constraints
                            break

                    if referenced_field_name is None:
                        raise ValueError(f"No primary key found in referenced table {referenced_table_name}.")

                    column_definition = f"{field_name} {referenced_field_type}"

                    if referenced_field_constraints.get(' null') == 'False':
                        column_definition += " NOT NULL"

                    foreign_key = f"FOREIGN KEY ({field_name}) REFERENCES {referenced_table_name.lower()}({referenced_field_name})"
                    foreign_keys.append(foreign_key)
                else:
                    raise ValueError(f"No class found with name {referenced_table_name}.")

            # Проверка на ManyToManyField
            if isinstance(field, ManyToManyField):
                table_name = f"{cls.__name__.lower()}_{field_name}_link"
                columns_many = [
                    f"{cls.__name__.lower()}_id INT NOT NULL",
                    f"{field.to.lower()}_id INT NOT NULL",
                    "PRIMARY KEY ({}_id, {}_id)".format(cls.__name__.lower(), field.to.lower())
                ]
                many_to_many_tables = f"CREATE TABLE IF NOT EXISTS {table_name} ({', '.join(columns_many)});"

            else:
                if field.constraints.get('null') == 'False' or field.constraints.get(' null') == 'False':
                    column_definition += " NOT NULL"

                if field.default is not None:
                    column_definition += f" DEFAULT '{field.default}'"

                if field.constraints.get(' primary_key'):
                    column_definition += " PRIMARY KEY"

            if isinstance(field, ManyToManyField):
                pass
            else:
                columns.append(column_definition)

        table_definition = f"CREATE TABLE IF NOT EXISTS {cls.__name__.lower()} ({', '.join(columns)}"

        if foreign_keys:
            table_definition += f", {', '.join(foreign_keys)}"

        table_definition += ");"

        if many_to_many_tables:
            return table_definition, many_to_many_tables

        return table_definition

    def save(self, cursor):
        """
            Сохраняет текущий объект в базе данных.

            Параметры
            ----------
            cursor : объект
                Объект курсора для выполнения SQL-запросов.

            Исключения
            ----------
            ValueError
                Выбрасывается, если не удалось найти первичный ключ в модели.

            Описание
            --------
            Метод сохраняет текущий объект модели в базе данных.
            Сначала определяет название первичного ключа модели.
            Затем проверяет, существует ли уже запись с таким первичным ключом в базе данных.
            Если запись существует, обновляет текущий объект данными из нового объекта, сгенерированного через generate().
            Если записи с таким первичным ключом нет, выполняет INSERT-запрос для сохранения данных объекта.
            Далее сохраняет ManyToMany связи, если они есть.
        """
        # Получаем название первичного ключа из модели
        primary_key_name = None
        for field_name, field in self._fields.items():
            if field.constraints.get(' primary_key'):
                primary_key_name = field_name
                break

        if primary_key_name is None:
            print("Ошибка: Не удалось найти первичный ключ в модели.")
            return

        # Проверяем, существует ли уже запись с таким первичным ключом
        query = f"SELECT * FROM {self.__class__.__name__.lower()} WHERE {primary_key_name} = %s"
        cursor.execute(query, (getattr(self, primary_key_name),))
        existing_record = cursor.fetchone()
        if existing_record:
            # Если запись существует, генерируем новый объект через generate и обновляем текущий объект
            new_instance = next(self.__class__.generate(1))
            self.__dict__.update(new_instance.__dict__)
            self.save(cursor)  # Рекурсивно сохраняем обновленный объект
            return

        # Если записи с таким первичным ключом нет, продолжаем с сохранением
        fields = []
        values = []
        for field_name, field in self._fields.items():
            fields.append(field_name)
            values.append(getattr(self, field_name))
        fields_str = ', '.join(fields)
        values_str = ', '.join(['%s'] * len(values))
        query = f"INSERT INTO {self.__class__.__name__.lower()} ({fields_str}) VALUES ({values_str})"
        cursor.execute(query, tuple(values))


    @classmethod
    def generate(cls, n):
        """
            Генерирует n случайных объектов данного класса.

            Параметры
            ----------
            n : int
                Количество объектов для генерации.

            Возвращает
            ----------
            generator
                Генератор, возвращающий сгенерированные объекты.

            Описание
            --------
            Метод генерирует n случайных объектов данного класса.
            Для каждого поля класса определяет случайное значение в соответствии с его типом и ограничениями.
            Если поле является ForeignKey, то случайно выбирает значение из возможных значений данного поля.
            Если поле является CharField, генерирует случайную строку, учитывая максимальную длину и ограничения на количество слов.
            Если поле является IntegerField, генерирует случайное целое число в указанном диапазоне.
            Если поле является TimeField, генерирует случайное время в формате HH:MM:SS.
            Возвращает генератор, который возвращает сгенерированные объекты.
        """
        for _ in range(n):
            kwargs = {}
            for field_name, field in cls._fields.items():
                if isinstance(field, IntegerField):
                    min_val = field.constraints.get(' min')
                    max_val = field.constraints.get(' max')
                    if min_val == max_val and min_val is not None and max_val is not None:
                        kwargs[field_name] = random.randint(int(max_val), int(max_val))
                    elif min_val is not None and max_val is not None:
                        kwargs[field_name] = random.randint(int(min_val), int(max_val))
                    else:
                        kwargs[field_name] = random.randint(0, 100000)
                elif isinstance(field, CharField):
                    if field.constraints.get(' words_count') is not None:
                        count = int(field.constraints.get(' words_count'))
                        if count > 1:
                            max_words_length = min(field.max_length, field.max_length // count)
                            words = [
                                ''.join(random.choices(string.ascii_letters, k=random.randint(1, max_words_length))) for
                                _ in range(count)]
                            generated_value = ' '.join(words)

                            # Ensure the total length of the generated value does not exceed field.max_length
                            if len(generated_value) > field.max_length:
                                generated_value = generated_value[:field.max_length]

                            kwargs[field_name] = generated_value
                        else:

                            kwargs[field_name] = ''.join(random.choices(string.ascii_letters, k=field.max_length))
                    else:
                        kwargs[field_name] = ''.join(random.choices(string.ascii_letters, k=field.max_length))
                elif isinstance(field, ForeignKey):
                    referenced_table_name = field.to
                    if isinstance(referenced_table_name, str):
                        referenced_table = globals()[referenced_table_name]
                    else:
                        referenced_table = referenced_table_name

                    with DatabaseConnection('localhost', 'root', 'root', 'sandbox_mydb') as (cursor, connection):
                        primary_key_field_name = None
                        for key, f in referenced_table._fields.items():
                            if f.constraints.get(' primary_key'):
                                primary_key_field_name = key
                                break
                        cursor.execute(f"SELECT {primary_key_field_name} FROM {referenced_table.__name__.lower()}")
                        possible_values = cursor.fetchall()
                        if possible_values:
                            kwargs[field_name] = random.choice(possible_values)[0]
                        else:
                            kwargs[field_name] = None
                elif isinstance(field, TimeField):
                    kwargs[
                        field_name] = f"{random.randint(0, 23):02}:{random.randint(0, 59):02}:{random.randint(0, 59):02}"
                elif isinstance(field, ManyToManyField):
                    pass
                else:
                    kwargs[field_name] = None
            yield cls(**kwargs)


class Airlines(Model):
    """
    id: IntegerField: null=False, primary_key=True
    name: CharField: max_length=20, null=False, words_count=2
    code: CharField: max_length=3, null=False, words_count=1
    country: CharField: max_length=10, null=False, words_count=1
    """
    id = IntegerField(null=False, primary_key=True)
    name = CharField(max_length=20, null=False, words_count=2)
    code = CharField(max_length=3, null=False)
    country = CharField(max_length=10, null=False, words_count=1)

class Airport(Model):
    """
    code: CharField: max_length=10, null=False, primary_key=True, words_count=1
    name: CharField: max_length=20, null=False, words_count=1
    city: CharField: max_length=20, null=False, words_count=1
    country: CharField: max_length=20, null=False, words_count=1
    """
    code = CharField(max_length=10, null=False, primary_key=True, words_count=1)
    name = CharField(max_length=20, null=False, words_count=1)
    city = CharField(max_length=20, null=False, words_count=1)
    country = CharField(max_length=20, null=False, words_count=1)


class AirportStaff(Model):
    """
    id: IntegerField: null=False, primary_key=True
    first_name: CharField: max_length=20, null=False, words_count=1
    last_name: CharField: max_length=20, null=False, words_count=1
    job_title: CharField: max_length=20, words_count=1
    contact_info: IntegerField: null=False, min=111111111, max=999999999
    airport_code: ForeignKey: to=Airport, null=False
    """
    id = IntegerField(null=False, primary_key=True)
    first_name = CharField(max_length=20, null=False, words_count=1)
    last_name = CharField(max_length=20, null=False, words_count=1)
    job_title = CharField(max_length=20, words_count=1)
    contact_info = IntegerField(null=False, min=11111111, max=99999999)
    airport_code = ForeignKey(to=Airport, null=False)

class Baggage(Model):
    """
    id: IntegerField: null=False, primary_key=True
    flight_id: ForeignKey: to=Flights, null=False
    weight: IntegerField: null=False, min=0, max=120
    passenger_id: ForeignKey: to=Passengers, null=False
    """
    id = IntegerField(null=False, primary_key=True)
    flight_id = ForeignKey(to='Flights', null=False)
    weight = IntegerField(null=False, min=0, max=120)
    passenger_id = ForeignKey(to='Passengers', null=False)

class Flights(Model):
    """
    id: IntegerField: null=False, primary_key=True
    departure_time: TimeField: null=False
    arrival_time: TimeField: null=False
    flight_status: CharField: null=False, max_length=10, words_count=1
    airline_id: ForeignKey: to=Airlines, null=False
    origin_airport_code: ForeignKey: to=Airport, null=False
    destination_airport_code: ForeignKey: to=Airport, null=False
    """
    id = IntegerField(null=False, primary_key=True)
    departure_time = TimeField(null=False)
    arrival_time = TimeField(null=False)
    flight_status = CharField(null=False, max_length=10, words_count=1)
    airline_id = ForeignKey(to=Airlines, null=False)
    origin_airport_code = ForeignKey(to=Airport, null=False)
    destination_airport_code = ForeignKey(to=Airport, null=False)

class Passengers(Model):
    """
    id: IntegerField: null=False, primary_key=True
    first_name: CharField: max_length=20, null=False, words_count=1
    last_name: CharField: max_length=20, null=False, words_count=1
    passport_number: IntegerField: null=False, min=111111111, max=999999999
    contact_info: CharField: max_length=12, words_count=1
    """
    id = IntegerField(null=False, primary_key=True)
    first_name = CharField(max_length=20, null=False, words_count=1)
    last_name = CharField(max_length=20, null=False, words_count=1)
    passport_number = IntegerField(null=False, min=111111111, max=999999999)
    contact_info = CharField(max_length=12, words_count=1)


class SecurityCheck(Model):
    """
    id: IntegerField: null=False, primary_key=True
    check_time: TimeField: null=False
    result: CharField: max_length=10, null=False, words_count=1
    flight_id: ForeignKey: to=Flights, null=False
    tickets_id: ForeignKey: to=Tickets, null=False
    """
    id = IntegerField(null=False, primary_key=True)
    check_time = TimeField(null=False)
    result = CharField(max_length=10, null=False, words_count=1)
    flight_id = ForeignKey(to='Flights', null=False)
    tickets_id = ForeignKey(to='Tickets', null=False)


class Tickets(Model):
    """
    id: IntegerField: null=False, primary_key=True
    seat_number: CharField: max_length=3, null=True
    passenger_id: ForeignKey: to=Passengers, null=False
    flight_id: ForeignKey: to=Flights, null=False
    cost: IntegerField: null=False, min=1000, max=20000
    """
    id = IntegerField(null=False, primary_key=True)
    seat_number = CharField(max_length=3, null=True)
    passenger_id = ForeignKey(to='Passengers', null=False)
    flight_id = ForeignKey(to='Flights', null=False)
    cost = IntegerField(null=False, min=1000, max=20000)
