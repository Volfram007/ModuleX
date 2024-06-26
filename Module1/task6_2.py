# Практическое задание по теме: "Словари и множества"
#
# • Цель: написать программу на Python для работы со словарями и множествами.
# • Работа со словарями: создать переменную my_dict, присвоить ей словарь с парами ключ-значение.
# • Вывести на экран словарь my_dict и значения по существующим и отсутствующим ключам.
# • Добавить и удалить пары из словаря my_dict, вывести значения на экран.
# • Работа с множествами: создать переменную my_set, присвоить ей множество с разными типами данных и
#   повторяющимися значениями.
# • Вывести на экран множество my_set и измененное множество после добавления и удаления элементов.
# • Словарь и множество являются неупорядоченными коллекциями.

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
