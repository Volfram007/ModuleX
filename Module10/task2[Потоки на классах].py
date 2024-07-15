from time import sleep
from threading import Thread


class Knight(Thread):
    def __init__(self, name, power, color=0):
        super().__init__()
        self.name = name
        self.power = power
        self.color = color

    def run(self):
        colored_name = f"\033[{self.color}m{self.name}\033[0m"
        enemies = 100
        days = 0
        while enemies > 0:
            sleep(1)
            days += 1
            enemies -= self.power
            print(f"{colored_name} сражается {days} день(дня)..., осталось {enemies} воинов.")
        print(f"{colored_name} одержал победу спустя {days} дней(дня)!")

    def __str__(self):
        return f'\033[0mИмя:\033[93m{self.name}\033[0m \tУмение:\033[91m{self.power}'


sir = Knight('Lancelot', 20, 94)
sir2 = Knight('Galahad', 10, 93)

print(sir)
print(sir2)

print(f'\tНа нас напали!'.upper())

sir.start()
sir2.start()
sir.join()
sir2.join()

# ### Задача "За честь и отвагу!"
# Создайте класс `Knight`, наследованный от `Thread`, с атрибутами `name` (имя рыцаря, тип `str`)
# и `power` (сила рыцаря, тип `int`).
#
# Реализуйте метод `run`, в котором:
# - При запуске потока выводится "<Имя рыцаря>, на нас напали!".
# - Рыцарь сражается до победы над всеми врагами (100 для всех потоков).
# - Количество врагов уменьшается на `power` рыцаря.
# - Каждый день сражения (1 секунда) выводится
# "<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."
# - После победы выводится "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!".
#
# ### Задание
# 1. Создайте класс `Knight` с описанными свойствами.
# 2. Создайте и запустите 2 потока на основе класса `Knight`.
# 3. Выведите на экран строку об окончании битв.
#
# **Примечания:**
# - Метод `run` класса `Knight` должен корректно обрабатывать бой и выводить соответствующие сообщения.
# - Для создания задержки используйте `sleep` из модуля `time`.
# - Окончание битв выводится после завершения всех потоков.
