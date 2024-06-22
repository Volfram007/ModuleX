"""
Задача 1: Фабрика Функций.
Написать функцию, которая возвращает различные математические функции (например, деление, умножение)
в зависимости от переданных аргументов.
"""


def calc(operation):
    if operation == 'деление':
        def divide(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return "Ошибка: Деление на ноль"

        return divide

    elif operation == 'умножение':
        def multiply(x, y):
            return x * y

        return multiply
    else:
        return "Неподдерживаемая операция"


div = calc('деление')
mul = calc('умножение')

print("Задача 1: Фабрика Функций")
print(div(6, 3))
print(mul(2, 3))
print(div(6, 0))

"""
Задача 2: Лямбда-Функции.
Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def. 
Например, возведение числа в квадрат
"""


# Функция с использованием def
def square_def(x):
    return x ** 2


# Функция с использованием lambda
square = lambda x: x ** 2

print("\nЗадача 2: Лямбда-Функции")
print(square(4))
print(square_def(4))

"""
Задача 3: Вызываемые Объекты.
Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__, 
который возвращает площадь прямоугольника, то есть a*b
"""

class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rect = Rect(2, 4)
print("\nЗадача 3: Вызываемые Объекты")
print(f"Стороны: {rect.a}, {rect.b}")
print(f"Площадь: {rect()}")
