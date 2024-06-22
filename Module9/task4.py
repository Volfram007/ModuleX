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


a = all_variants("abc")
for i in a:
    print(i)

# Выходные данные
# a
# b
# c
# ab
# bc
# abc
