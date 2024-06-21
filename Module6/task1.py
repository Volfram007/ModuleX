# Наследование классов.
class Car:
    def __init__(self, price=1000000):
        self.price = price

    def horse_power(self):
        return 200

    def __str__(self):
        return f"{self.__class__.__name__},\t Horse power: {self.horse_power()},\t Price: {self.price}"


class Nissan(Car):
    def horse_power(self):
        return 180


class Kia(Car):
    def horse_power(self):
        return 250


p_car = Car()
print(p_car)

p_car = Nissan(9000)
print(p_car)

p_car = Kia(10000)
print(p_car)
