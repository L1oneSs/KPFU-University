import os
import random

from matplotlib import pyplot as plt

graph_info = []
graph_generate_info = []

def create_graphics(num):
    if num == "1":
        if len(graph_info) == 0:
            print("Вы еще не выполнили ни одного запроса!")
            return
        num_entries = len(graph_info)
        colors = [plt.cm.jet(i / num_entries) for i in range(num_entries)]
        markers = ['o', 's', '^', 'x', '*', 'D', 'P', 'h', '+', 'v']

        # Group entries by operation type
        grouped_entries = {}
        for entry in graph_info:
            op_name, row_count, time_query = entry
            if op_name not in grouped_entries:
                grouped_entries[op_name] = {'row_counts': [], 'time_queries': [],
                                            'color': random.choice(colors),
                                            'marker': random.choice(markers)}
            grouped_entries[op_name]['row_counts'].append(row_count)
            grouped_entries[op_name]['time_queries'].append(time_query)

        for op_name, data in grouped_entries.items():
            fig, ax = plt.subplots()
            ax.plot(data['row_counts'], data['time_queries'], marker=data['marker'], color=data['color'])
            ax.set_xlabel('Записи')
            ax.set_ylabel('Время выполнения (с)')
            ax.set_title(f'График зависимости времени выполнения от количества записей ({op_name})')
            # Создаем имя файла на основе типа операции
            filename = f"investigations/images/execution_time_plot_{op_name}.png"
            # Сохраняем график в папку "images"
            plt.savefig(filename)
            # Показываем график
            plt.show()


    elif num == "2":
        if len(graph_generate_info) == 0:
            print("Сначала сгенерируйте какие-либо данные!")
            return
        data = {'row_counts': [], 'time_queries': []}

        for entry in graph_generate_info:
            data['row_counts'].append(entry[1])
            data['time_queries'].append(entry[2])

        plt.plot(data['row_counts'], data['time_queries'], color='blue')

        plt.xlabel('Записи')
        plt.ylabel('Время выполнения (с)')
        plt.title('График зависимости генерации данных от количества записей')

        # Проверяем, существует ли папка "images", если нет, то создаем ее
        if not os.path.exists("investigations/images"):
            os.makedirs("investigations/images")

        # Сохраняем график в папку "images"
        plt.savefig("investigations/images/execution_time_plot_generate.png")

        # Показываем график
        plt.show()