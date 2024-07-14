def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result <= 1:
            print("Ни простое, ни составное")
        else:
            is_prime_bool = True
            for i in range(2, int(result ** 0.5) + 1):
                if result % i == 0:
                    is_prime_bool = False
                    break
            if is_prime_bool:
                print(f"{result} Простое")
            else:
                print(f"{result} Составное")
        return result

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


# Пример использования
sum_three(2, 3, 6)  # "Простое"
sum_three(4, 6, 2)  # "Составное"
sum_three(0, 0, 0)  # "Ни простое, ни составное"

'''
### Задача "Декораторы в Python"
**Цель задания:**
Освоить механизмы создания декораторов Python и практически применить знания,
создав функцию-декоратор и обернув ею другую функцию.

**Задание:**
1. Напишите две функции:
    - `sum_three`, которая складывает три числа.
    - `is_prime`, функцию-декоратор, которая распечатывает "Простое", если результат `sum_three` будет простым числом,
    и "Составное" в противном случае.

**Пример выполнения кода:**
```python
result = sum_three(2, 3, 6)
print(result)
```

**Вывод на консоль:**
Простое
11

**Примечания:**
- Напишите внутреннюю функцию `wrapper` в декораторе `is_prime`.
- Функция `is_prime` должна возвращать `wrapper`.
- Используйте `@is_prime` как декоратор для функции `sum_three`.
'''