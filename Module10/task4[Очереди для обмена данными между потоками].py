from threading import Thread  # Библиотека для создания потоков
from time import sleep  # Библиотека для определения времени
from queue import Queue  # Библиотека для создания очереди


# Класс для столов в кафе
class Table:
    def __init__(self, number):
        self.number = number  # Номер стола
        self.is_busy = False  # Статус состояния стола в кафе


# Класс кафе
class Cafe:
    def __init__(self, tables):
        self.queue = Queue()  # Создаем очередь для посетителей
        self.tables = tables
        self.visitor_threads = []

    def customer_arrival(self):
        # Моделирует приход посетителя (каждую секунду)
        for i in range(1, 21):  # Цикл посетителей
            sleep(1)  # Имитация времени прихода следующего посетителя
            # Посетитель номер # прибыл
            print_event('arrival', i)
            visitor = Thread(target=self.serve_customer, args=(i,))  # Создаем поток посетителя
            self.visitor_threads.append(visitor)  # Добавляем поток в список
            visitor.start()
        print_event('all_served')
        # Ждем завершения всех потоков посетителей
        for visitor in self.visitor_threads:
            visitor.join()
        print_event('close')  # Закрываем кафе

    def serve_customer(self, visitor):
        # Моделирует обслуживание посетителя
        for table in self.tables:  # Перебираем столики
            if not table.is_busy:  # Проверяем статус состояния стола в кафе
                table.is_busy = True  # Бронируем стол
                # Посетитель номер # сел за стол #
                print_event('seated', visitor, table.number)
                sleep(5)
                # Посетитель номер # покушал и ушёл
                print_event('finished', visitor)
                table.is_busy = False  # Снимаем бронь со стола
                if not self.queue.empty():  # Проверяем, есть ли еще посетители
                    # Создаем поток посетителя из очереди
                    visitor = Thread(target=self.serve_customer, args=(self.queue.get(),))
                    self.visitor_threads.append(visitor)  # Добавляем поток в список
                    visitor.start()
                exit()
        print_event('waiting', visitor, queue=self.queue.qsize())
        self.queue.put(visitor)  # Добавляем посетителя в очередь


def print_event(event_type, visitor_number=None, table_number=None, queue=None):
    # Выводим событие в раскраске
    if event_type == 'arrival':
        print(f"\033[90mПосетитель номер \033[0m{visitor_number}\033[90m прибыл\033[0m")
    elif event_type == 'seated':
        print(f"\033[32mПосетитель номер \033[0m{visitor_number}\033[32m сел за стол \033[0m{table_number}")
    elif event_type == 'waiting':
        print(
            f"\033[33mПосетитель номер \033[0m{visitor_number}\033[33m ожидает свободный стол\033[0m")
    elif event_type == 'finished':
        print(
            f"\033[34mПосетитель номер \033[0m{visitor_number}\033[34m покушал и ушёл\033[0m")
    elif event_type == 'all_served':
        print("Достигнуто максимальное количество посетителей. Прием новых посетителей завершен.")
    elif event_type == 'close':
        print("\033[1;91mКАФЕ ЗАКРЫТО")
    else:
        print(event_type)


# Создаем столики в кафе
tables_ = [Table(i) for i in range(1, 4)]

# Инициализируем кафе
cafe = Cafe(tables_)

# Запускаем поток для прибытия посетителей
customer_arrival_thread = Thread(target=cafe.customer_arrival)
customer_arrival_thread.start()

# Ожидаем завершения работы прибытия посетителей
customer_arrival_thread.join()

# Задание "Очереди для обмена данными между потоками"
# Моделирование работы сети кафе с несколькими столиками и потоком посетителей,
# прибывающих для заказа пищи и уходящих после завершения приема.
#
# Есть сеть кафе с несколькими столиками. Посетители приходят, заказывают еду, занимают столик, употребляют еду и
# уходят. Если столик свободен, новый посетитель принимается к обслуживанию, иначе он становится в очередь на ожидание.
#
# Создайте 3 класса:
# Table - класс для столов, который будет содержать следующие атрибуты:
# number(int) - номер стола,
# is_busy(bool) - занят стол или нет.
#
# Cafe - класс для симуляции процессов в кафе. Должен содержать следующие атрибуты и методы:
# Атрибуты queue - очередь посетителей (создаётся внутри init), tables список столов (поступает из вне).
# Метод customer_arrival(self) - моделирует приход посетителя(каждую секунду).
# Метод serve_customer(self, customer) - моделирует обслуживание посетителя. Проверяет наличие свободных столов,
# в случае наличия стола - начинает обслуживание посетителя (запуск потока),
# в противном случае - посетитель поступает в очередь. Время обслуживания 5 секунд.
# Customer - класс (поток) посетителя. Запускается, если есть свободные столы.
#
# Так же должны выводиться текстовые сообщения соответствующие событиям:
# Посетитель номер <номер посетителя> прибыл.
# Посетитель номер <номер посетителя> сел за стол <номер стола>. (начало обслуживания)
# Посетитель номер <номер посетителя> покушал и ушёл. (конец обслуживания)
# Посетитель номер <номер посетителя> ожидает свободный стол. (помещение в очередь)
#
# Пример работы:
# # Создаем столики в кафе
# table1 = Table(1)
# table2 = Table(2)
# table3 = Table(3)
# tables = [table1, table2, table3]
#
# # Инициализируем кафе
# cafe = Cafe(tables)
#
# # Запускаем поток для прибытия посетителей
# customer_arrival_thread = threading.Thread(target=cafe.customer_arrival)
# customer_arrival_thread.start()
#
# # Ожидаем завершения работы прибытия посетителей
# customer_arrival_thread.join()
#
# Вывод на консоль (20 посетителей [ограничение выставить в методе customer_arrival]):
# Посетитель номер 1 прибыл
# Посетитель номер 1 сел за стол 1
# Посетитель номер 2 прибыл
# Посетитель номер 2 сел за стол 2
# Посетитель номер 3 прибыл
# Посетитель номер 3 сел за стол 3
# Посетитель номер 4 прибыл
# Посетитель номер 4 ожидает свободный стол
# Посетитель номер 5 прибыл
# Посетитель номер 5 ожидает свободный стол
# ......
# Посетитель номер 20 прибыл
# Посетитель номер 20 ожидает свободный стол
# Посетитель номер 17 покушал и ушёл.
# Посетитель номер 20 сел за стол N.
# Посетитель номер 18 покушал и ушёл.
# Посетитель номер 19 покушал и ушёл.
# Посетитель номер 20 покушал и ушёл.
