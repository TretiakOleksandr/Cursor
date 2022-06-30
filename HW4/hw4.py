#1
class Vehicle:
    def __init__(self, name, max_speed, total_capacity):
        self.name = name
        self.max_speed = max_speed
        self.total_capacity = total_capacity

    def fare(self):
        return self.total_capacity * 100

#2
class Bus(Vehicle):
    message = "Sorry, too big quantity"
    def __init__(self, name, max_speed, total_capacity, used_capacity): #6
        super().__init__(name, max_speed, total_capacity)
        self.used_capacity = used_capacity
        if self.used_capacity > self.total_capacity: #6
            raise "Error: I can`t contain so many :("

    def __str__(self):
        return f"Bus {self.name} \nmax speed: {self.max_speed} \ntotal capacity: {self.total_capacity} \nused capacity: {self.used_capacity if self.used_capacity <= self.total_capacity else self.message}"
#5
    def fare(self):
        return self.total_capacity * 100 * 1,1
#7
    def __len__(self):
        return self.total_capacity

#8
class Engine:
    def __init__(self, volume):
        self.volume = volume

    def get_volume(self):
        return self.volume


class Car(Vehicle, Engine): #9
    def __init__(self, name, max_speed, total_capacity):
        super().__init__(name, max_speed, total_capacity)

    def __str__(self):
        return f"Car {self.name} \nmax speed: {self.max_speed} \ntotal capacity: {self.total_capacity}"


#3
car_1 = Car('Audi', 180, 30)
car_2 = Car('Volvo', 200, 40)
car_3 = Car('Opel', 230, 50)

bus_1 = Bus('Mercedes', 300, 60, 50)
bus_2 = Bus('Renault', 310, 65, 60)


def typeCheck(x, checkedType):
    print(isinstance(x, checkedType))
#4
typeCheck(car_1, Car)      # True
typeCheck(car_2, Vehicle)  # True
typeCheck(bus_1, Car)      # False
typeCheck(bus_1, Vehicle)  # True
#10
print(Car.mro())

print(car_1)
print(car_2)
print(car_3)
print(bus_1)
print(bus_2)

print(bus_1.__len__())
print(bus_2.__len__())
