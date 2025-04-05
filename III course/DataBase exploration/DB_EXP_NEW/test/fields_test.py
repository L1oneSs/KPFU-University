"""
Модуль fields_test предназначен для тестирования классов полей, определенных в модуле lib.fields.

Каждая функция тестирования проверяет корректность создания конкретного класса поля.

Примеры использования:
    test_field(): Тестирует базовый класс поля Field.
    test_integer_field(): Тестирует класс поля IntegerField.
    test_char_field(): Тестирует класс поля CharField.
    test_foreign_key(): Тестирует класс внешнего ключа ForeignKey.
    test_time_field(): Тестирует класс поля времени TimeField.
    test_many_to_many_field(): Тестирует класс поля многие ко многим ManyToManyField.

Каждая функция выводит сообщение "test_passed" в случае успешного прохождения теста.
"""

from lib.fields import Field, IntegerField, CharField, ForeignKey, TimeField, ManyToManyField

def test_field():
    field = Field(name='test_field', null=False, default='default_value', primary_key=True)
    assert field.name == 'test_field'
    assert field.null is False
    assert field.default == 'default_value'
    assert field.primary_key is True
    assert field.constraints == {'name': 'test_field', 'null': False, 'default': 'default_value', 'primary_key': True}
    print("test_field passed.")

def test_integer_field():
    int_field = IntegerField(name='test_int_field', min=0, max=100)
    assert int_field.type == 'INT'
    assert int_field.min == 0
    assert int_field.max == 100
    assert int_field.validate(50) is True
    assert int_field.validate(-1) is False
    assert int_field.validate(101) is False
    print("test_integer_field passed.")

def test_char_field():
    char_field = CharField(name='test_char_field', max_length=10, words_count=1)
    assert char_field.type == 'VARCHAR(10)'
    assert char_field.max_length == 10
    assert char_field.words_count == 1
    assert char_field.validate('short') is True
    assert char_field.validate('this_is_a_long_string') is False
    print("test_char_field passed.")

def test_foreign_key():
    foreign_key = ForeignKey(name='test_fk', to='related_table')
    assert foreign_key.type == 'INT'
    assert foreign_key.to == 'related_table'
    print("test_foreign_key passed.")

def test_time_field():
    time_field = TimeField(name='test_time_field')
    assert time_field.type == 'TIME'
    print("test_time_field passed.")

def test_many_to_many_field():
    many_to_many_field = ManyToManyField(name='test_m2m_field', to='related_table')
    assert many_to_many_field.type == 'MANYTOMANY'
    assert many_to_many_field.to == 'related_table'
    print("test_many_to_many_field passed.")


test_field()
test_integer_field()
test_char_field()
test_foreign_key()
test_time_field()
test_many_to_many_field()
print("All tests passed.")