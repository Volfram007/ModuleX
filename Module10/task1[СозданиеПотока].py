from time import sleep, time
from threading import Thread


def write_words(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(1, word_count + 1):
            f.write(f"Какое-то слово № {i}\n")
            sleep(0.1)
    print(f"Завершилась запись в файл {file_name}")


start_time = time()

write_words(10, 'Test/example1.txt')
write_words(30, 'Test/example2.txt')
write_words(200, 'Test/example3.txt')
write_words(100, 'Test/example4.txt')

end_time = time()
print(f"Работа функций: {end_time - start_time}")

start_time = time()

threads = [
    Thread(target=write_words, args=(10, 'Test/example5.txt')),
    Thread(target=write_words, args=(30, 'Test/example6.txt')),
    Thread(target=write_words, args=(200, 'Test/example7.txt')),
    Thread(target=write_words, args=(100, 'Test/example8.txt')),
]

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

end_time = time()
print(f"Работа потоков: {end_time - start_time}")

# ### Задача "Потоковая запись в файлы"
# Создать функцию для записи слов в файл с паузами и измерить время выполнения этой функции как в однопоточном,
# так и в многопоточном режиме.
#
# **Задание:**
# 1. Напишите функцию `write_words(word_count, file_name)`, которая:
#     - принимает `word_count` (количество записываемых слов) и `file_name` (название файла).
#     - Записывает слова "Какое-то слово № <номер слова по порядку>" в файл.
#     - Делает паузу 0.1 секунды после записи каждого слова (используйте `sleep` из модуля `time`).
#     - По завершении записи выводит "Завершилась запись в файл <название файла>".
# 2. Вызовите функцию `write_words` 4 раза с параметрами:
#     - 10, `example1.txt`
#     - 30, `example2.txt`
#     - 200, `example3.txt`
#     - 100, `example4.txt`
# 3. Создайте 4 потока для вызова этой функции с параметрами:
#     - 10, `example5.txt`
#     - 30, `example6.txt`
#     - 200, `example7.txt`
#     - 100, `example8.txt`
# 4. Запустите потоки методом `start`, остановите основной поток методом `join`.
# 5. Измерьте и выведите время, затраченное на выполнение функций и потоков.
#
# **Примечания:**
# - Ожидаемое время выполнения функций не должно превышать 34 секунды, а потоков — 20 секунд.
# - Потоки работают почти одновременно, поэтому завершение записи в файлы может происходить в разном порядке.
