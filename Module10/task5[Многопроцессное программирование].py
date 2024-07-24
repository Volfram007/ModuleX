from multiprocessing import Pool, Manager


class WarehouseManager:
    def __init__(self):
        # создания словаря
        self.data = Manager().dict()

    def process_request(self, request):
        # Распаковываем кортеж в отдельные переменные
        product, request, count = request

        # Выполняем запрос на получение товара
        if request == "receipt":
            # Увеличиваем количество товара на складе
            self.data[product] = self.data.get(product, 0) + count

        # Обрабатываем запрос на отгрузку товара
        elif request == "shipment":
            # Уменьшаем количество товара на складе
            if count > self.data.get(product, 0):
                print(f"Недостаточно товара '{product}' на складе!")
            else:
                self.data[product] = self.data.get(product, 0) - count

    def run(self, requests_):
        # Создаем пул процессов. Количество процессов будет равно количеству ядер процессора по умолчанию.
        with Pool() as pool:
            # Запускаем обработку каждого запроса в отдельном процессе, используя map
            # Метод map блокирует выполнение, пока все процессы не завершатся
            pool.map(self.process_request, requests_)


if __name__ == "__main__":
    # Создаем менеджера склада
    manager = WarehouseManager()
    # Множество запросов на изменение данных о складских запасах
    requests = [
        ("product1", "receipt", 100),
        ("product2", "receipt", 150),
        ("product1", "shipment", 30),
        ("product3", "receipt", 200),
        ("product2", "shipment", 50),
    ]

    manager.run(requests)

    print(dict(manager.data))

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
# https://docs-python.ru/standart-library/paket-multiprocessing-python/klass-pool-modulja-multiprocessing/

# from threading import Thread
#
#
# class WarehouseManager:
#     def __init__(self):
#         self.data = {}  # Список с данными о товарах
#
#     def process_request(self, request):
#         # Обрабатываем запрос
#         product, request, count = request
#
#         if request == 'receipt':
#             # Выполняем запрос на получение
#             if product in self.data:  # Если товар есть в списке
#                 self.data[product] += count  # Увеличиваем счетчик
#             else:
#                 self.data[product] = count  # Добавляем товар в список
#         elif request == 'shipment':
#             # Выполняем запрос на отгрузку
#             if product in self.data and self.data[product] >= count:
#                 self.data[product] -= count  # Уменьшаем счетчик
#             else:
#                 print(f"Недостаточно товара {product} для отгрузки {count}")
#
#     def run(self, requests):
#         # Запускаем менеджера склада
#         threads = []
#         for request in requests:  # Создаем поток для обработки запроса
#             thread = Thread(target=self.process_request, args=(request,))
#             threads.append(thread)
#             thread.start()
#
#         # Завершаем все потоки
#         for th in threads:
#             th.join()
#
#
# # Создаем менеджера склада
# manager = WarehouseManager()
#
# # Множество запросов на изменение данных о складских запасах
# requests_ = [
#     ("product1", "receipt", 100),
#     ("product2", "receipt", 150),
#     ("product1", "shipment", 30),
#     ("product3", "receipt", 200),
#     ("product2", "shipment", 50)
# ]
#
# # Запускаем обработку запросов
# manager.run(requests_)
#
# # Выводим обновленные данные о складских запасах
# print(manager.data)
