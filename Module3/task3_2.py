def print_params(a=1, b='строка', c=True):
    print(f"a = {a}, b = {b}, c = {c}")

# Вызовы функции с разным количеством аргументов
print("Вызовы функции print_params")
print_params()
print_params(10)
print_params(20, "новая строка")
print_params(30, "другая строка", False)
print_params(b=25)
print_params(c=[1,2,3])

# 2. Распаковка параметров
values_list = [100, "список", False]
values_dict = {'a': 200, 'b': "словарь", 'c': [4, 5, 6]}

print("\nРаспаковка списка:")
print_params(*values_list)
print("Распаковка словаря:")
print_params(**values_dict)

# 3. Распаковка + отдельные параметры
values_list_2 = [300, "новый список"]
print("\nРаспаковка списка + отдельный параметр:")
print_params(*values_list_2, 42)