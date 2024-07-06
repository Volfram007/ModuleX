def get_multiplied_digits(number):
    # Преобразуем число в строку
    str_number = str(number)

    # Получаем первую цифру числа
    first = int(str_number[0])

    # Если число состоит из одной цифры, возвращаем эту цифру
    if len(str_number) == 1:
        return first
    else:
        # Если число состоит из нескольких цифр, вызываем рекурсивно функцию для остальной части числа
        return first * get_multiplied_digits(int(str_number[1:]))


print(get_multiplied_digits(40203))
print(get_multiplied_digits(123))
print(get_multiplied_digits(5))

'''
**Задача "Рекурсивное умножение цифр"**
Напишите функцию `get_multiplied_digits`, которая принимает аргумент `number` и подсчитывает произведение его цифр.

**Пункты задачи:**
1. Напишите функцию `get_multiplied_digits` с параметром `number`.
2. Преобразуйте `number` в строку и сохраните в переменной `str_number`.
3. Создайте переменную `first`, содержащую первую цифру из `str_number` в числовом представлении (int).
4. Если длина `str_number` больше 1, верните `first * get_multiplied_digits(int(str_number[1:]))`.
5. Если длина `str_number` равна 1, верните `first`.

**Примечания:**
- При преобразовании строки в число первые нули убираются: `int('00123') -> 123`.
- Для отладки используйте пошаговое выполнение, чтобы избежать ошибок бесконечной рекурсии или неверного обращения по индексу.
'''
