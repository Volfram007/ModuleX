class House:
    def __init__(self):  # Инициализируем атрибуты по умолчанию
        self.numberOfFloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOfFloors = floors
        print("Количество этажей:", self.numberOfFloors)


my_house = House()  # Создаем экземпляр класса House
my_house.setNewNumberOfFloors(5)  # Устанавливаем новое количество этажей
my_house.setNewNumberOfFloors(10)
