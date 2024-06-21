# Работа со словарями
my_dict = {
    "Вася": 1990,
    "Егор": 1985,
    "Маша": 1992
}
print("my_dict:", my_dict)

print("Значение 'Егор':", my_dict.get("Егор"))
print("Значение 'Aleks' (отсутствует):", my_dict.get("Aleks", "Не найден"))

my_dict["Aleks"] = 1984
my_dict["Толя"] = 1995
print("Проверка:", my_dict)

removed_value = my_dict.pop("Толя", "Не найден")
print("Вывод вырезанного ключа:", removed_value)
print("Проверка:", my_dict)

# Работа с множествами
my_set = {1, 2, False, 'Яблоко', 1, 2}
print("Проверка:", my_set)

my_set.add("Помидор")
my_set.add(555)
print("Проверка:", my_set)

my_set.remove('Яблоко')  # Удаляем элемент 555
print("Проверка:", my_set)
