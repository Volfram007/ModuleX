# https://docs.python.org/3/library/itertools.html


def all_variants(text):
    ln = len(text)
    # Шаг для формирования подстрок
    step = 1

    for start in range(ln * ln - 2):
        # Увеличиваем шаг каждый раз, когда достигаем конца строки
        if start % ln == ln - 1:
            step += 1
        # Если индекс больше длины строки, возвращаем символ по этому индексу
        if ln - step >= start % ln:
            yield text[start % ln:start % ln + step]
        # Если индекс меньше длины строки, возвращаем символ по этому индексу
        elif start < ln:
            yield text[start % ln]


def all_variants2(text, length=1, step=1):
    # Цикл по всем возможным началам подстроки
    for start in range(len(text) - length + 1):
        yield text[start:start + length]
    # Завершаем рекурсию
    if length + step > len(text):
        return
    else:
        # Рекурсивно вызываем функцию
        for _ in all_variants2(text, length + step, step):
            yield _


a = all_variants("abc")
for i in a:
    print(i)

# рекурсивно вызываем функцию
print('\nЧерез рекурсию')
a = all_variants2("abс")
for i in a:
    print(i)

# Выходные данные
# a
# b
# c
# ab
# bc
# abc
