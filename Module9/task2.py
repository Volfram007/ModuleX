print("\nЗадача 1: Фабрика Функций")


def calc(operation):
    if operation == 'деление':
        def divide(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return "Error: Division by zero"

        return divide

    elif operation == 'умножение':
        def multiply(x, y):
            return x * y

        return multiply
    else:
        return "Неподдерживаемая операция"


div = calc('деление')
mul = calc('умножение')

print(div(6, 3))
print(mul(2, 3))
print(div(6, 0))

print("\nЗадача 2: Лямбда-Функции")


# Функция с использованием def
def square_def(x):
    return x ** 2


# Функция с использованием lambda
square = lambda x: x ** 2

print(square(4))
print(square_def(4))

print("\nЗадача 3: Вызываемые Объекты")


class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b


rect = Rect(2, 4)
print(f"Стороны: {rect.a}, {rect.b}")
print(f"Площадь: {rect()}")
