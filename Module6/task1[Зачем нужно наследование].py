class Animal:
    def __init__(self, name):
        self.name = name
        self.alive = True  # Живой
        self.fed = False  # Накормленный


class Mammal(Animal):
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False


class Predator(Mammal):
    pass


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # Съедобное


class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False


class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)

'''
### Задача "Съедобное, несъедобное"
Создайте иерархию классов для описания животного мира с использованием наследования.

#### Пункты задачи:
1. Создайте классы `Animal` и `Plant` с соответствующими атрибутами и методами:
   - `Animal`: атрибуты `alive = True`, `fed = False`, `name`.
   - `Plant`: атрибуты `edible = False`, `name`.
2. Создайте наследуемые классы:
   - `Mammal`, `Predator` (наследуют `Animal`).
   - `Flower`, `Fruit` (наследуют `Plant`).
   - Для `Fruit` переопределите атрибут `edible = True`.
3. В классах `Mammal` и `Predator` реализуйте метод `eat(food)`:
   - Если `food.edible == True`, выводит `"<self.name> съел <food.name>"` и устанавливает `self.fed = True`.
   - Если `food.edible == False`, выводит `"<self.name> не стал есть <food.name>"` и устанавливает `self.alive = False`.
4. Создайте объекты классов и проверьте их взаимодействие.

#### Пример результата выполнения программы:
```python
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)  # Волк с Уолл-Стрит
print(p1.name)  # Цветик семицветик

print(a1.alive)  # True
print(a2.fed)    # False
a1.eat(p1)       # Волк с Уолл-Стрит не стал есть Цветик семицветик
a2.eat(p2)       # Хатико съел Заводной апельсин
print(a1.alive)  # False
print(a2.fed)    # True
```

### Примечания:
- Используйте `self` для обращения к атрибутам объекта текущего класса.
- Метод `eat` принимает объекты классов `Fruit` и `Flower` и работает с их атрибутами.
'''