# Создание исключений

class InvalidDataException(Exception):
    pass


class ProcessingException(Exception):
    def __init__(self, message, Info=None):
        self.message = message
        self.Info = Info


def generate_exceptions(arg):
    b = 9
    if isinstance(arg, (int, float)) and arg < 0:
        raise InvalidDataException("Отрицательное число")
    elif isinstance(arg, str) and not arg:
        raise InvalidDataException("Пустая строка")
    elif isinstance(arg, (int, float)) and arg > 1000:
        raise ProcessingException("Значение превышает допустимый предел")
    else:
        try:
            result = f"Ответ:  {b / arg}"
        except ZeroDivisionError as e:
            raise ProcessingException(e, f"b: {b}, arg: {arg}")
        except TypeError as e:
            raise ProcessingException(e)
    return result


def func(arg):
    try:
        result = generate_exceptions(arg)
        print(result)
    except InvalidDataException as e:
        print(f"Ошибка: {e}")
        raise  # Передаем исключение дальше по стеку вызовов
    except ProcessingException as e:
        print(f"Ошибка: {e}")
        raise  # Передаем исключение дальше по стеку вызовов


test = [-10, "", 5000, "текст", 0, 42, ]

for value in test:
    try:
        func(value)
    except (InvalidDataException, ProcessingException) as e:
        print(f"Исключение обработано: [{e}]")
    finally:
        print(f"Завершена обработка значения: [{value}]\n")
