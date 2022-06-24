class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100

class Bus(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    def fare(self):
        return self.total_capacity * 100 * 1,1

class Car(Vehicle):
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)
    pass

car_1 = Car('Audi', 180, 30)
car_2 = Car('Volvo', 200, 40)
car_3 = Car('Opel', 230, 50)

bus_1 = Bus('Mercedes', 300, 60)
bus_2 = Bus('Renault', 310, 65)

def typeCheck(x, checkedType):
    print(isinstance(x, checkedType))

typeCheck(car_1, Car)      # True
typeCheck(car_2, Vehicle)  # True
typeCheck(bus_1, Car)      # False
typeCheck(bus_1, Vehicle)  # True


