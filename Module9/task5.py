# Домашнее задание по теме "Декораторы"
#   Задание:
# 1. Написать функцию sum_three, которая складывает 3 числа.
# 2. Написать функцию-декоратор is_prime, которая проверяет результат функции sum_three на простоту и выводит
#   "Простое" или "Составное".


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
