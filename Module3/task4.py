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
