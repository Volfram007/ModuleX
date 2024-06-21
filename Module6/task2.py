# Множественное наследование

class Vehicle:
    def __init__(self, vehicle_type="none"):
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"vehicle_type: {self.vehicle_type}"


class Car(Vehicle):
    def __init__(self, price=1000000):
        super().__init__()
        self.price = price

    def horse_power(self, horse_power=100):
        return horse_power

    def __str__(self):
        return f"H_P: {self.horse_power()}\t Price: {self.price}"


class Nissan(Car):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f"V_Type: {self.vehicle_type}, H_P: {self.horse_power()}\t Price: {self.price}"


p_car = Nissan()
print(p_car.vehicle_type, p_car.price)
