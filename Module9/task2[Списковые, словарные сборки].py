first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(x) for x in first_strings if len(x) >= 5]
second_result = [[x, y] for x in first_strings for y in second_strings if len(x) == len(y)]
third_result = {x: len(x) for x in first_strings + second_strings if len(x) % 2 == 0}


print(first_result)
print(second_result)
print(third_result)

# def first_result2():
#     result = []
#     for x in first_strings:
#         if len(x) >= 5:
#             result.append(len(x))
#     return result
#
#
# print(first_result2())


# def second_result2():
#     result = []
#     for x in first_strings:
#         for y in second_strings:
#             if len(x) == len(y):
#                 result.append((x, y))
#     return result
#
#
# print(second_result2())


# def third_result2():
#     result = {}
#     for x in first_strings + second_strings:
#         if len(x) % 2 == 0:
#             result[x] = len(x)
#     return result
#
#
# print(third_result2())

'''
### Задача "Списковые, словарные сборки"
Даны списки строк:
- `first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']`
- `second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']`

1. В переменную `first_result` запишите список длин строк из `first_strings`, длина которых не менее 5 символов.
2. В переменную `second_result` запишите список кортежей, состоящих из пар слов одинаковой длины из списков 
`first_strings` и `second_strings` (используйте два вложенных цикла).
3. В переменную `third_result` запишите словарь, где ключ - строка, значение - длина строки. Строки для словаря берутся 
из объединённых списков `first_strings` и `second_strings`. Пары добавляются в словарь, если длина строки чётная.

### Пример:
```python
print(first_result)
print(second_result) 
print(third_result)
```

### Вывод:
[10, 8, 8]
[('Elon', 'Task'), ('Elon', 'Java'), ('Musk', 'Task'), ('Musk', 'Java'), ('Monitors', 'Computer'), ('Variable', 'Computer')]
{'Elon': 4, 'Musk': 4, 'Programmer': 10, 'Monitors': 8, 'Variable': 8, 'Task': 4, 'Java': 4, 'Computer': 8}

### Примечания:
- При использовании двух циклов for внутри сборки, первый цикл - внешний, второй - внутренний.
'''
