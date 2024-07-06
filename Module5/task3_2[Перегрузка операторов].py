class House:
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors

    def __str__(self):
        return f"Название: {self.name}, кол-во этажей: {self.floors}"

    def __eq__(self, other):
        """Сравнивает количество этажей двух домов"""
        if isinstance(other, House):
            return self.floors == other.floors
        return False

    def __lt__(self, other):
        """Сравнивает количество этажей (меньше)"""
        if isinstance(other, House) or isinstance(other, int):
            return self.floors < other.floors
        return

    def __le__(self, other):
        """Сравнивает количество этажей (меньше или равно)"""
        if isinstance(other, House) or isinstance(other, int):
            return self.floors <= other.floors
        return

    def __gt__(self, other):
        """Сравнивает количество этажей (больше)"""
        if isinstance(other, House) or isinstance(other, int):
            return self.floors > other.floors
        return

    def __ge__(self, other):
        """Сравнивает количество этажей (больше или равно)"""
        if isinstance(other, House) or isinstance(other, int):
            return self.floors >= other.floors
        return

    def __ne__(self, other):
        """Сравнивает количество этажей (не равно)"""
        if isinstance(other, House):
            return self.floors != other.floors
        return True

    def __add__(self, value):
        """Увеличивает количество этажей на заданное значение"""
        if isinstance(value, int):
            self.floors += value
            return self
        return

    __radd__ = __add__
    __iadd__ = __add__


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__

'''
**Задача "Нужно больше этажей"**
Дополните класс `House` следующими методами:
1. `__eq__(self, other)`: возвращает `True`, если количество этажей одинаковое у `self` и `other`.
2. Методы `__lt__(<)`, `__le__(<=)`, `__gt__(>)`, `__ge__(>=)`, `__ne__(!=)`: возвращают результаты сравнения по 
соответствующим операторам, сравнивая количество этажей.
3. `__add__(self, value)`: увеличивает количество этажей на `value`, возвращает объект `self`.
4. `__radd__(self, value)` и `__iadd__(self, value)`: работают так же, как и `__add__`, возвращают результат его вызова.

Для более точной логики работы методов используйте функцию `isinstance` для проверки типа объекта перед выполнением 
действия.

**Пример выполнения программы:**
```python
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
```

**Вывод на консоль:**
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
False
Название: ЖК Эльбрус, кол-во этажей: 20
True
Название: ЖК Эльбрус, кол-во этажей: 30
Название: ЖК Акация, кол-во этажей: 30
False
True
False
True
False

**Примечания:**
Методы `__iadd__` и `__radd__` могут возвращать результат вызова `__add__`.
'''
