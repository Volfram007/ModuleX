from random import randint


class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        # Сравниваем количество этажей и тип здания
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


building1 = Building(5, "Жилой")
building2 = Building(5, "Офисный")
building3 = Building(10, "Жилой")
building4 = Building(5, "Жилой")

if not building1 == building2:
    print("Здания не одинаковы")

if building2 == building3:
    print("Здания одинаковы")
else:
    print("Здания не одинаковы")

if building1 == building4:
    print("Здания одинаковы")

# метод циклом
# buildings = [building1, building2, building3, building4]
# for i, building_i in enumerate(buildings, 1):
#     for j, building_j in enumerate(buildings, 1):
#         if i != j:  # Исключаем сравнение с самим собой
#             if i == len(buildings):  # Исключаем сравнение последнего элемента
#                 break
#             else:
#                 if building_i == building_j:
#                     print(f"Сравнение building{i} и building{j}:", 'Здания одинаковы')
#                 # else:
#                 #     print(f"Сравнение building{i} и building{j}:", 'Здания не одинаковы')
