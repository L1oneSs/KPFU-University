"""
Модуль graphics предоставляет функциональность для создания графиков с использованием библиотеки Matplotlib.
Основной класс `PlotBuilder` позволяет создавать графики, добавлять данные, сохранять и отображать графики.
"""

import matplotlib.pyplot as plt
import random

class PlotBuilder:
    """
        Класс для построения графиков с использованием Matplotlib.

        Атрибуты
        ----------
        title : str
            Заголовок графика.
        x_label : str
            Метка оси X.
        y_label : str
            Метка оси Y.
        fig : matplotlib.figure.Figure
            Объект фигуры Matplotlib.
        ax : matplotlib.axes._axes.Axes
            Объект оси Matplotlib.

        Методы
        ----------
        __init__(title, x_label, y_label)
            Инициализирует объект PlotBuilder с заданным заголовком и метками осей.
        add_line(x_data, y_data, label)
            Добавляет линию на график с заданными данными и меткой.
        save(file_name, file_format='png')
            Сохраняет график в файл с заданным именем и форматом.
        show()
            Отображает график на экране.
    """
    def __init__(self, title, x_label, y_label):
        """
            Инициализация объекта PlotBuilder.

            Параметры
            ----------
            title : str
                Заголовок графика.
            x_label : str
                Метка оси X.
            y_label : str
                Метка оси Y.
        """
        self.title = title
        self.x_label = x_label
        self.y_label = y_label
        self.fig, self.ax = plt.subplots()
        self.fig.subplots_adjust(left=0.2)

    def add_line(self, x_data, y_data, label):
        """
            Добавляет линию на график.

            Параметры
            ----------
            x_data : list
                Данные для оси X.
            y_data : list
                Данные для оси Y.
            label : str
                Метка линии.
        """
        line_style = random.choice(['-', '--', '-.', ':'])
        if len(x_data) > 10:
            marker_style = random.choice(['o', 's', 'D', '^', 'v', '<', '>', 'p', '*'])
        else:
            marker_style = None
        self.ax.plot(x_data, y_data, label=label, linestyle=line_style, marker=marker_style)

    def save(self, file_name, file_format='png'):
        """
            Сохраняет график в файл.

            Параметры
            ----------
            file_name : str
                Имя файла для сохранения графика.
            file_format : str, optional
                Формат файла (по умолчанию 'png').
        """
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        self.ax.legend()
        self.fig.savefig(f"{file_name}.{file_format}", format=file_format)

    def show(self):
        """
            Отображает график на экране.
        """
        self.ax.set_title(self.title)
        self.ax.set_xlabel(self.x_label)
        self.ax.set_ylabel(self.y_label)
        self.ax.legend()
        plt.show()