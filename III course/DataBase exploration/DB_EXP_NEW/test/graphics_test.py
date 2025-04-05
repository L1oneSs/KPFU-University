"""
Модуль graphics_test предназначен для тестирования функциональности построения графиков
с использованием класса PlotBuilder из модуля investigations.graphics.

Функция test_plot_builder() проверяет различные аспекты работы класса PlotBuilder:
добавление линий на график, установку заголовка и подписей осей,
сохранение графика в файл и его отображение.
"""

import random
from investigations.graphics import PlotBuilder

def test_plot_builder():
    """
        Тестирует функциональность класса PlotBuilder для создания и настройки графиков.

        Создает экземпляр PlotBuilder с заданными параметрами: заголовок 'Test Plot', подписи осей 'X-axis' и 'Y-axis'.
        Добавляет две линии данных на график с использованием случайно сгенерированных данных.
        Сохраняет график в файл с именем 'test_plot'.
        Отображает график на экране.

        Выводит сообщение "test_plot_builder passed." при успешном прохождении теста.
    """
    plot_builder = PlotBuilder(title='Test Plot', x_label='X-axis', y_label='Y-axis')

    x_data1 = list(range(11))
    y_data1 = [random.randint(1, 11) for _ in range(11)]
    plot_builder.add_line(x_data1, y_data1, label='Line 1')

    x_data2 = list(range(5))
    y_data2 = [random.randint(1, 10) for _ in range(5)]
    plot_builder.add_line(x_data2, y_data2, label='Line 2')

    file_name = 'test_plot'
    plot_builder.save(file_name)

    plot_builder.show()

    print("test_plot_builder passed.")

test_plot_builder()
