# 1. Необходимо написать программу с использованием механизмов многопоточности.
# 2. Программа должна создавать два потока-рыцаря.
# 3. Каждый рыцарь должен иметь имя и умение.
# 4. Умение рыцаря определяет время, необходимое для выполнения защитной миссии.
# 5. Враги будут нападать в количестве 100 человек.
# 6. Каждый день рыцарь может ослабить вражеское войско на определенное количество человек, равное его умению.
# 7. Если у рыцаря умение равно 20, то он будет защищать крепость в течение 5 дней (5 секунд в программе).
# 8. Чем выше умение рыцаря, тем быстрее он сможет защитить королевство.

import time
from threading import Thread


class Knight:
    name = ''
    skill = 0
    active = 'На посту'

    def __init__(self, name, skill):
        self.name = name
        self.skill = skill

    def __str__(self):
        return f'Имя:\033[93m{self.name}\033[0m \tУмение:\033[91m{self.skill} \t\033[0m[{self.active}]'


def Fortress(count, knight):
    knight.active = 'На прогулке'
    print(knight)
    for attack in range(round(count / knight.skill)):
        ...


sir = Knight('Lancelot', 20)
sir2 = Knight('Galahad', 10)

print(sir)
print(f'На нас напали!')
thread1 = Thread(Fortress(100, sir))

# thread1.start()
# thread1.join()
