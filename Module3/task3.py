# Функция test с произвольным числом параметров разного типа

def test(txt, *args, **comments):
    print(txt)

    for arg in args:
        print(type(arg), end='')
        print(arg)
    for key, value in comments.items():
        print(f'{key}: {value}')


_list = [1, 2, ]
_tuple = (1, 2, 3)
_bool = True
_set = {1, 2, 3, }
_dict = {'Start': 1, 'End': 100}

test('Параметры:', 123, _list, _tuple, _bool, _set, _dict, name="Aleks", cource='Python')


# Рекурсивная функция для вычисления факториала числа n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print('\n', 'Факториал:', factorial(8))


def get_multiplied_digits(number):
    # Преобразуем число в строку для работы с цифрами
    str_number = str(number)

    # Получаем первую цифру
    first = int(str_number[0])
    # Если длина строки больше 1, продолжаем рекурсивный вызов
    if len(str_number) > 1:
        # Возвращаем произведение первой цифры и рекурсивного вызова для оставшейся части числа
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        # Если строка состоит из одной цифры, возвращаем эту цифру
        return first


print('Рекурсивное умножение', get_multiplied_digits(40203))
