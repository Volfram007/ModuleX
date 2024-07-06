class House:
    houses_history = []  # список созданных объектов

    def __new__(cls, *args):
        name = args[0]  # получаем название здания по индексу [0]
        cls.houses_history.append(args[0])  # добавляем название здания в историю
        return object.__new__(cls)

    def __init__(self, name, area):
        self.name = name

    def __del__(self):
        print(f'"{self.name}" снесён, но он останется в истории')
        House.houses_history.remove(self.name)  # удаляем название здания из истории


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h2
del h3
print(House.houses_history)

'''
### Задание "История строительства"
В классе `House` создайте атрибут `houses_history = []`, который будет хранить названия созданных объектов.

Дополните метод `__new__`, чтобы:
- Название объекта добавлялось в список `cls.houses_history`.
- Название строения бралось из `args` по индексу.

Переопределите метод `__del__` так, чтобы он выводил строку:
`"<название> снесён, но он останется в истории"`.

Создайте несколько объектов класса `House` и проверьте работу методов `__del__` и `__new__`, а также значение атрибута 
`houses_history`.

Пример выполнения программы:
```python
h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
```

Ожидаемый вывод:
['ЖК Эльбрус']
['ЖК Эльбрус', 'ЖК Акация']
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
ЖК Акация снесён, но он останется в истории
ЖК Матрёшки снесён, но он останется в истории
['ЖК Эльбрус', 'ЖК Акация', 'ЖК Матрёшки']
'''