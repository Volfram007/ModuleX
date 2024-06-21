numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Пустые списки для простых и непростых чисел
primes = []
not_primes = []

for num in numbers:
    # Число 1 не является простым
    if num == 1:
        continue
    # Переменная-флаг для отметки простоты числа
    is_prime = True
    # Проверяем делители числа от 2 до num-1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    # Если число простое, добавляем его в список primes
    if is_prime:
        primes.append(num)
    else:
        not_primes.append(num)

# Выводим списки на экран
print("Простое:", primes)
print("Не простое:", not_primes)
