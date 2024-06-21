# Списки и словари

my_list = ["Яблоко", "Помидор", "Груша", "Апельсин", "Арбуз", "Манго"]
print(my_list)
print(my_list[0], my_list[-1])
print(my_list[2:5])
# Заменяем Апельсин на СОЛЬ
# my_list[3] = "СОЛЬ"
my_list.insert(3, "СОЛЬ")
print(my_list)
del my_list[0:4]
print(my_list)

print('-------------------------------------------------')
my_dict = {"Apple": "Яблоко", "Pear": "заменить", "Tomato": "Помидор"}
print(my_dict)
print(my_dict["Pear"])
# Заменяем значение и добавляем апельсин
my_dict.update({'Pear': 'Груша', 'Orange': 'Апельсин'})
print(my_dict)
