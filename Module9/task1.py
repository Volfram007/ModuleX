# Дан список целых чисел, примените функции map и filter так, чтобы в конечном списке оставить нечётные квадраты чисел
# [1, 25, 49, 121, 1225, 7921]


numbers = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]


def isOdd(x):
    # Проверяем, является ли число нечетным
    return x % 2 == 1


def square(x):
    # Возводит число в квадрат
    return x ** 2


oddNumbers = filter(isOdd, numbers)
oddNumbersSquared = map(square, oddNumbers)

# oddNumbers = filter(lambda x: x % 2 == 1, numbers)
# oddNumbersSquared = map(lambda x: x ** 2, oddNumbers)

print(list(oddNumbersSquared))
