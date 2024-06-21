# Различие атрибутов класса и экземпляра
class Building:
    buildType = ["Жилой", "Офис", "Магазин"]
    total = 0

    def __init__(self):
        from random import randint
        Building.total += 1
        self.number = self.total
        self.buildingType = self.buildType[randint(0, 2)]

    def __str__(self):
        return f"Здание {self.number}, {self.buildingType}"


buildings = [Building() for gen in range(40)]

for building in buildings:
    print(building)
