"""
    Получаем список процессоров из таблицы сайта, сортируем и выводим результат в графике
    requests - получаем код страницы
    beautifulsoup4 - библиотека для парсинга страниц
    matplotlib и numpy - библиотеки для работы с графиками
    pip install requests beautifulsoup4 matplotlib numpy
"""

import requests
import matplotlib.pyplot as plt
import numpy as np
from bs4 import BeautifulSoup

# URL страницы
url = "https://www.cpubenchmark.net/cpu_list.php"

response = requests.get(url)
# print(response.status_code)

# Парсим HTML-код страницы
bs = BeautifulSoup(response.text, 'html.parser')

# Находим таблицу с процессорами
table = bs.find('table', {'id': 'cputable'})

# Ищем все строки таблицы
rows = table.find_all('tr')

# Инициализируем список для хранения данных
cpu_data = {}

# Обрабатываем каждую строку таблицы (max 30 строк)
for row in rows[:30]:
    cols = row.find_all('td')
    if len(cols) > 1:
        name = cols[0].text.strip()
        rank = int(cols[1].text.strip().replace(',', ''))
        cpu_data[name] = rank

# Сортируем данные по рангу и выбираем топ 10 процессоров
top_cpu_data = dict(sorted(cpu_data.items(), key=lambda item: item[1])[:10])
# print(top_cpu_data)

# Подготовка данных для построения графика
cpu_names = list(top_cpu_data.keys())
cpu_ranks = list(top_cpu_data.values())

x = np.arange(len(cpu_names))
width = 0.35  # ширина столбцов
fig, ax = plt.subplots()

# Группированный столбчатый график
rects1 = ax.bar(x - width / 2, cpu_ranks, width, label='Рейтинг')

# Добавление подписей
# ax.set_ylabel('Рейтинг')
ax.set_title('Топ 10 CPU')
ax.set_xticks(x)
ax.set_xticklabels(cpu_names, rotation=45, ha='right')
ax.legend()


# Функция для добавления меток на столбцы
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


autolabel(rects1)  # добавляем метки на столбцы
fig.tight_layout()
plt.show()
