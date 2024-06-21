# читает три числа, вводимые пользователем,
# и использует условные операторы для определения количества одинаковых чисел среди них

first = int(input())
second = int(input())
third = int(input())

# Определения количества одинаковых чисел
if first == second == third:
    print(3)
elif first == second or first == third or second == third:
    print(2)
else:
    print(0)
