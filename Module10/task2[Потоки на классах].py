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
    color = '0'

    def __init__(self, name, skill, color=0):
        self.name = name
        self.skill = skill
        self.color = color

    def __str__(self):
        return f'\033[0mИмя:\033[93m{self.name}\033[0m \tУмение:\033[91m{self.skill}'


def Fortress(count, knight):
    for attack in range(round(count / knight.skill)):
        print(
            f'\033[97m{knight.name}\033[{knight.color}m, сражается день {attack + 1}.\tОсталось {count - (attack + 1) * knight.skill} воинов.')
        time.sleep(1)
    print(f'\033[91m{knight.name} Победил всех!')


sir = Knight('Lancelot', 20, 94)
sir2 = Knight('Galahad', 10, 93)

thread1 = Thread(target=Fortress, args=(100, sir))
thread2 = Thread(target=Fortress, args=(100, sir2))

print(sir)
print(sir2)

print(f'\tНа нас напали!'.upper())

thread1.start()
thread2.start()
thread1.join()
thread2.join()
