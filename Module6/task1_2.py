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
