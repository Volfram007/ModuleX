from threading import Thread


class WarehouseManager:
    def __init__(self):
        self.data = {}  # Список с данными о товарах

    def process_request(self, request):
        # Обрабатываем запрос
        product, request, count = request

        if request == 'receipt':
            # Выполняем запрос на получение
            if product in self.data:  # Если товар есть в списке
                self.data[product] += count  # Увеличиваем счетчик
            else:
                self.data[product] = count  # Добавляем товар в список
        elif request == 'shipment':
            # Выполняем запрос на отгрузку
            if product in self.data and self.data[product] >= count:
                self.data[product] -= count  # Уменьшаем счетчик
            else:
                print(f"Недостаточно товара {product} для отгрузки {count}")

    # Обрабатываем неизвестный запрос

    def run(self, requests):
        # Запускаем менеджера склада
        threads = []
        for request in requests:  # Создаем поток для обработки запроса
            thread = Thread(target=self.process_request, args=(request,))
            threads.append(thread)
            thread.start()

        # Завершаем все потоки
        for th in threads:
            th.join()


# Создаем менеджера склада
manager = WarehouseManager()

# Множество запросов на изменение данных о складских запасах
requests_ = [
    ("product1", "receipt", 100),
    ("product2", "receipt", 150),
    ("product1", "shipment", 30),
    ("product3", "receipt", 200),
    ("product2", "shipment", 50)
]

# Запускаем обработку запросов
manager.run(requests_)

# Выводим обновленные данные о складских запасах
print(manager.data)

# ## Задание "Многопроцессное программирование"
#
# Разработайте программу `WarehouseManager` для управления данными о движении товаров на складе в
# многопользовательской среде.
#
# 1. **Класс `WarehouseManager`:**
#     * Атрибут `data`: словарь, где ключ - название продукта, значение - его количество (изначально пустой).
#     * Метод `process_request`: обрабатывает запрос (получение или отгрузка товара), принимая кортеж `request`
#     в формате `(название_продукта, действие, количество)`.
#         * `receipt`: добавить товар в `data` (или увеличить количество, если товар уже есть).
#         * `shipment`: уменьшить количество товара в `data` (если товар есть и количество больше 0).
# 2. **Метод `run`:**
#     * Принимает список запросов `requests`.
#     * Создает для каждого запроса отдельный параллельный процесс.
#     * Запускает каждый процесс (`start`).
#     * Ожидает завершения всех процессов (`join`).
#
# **Используйте механизм мультипроцессорности для обеспечения быстрой обработки запросов.**
