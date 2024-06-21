# Функция с параметрами по умолчанию

def print_params(a='Default', b=1, c=True):
    print(a, b, c)


print_params()
print_params('Свои значения', 22, )
print_params(b=25)
print_params(c=[1, 2, 3, ])

# Распаковка параметров
values_list = ['List', 33, True, ]
values_dict = {'a': 'Dict', 'b': 44, 'c': ['Type', 44, True, ]}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list2 = ['List2', 55, ]
print_params(*values_list2, 'Ok')

# print_params(c=True, b='не по порядку', a='Заполнено')
