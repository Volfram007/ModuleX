# добавить отрицательный результат для abs
first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = [len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s)]
second_result = [len(first[i]) == len(second[i]) for i in range(len(first))]

print(first_result)
print(second_result)

# def first_result2():
#     result = []
#     for f, s in zip(first, second):
#         if len(f) != len(s):
#             result.append(abs(len(f) - len(s)))
#     return result
#
#
# print(first_result2())

# def second_result2():
#     result = []
#     for i in range(len(first)):
#         result.append(len(first[i]) == len(second[i]))
#     return result
#
#
# print(second_result2())

'''
Задача "Генераторные сборки"
Даны два списка:
- `first = ['Strings', 'Student', 'Computers']`
- `second = ['Строка', 'Урбан', 'Компьютер']`

Необходимо создать две генераторные сборки:
1. В переменную `first_result` запишите генераторную сборку, которая высчитывает разницу длин строк из списков `first` 
и `second`, если их длины не равны. Используйте функцию `zip` для перебора строк попарно из двух списков.
2. В переменную `second_result` запишите генераторную сборку, которая содержит результаты сравнения строк в одинаковых 
позициях из списков `first` и `second`. Для этого используйте функции `range` и `len`, НЕ используя функцию `zip`.

### Пример:
```python
print(list(first_result))  # [1, 2]
print(list(second_result))  # [False, False, True]
```

### Примечания:
- Важно соблюдать каждое условие задания.
'''
