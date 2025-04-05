
"""
Этот модуль определяет различные типы полей, используемые в моделях базы данных.

    Классы
    ------
    Field
        Базовый класс для определения поля базы данных.
    IntegerField
        Класс для определения целочисленного поля с дополнительными ограничениями.
    CharField
        Класс для определения символьного поля с максимальной длиной.
    ForeignKey
        Класс для определения поля внешнего ключа.
    TimeField
        Класс для определения поля времени.
    ManyToManyField
        Класс для определения поля отношения "многие ко многим".
"""



class Field:
    """
        Базовый класс для определения поля базы данных.

        Атрибуты
        --------
        name : str
            Имя поля.
        null : bool
            Указывает, может ли поле быть пустым (по умолчанию True).
        default : any
            Значение по умолчанию для поля (по умолчанию None).
        primary_key : bool
            Указывает, является ли поле первичным ключом (по умолчанию False).
        constraints : dict
            Дополнительные ограничения для поля.
    """
    def __init__(self, **kwargs):
        """
            Параметры
            ---------
            **kwargs : dict
                Произвольные именованные аргументы для установки атрибутов поля.
        """
        self.name = kwargs.get('name')
        self.null = kwargs.get('null', True)
        self.default = kwargs.get('default', None)
        self.primary_key = kwargs.get('primary_key', False)
        self.constraints = kwargs


class IntegerField(Field):
    """
        Класс для определения целочисленного поля с дополнительными ограничениями.

        Атрибуты
        --------
        type : str
            Тип поля, всегда 'INT'.
        min : int, optional
            Минимальное значение для поля.
        max : int, optional
            Максимальное значение для поля.
    """
    def __init__(self, min=None, max=None, **kwargs):
        """
            Параметры
            ---------
            min : int, optional
                Минимальное значение для поля (по умолчанию None).
            max : int, optional
                Максимальное значение для поля (по умолчанию None).
            **kwargs : dict
                Произвольные именованные аргументы для установки атрибутов базового класса.
        """
        super().__init__(**kwargs)
        self.type = 'INT'
        self.min = int(min) if min is not None else None
        self.max = int(max) if max is not None else None

    def validate(self, value):
        """
            Проверяет, соответствует ли значение ограничениям поля.

            Параметры
            ---------
            value : int
                Значение для проверки.

            Возвращает
            ----------
            bool
                True, если значение соответствует ограничениям, иначе False.
        """
        if self.min is not None and value < self.min:
            return False
        if self.max is not None and value > self.max:
            return False
        return True


class CharField(Field):
    """
        Класс для определения символьного поля с максимальной длиной.

        Атрибуты
        --------
        type : str
            Тип поля, всегда 'VARCHAR' с указанием максимальной длины.
        max_length : int
            Максимальная длина строки.
        words_count : int
            Количество слов.
    """
    def __init__(self, max_length=45, words_count=1, **kwargs):
        """
            Параметры
            ---------
            max_length : int, optional
                Максимальная длина строки (по умолчанию 45).
            words_count : int, optional
                Количество слов (по умолчанию 1).
            **kwargs : dict
                Произвольные именованные аргументы для установки атрибутов базового класса.
        """
        super().__init__(**kwargs)
        self.type = f'VARCHAR({max_length})'
        self.max_length = int(max_length)
        self.words_count = int(words_count)

    def validate(self, value):
        """
            Проверяет, соответствует ли значение ограничениям поля.

            Параметры
            ---------
            value : str
                Значение для проверки.

            Возвращает
            ----------
            bool
                True, если значение соответствует ограничениям, иначе False.
        """
        if self.constraints.get(' words_count') is not None:
            if int(self.constraints.get(' words_count')) > 1:
                return True  # В случае, если words_count > 1, длина слов не будет проверяться
        return True if len(str(value)) <= self.max_length else False


class ForeignKey(Field):
    """
        Класс для определения поля внешнего ключа.

        Атрибуты
        --------
        type : str
            Тип поля, всегда 'INT'.
        to : str
            Имя таблицы, на которую ссылается внешний ключ.
    """
    def __init__(self, to, **kwargs):
        """
            Параметры
            ---------
            to : str
                Имя таблицы, на которую ссылается внешний ключ.
            **kwargs : dict
                Произвольные именованные аргументы для установки атрибутов базового класса.
        """
        super().__init__(**kwargs)
        self.type = 'INT'
        self.to = to



class TimeField(Field):
    """
        Класс для определения поля времени.

        Атрибуты
        --------
        type : str
            Тип поля, всегда 'TIME'.
    """
    def __init__(self, **kwargs):
        """
            Параметры
            ---------
            **kwargs : dict
                Произвольные именованные аргументы для установки атрибутов базового класса.
        """
        super().__init__(**kwargs)
        self.type = 'TIME'


class ManyToManyField(Field):
    """
        Класс для определения поля отношения "многие ко многим".

        Атрибуты
        --------
        type : str
            Тип поля, всегда 'MANYTOMANY'.
        to : str
            Имя таблицы, на которую ссылается отношение.
    """
    def __init__(self, to, **kwargs):
        """
            Параметры
            ---------
            to : str
                Имя таблицы, на которую ссылается отношение.
            **kwargs : dict
                Произвольные именованные аргументы для установки атрибутов базового класса.
        """
        super().__init__(**kwargs)
        self.type = 'MANYTOMANY'
        self.to = to