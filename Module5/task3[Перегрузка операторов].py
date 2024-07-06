from random import randint


class Building:
    def __init__(self, number_of_floors, building_type):
        self.numberOfFloors = number_of_floors
        self.buildingType = building_type

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

'''
**Задача "Перегрузка операторов"**
1. Создайте новый проект в PyCharm.
2. Запустите созданный проект.

**Ваша задача:**
1. Создайте класс `Building`.
2. Создайте инициализатор `__init__` для класса `Building`, который будет задавать целочисленный атрибут 
`self.numberOfFloors` и строковый атрибут `self.buildingType`.
3. Перегрузите метод `__eq__`, чтобы сравнение объектов происходило по атрибутам `numberOfFloors` и `buildingType`.

**Примечания:**
- Создайте новый проект в PyCharm и реализуйте указанный код.
- Убедитесь, что перегруженный оператор `__eq__` корректно сравнивает объекты по заданным атрибутам.
'''