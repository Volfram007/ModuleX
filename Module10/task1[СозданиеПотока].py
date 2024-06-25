# Задание:
# Напишите программу, которая создает два потока.
# Первый поток должен выводить числа от 1 до 10 с интервалом в 1 секунду.
# Второй поток должен выводить буквы от 'a' до 'j' с тем же интервалом.
# Оба потока должны работать параллельно.

# import asyncio
#
#
# async def print_numbers():
#     for number in range(1, 11):
#         print('\033[32mThread 1: {}'.format(number))
#         await asyncio.sleep(0.01)
#
#
# async def print_letters():
#     for letter in 'abcdefghij'.upper():
#         print('\033[93mThread 2: {}'.format(letter))
#         await asyncio.sleep(0.01)
#
#
# async def main():
#     task1 = asyncio.create_task(print_numbers())
#     task2 = asyncio.create_task(print_letters())
#
#     # Ждем завершения обоих потоков
#     await task1
#     await task2
#     # await asyncio.gather(task1, task2)
#
#
# asyncio.run(main())

import time
from threading import Thread


def print_numbers():
    for number in range(1, 11):
        print(f'\033[32mThread 1: {number}')
        time.sleep(1)


def print_letters():
    for letter in 'abcdefghij':
        print(f'\033[33mThread 2: {letter}')
        time.sleep(1)


thread1 = Thread(target=print_numbers)
thread2 = Thread(target=print_letters)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
