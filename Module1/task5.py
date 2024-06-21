# Неизменяемые и изменяемые объекты. Кортежи.

# Создание неизменяемых объектов
immutable_var = 1, "Str", 3, 4, True
print("immutable_var:", immutable_var)
# immutable_var[3] = "Изменено"
# Кортежи являются неизменяемыми структурами данных и после создания кортежа изменить его содержимое нельзя.

# Создание изменяемых объектов
mutable_list = [1, "Str", 3, 4, True]
print("mutable_list:", mutable_list)
mutable_list[3] = "Изменено"
print("mutable_New:", mutable_list)