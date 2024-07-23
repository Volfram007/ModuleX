import asyncio


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнование.')
    for i in range(1, 6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {i} шар')
    print(f'Силач {name} закончил соревнования.')


async def start_tournament():
    strongman1 = asyncio.create_task(start_strongman('Паша', 3))
    strongman2 = asyncio.create_task(start_strongman('Дениса', 4))
    strongman3 = asyncio.create_task(start_strongman('Аполон', 5))
    await asyncio.gather(strongman1, strongman2, strongman3)


asyncio.run(start_tournament())

# **Задача "Асинхронные силачи"**
# 1. Напишите асинхронную функцию `start_strongman(name, power)`:
#     - Выведите строку: 'Силач <имя силача> начал соревнования.'
#     - Поднимите 5 шаров, выводя строку: 'Силач <имя силача> поднял <номер шара>' с задержкой, обратной `power`.
#     - В конце выведите строку: 'Силач <имя силача> закончил соревнования.'
#
# 2. Напишите асинхронную функцию `start_tournament`:
#     - Создайте 3 задачи для `start_strongman` с выбранными именами и силой.
#     - Ожидайте выполнение каждой задачи (await).
#
# 3. Запустите `start_tournament` с помощью `asyncio.run`.
#
# **Пример вывода:**
# ```
# Силач Pasha начал соревнования
# Силач Denis начал соревнования
# Силач Apollon начал соревнования
# Силач Apollon поднял 1 шар
# Силач Denis поднял 1 шар
# Силач Pasha поднял 1 шар
# Силач Apollon поднял 2 шар
# Силач Denis поднял 2 шар
# Силач Apollon поднял 3 шар
# Силач Pasha поднял 2 шар
# Силач Denis поднял 3 шар
# Силач Apollon поднял 4 шар
# Силач Pasha поднял 3 шар
# Силач Apollon поднял 5 шар
# Силач Apollon закончил соревнования
# Силач Denis поднял 4 шар
# Силач Denis поднял 5 шар
# Силач Denis закончил соревнования
# Силач Pasha поднял 4 шар
# Силач Pasha поднял 5 шар
# Силач Pasha закончил соревнования
# ```
#
# **Примечания:**
# - Используйте `async` для асинхронных функций.
# - Используйте `await` для ожидания задач.
# - Используйте `sleep` из `asyncio` для задержки.
# - Запустите асинхронную функцию с помощью `asyncio.run`.
