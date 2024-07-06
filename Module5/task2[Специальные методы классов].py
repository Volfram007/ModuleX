class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.numberOfFloors = number_of_floors

    def __str__(self):
        return f'Название "{self.name}", кол-во этажей: {self.numberOfFloors}'

    def __len__(self):
        return self.numberOfFloors


house1 = House('ЖК Эльбрус', 10)  # Создаем экземпляр класса
house2 = House('ЖК Акация', 20)
print(house1)
print(house2)
print(len(house1))
print(len(house2))

'''
**Задача "Магические здания"**
Дополните класс `House` следующими методами:
1. `__len__(self)`: возвращает количество этажей здания (`self.number_of_floors`).
2. `__str__(self)`: возвращает строку: "Название: <название>, кол-во этажей: <этажи>".

**Пример выполнения программы:**
```python
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)  # Название: ЖК Эльбрус, кол-во этажей: 10
print(h2)  # Название: ЖК Акация, кол-во этажей: 20

# __len__
print(len(h1))  # 10
print(len(h2))  # 20
```
'''
