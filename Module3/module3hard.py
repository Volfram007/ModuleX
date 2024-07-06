# from time import perf_counter

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


# Функция для суммирования чисел и длин строк
# Функция map
def calculateMap(item):
    if isinstance(item, int):  # Если элемент является целым числом
        return item
    elif isinstance(item, str):  # Если элемент является строкой
        # digits_str = [char for char in item if char.isdigit()]  # Получаем список всех цифр из строки
        # if len(digits_str) > 0:
        #     digits_int = int(''.join(digits_str))
        #     return len(item) - len(digits_str) + digits_int
        return len(item)
    elif isinstance(item, dict):  # Если элемент является словарем
        return sum(map(calculateMap, item)) + sum(map(calculateMap, item.values()))
    elif isinstance(item, (list, tuple, set)):  # Если элемент является списком, множеством, кортежем
        return sum(map(calculateMap, item))
    else:
        return 0


# Рекурсия for
def calculateFor(item):
    if isinstance(item, int):  # Если элемент является целым числом
        return item
    elif isinstance(item, str):  # Если элемент является строкой
        # digits_str = [char for char in item if char.isdigit()]  # Получаем список всех цифр из строки
        # if len(digits_str) > 0:
        #     digits_int = int(''.join(digits_str))
        #     return len(item) - len(digits_str) + digits_int
        return len(item)
    elif isinstance(item, dict):  # Если элемент является словарем
        return sum(len(key) for key in item) + sum(calculateFor(value) for value in item.values())
    elif isinstance(item, (list, tuple, set)):  # Если элемент является списком, множеством, кортежем
        return sum(calculateFor(sub_item) for sub_item in item)
    else:
        return 0


# start_time = perf_counter()  # Время начала работы программы
# for i in range(1000000):
#     sum(map(calculateMap, data_structure))
# end_time = perf_counter()  # Время окончания работы программы
# elapsed_time = end_time - start_time  # Время работы программы
# print(f"Время выполнения 'map': {elapsed_time} секунд")  # Время выполнения
#
# start_time = perf_counter()  # Время начала работы программы
# for i in range(1000000):
#     calculate(data_structure)
# end_time = perf_counter()  # Время окончания работы программы
# elapsed_time = end_time - start_time  # Время работы программы
# print(f"Время выполнения 'for': {elapsed_time} секунд")  # Время выполнения


# Рекурсивный обход структуры данных
resultMap = sum(map(calculateMap, data_structure))
resultFor = calculateFor(data_structure)

print("Сумма всех цифр и длины всех строк\nРекурсия:\t{}\nФунк. map:\t{}".format(resultFor, resultMap))

'''
**Задание: "Раз, два, три, четыре, пять .... Это не всё?"**
Все ученики Урбана очень умные, но иногда путаются в том, что сделали. Один из учеников уснул на клавиатуре, и его код 
выглядел следующим образом:
```python
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]
```

Он задался вопросом: "Как посчитать сумму всех чисел и длины всех строк?" 
Необходимо разработать универсальное решение для подсчёта всех чисел и длин всех строк в данной структуре.
**Что нужно подсчитать:**
- Все числа.
- Длины всех строк.

**Пример работы:**
Входные данные:
```python
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
```

Выходные данные:
99

**Примечания:**
- Подсчёт должен выполняться одним вызовом функции.
- Рекомендуется применить рекурсивный вызов функции для каждой внутренней структуры.
- Для определения типа данных используйте функцию `isinstance`.
'''
