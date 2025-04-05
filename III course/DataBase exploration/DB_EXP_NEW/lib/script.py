import matplotlib.pyplot as plt

# Значения по oX
sizes = [5, 50, 100, 200, 300, 500, 1000, 1500, 2000, 2500, 3000]

# Время выполнения запросов по таблицам Airlines, Passengers, Baggage
# Время выполнения запросов по таблицам Airlines, Passengers, Baggage
airlines_times = [0.5, 2.5, 5.0, 10.0, 15.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0]
passengers_times = [0.7, 3.5, 7.0, 14.0, 18.0, 22.0, 24.0, 26.0, 28.0, 30.0, 30.0]
baggage_times = [1.0, 5.0, 10.0, 15.0, 18.0, 20.0, 22.0, 24.0, 26.0, 28.0, 30.0]

# Построение графика
plt.plot(sizes, airlines_times, marker='o', linestyle='-', label='Airlines')
plt.plot(sizes, passengers_times, marker='s', linestyle='--', label='Passengers')
plt.plot(sizes, baggage_times, marker='D', linestyle='-.', label='Baggage')

# Настройка осей и заголовка
plt.title('Время выполнения запросов INSERT')
plt.xlabel('Количество вставляемых строк')
plt.ylabel('Время (секунды)')


# Добавление легенды
plt.legend()

# Отображение графика
plt.tight_layout()
plt.show()
