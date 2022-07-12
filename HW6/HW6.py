#1
print('--------------1--------------')
class Laptop:
    def __init__(self, model, batt_status, batt_capacity):
        self.model = model
        self.battery = Battery(batt_status, batt_capacity)

    def __str__(self):
        return f' Laptop {self.model} \n {self.battery}'

class Battery:
    def __init__(self, status, capacity):
        self.status = status
        self.capacity = capacity

    def __str__(self):
        return f'Battery {self.status}, capasity - {self.capacity}'

laptop = Laptop('Dell N1150', 'in charge', 9850)
print(laptop)

#2
print('--------------2--------------')
class GuitarString:
    def __init__(self, num, sound):
        self.num = num
        self.sound = sound

    def __str__(self):
        return f'{self.num} strings say {self.sound}'

class Guitar:
    def __init__(self, type_, string: GuitarString):
        self.type_ = type_
        self.string = string

    def __str__(self):
        return f'{self.type_} guitar with {self.string}'


gString_1 = GuitarString(6, 'Uiuiui')
gString_2 = GuitarString(7, 'Briatz')

guitar_el = Guitar('Electrical', gString_1)
guitar_ac = Guitar('Acoustic', gString_2)
print(guitar_el)
print(guitar_ac)

#3
print('--------------3--------------')
class Calc:
    @staticmethod
    def add_nums(a, b, c):
        return a + b + c

print(Calc.add_nums(2,3,7))

#4
print('--------------4--------------')
class Pasta:
    def __init__(self, ingr_list: list):
        self.ingr_list = ingr_list

    @classmethod
    def carbonara(cls):
        return cls(['forcemeat', 'tomato'])

    @classmethod
    def bolognaise(cls):
        return cls(['bacon', 'parmesan', 'eggs'])

pasta_1 = Pasta(["tomato", "cucumber"])
print(pasta_1.ingr_list)
pasta_2 = Pasta.bolognaise()
print(pasta_2.ingr_list)
pasta_3 = Pasta.carbonara()
print(pasta_3.ingr_list)

#5
print('--------------5--------------')
class Concert:
    max_visitors_num = 50

    def __init__(self, visitors_count):
        self.visitors = visitors_count

    @property
    def visitors_count(self):
        return self.visitors if self.visitors < self.max_visitors_num else self.max_visitors_num

concert_1 = Concert(48)
print(concert_1.visitors_count)
concert_2 = Concert(78)
print(concert_2.visitors_count)

#6
print('--------------6--------------')
import dataclasses
@dataclasses.dataclass
class AddressBookDataClass:
    key:int
    name:str
    phone_number:str
    address:str
    email:str
    birthday:str
    age:int
obj = AddressBookDataClass(3,'Vasyl','5556389','CA','rt@fg.g','28.08.88',33)
print(obj)
#7
print('--------------7--------------')
from collections import namedtuple
AddressBookDataClass_ = namedtuple('AddressBookDataClass_', ('key','name','phone_number','address','email','birthday','age'))
n_obj = AddressBookDataClass_(1,'Alex','5554562','Lviv,Rynok','a@b.c','25.12.90',22)
print(n_obj)

#8
print('--------------8--------------')
class AddressBook:
    def __init__(self ,key, name, phone_number, address, email, birthday, age):
        self.key = key
        self.name = name
        self.phone_number = phone_number
        self.address = address
        self.email = email
        self.birthday = birthday
        self.age = age

    def __str__(self):
        return f'Key: {self.key} \nName: {self.name} \nPhone: {self.phone_number} \nAddress: {self.address} ' \
               f'\nMail: {self.email} \nBirtday: {self.birthday} \nAge: {self.age}'

address_obj = AddressBook(5, 'Yuriy', '5551124','Kyiv','qwe@asd.zx','27.02.87',31)
print(address_obj)

#9
print('--------------9--------------')
class Person:
    name = "John"
    age = 36
    country = "USA"

john_1 = Person
john_1.age = 41
print(john_1.age)

#10
print('-------------10--------------')
class Student:
    id = 0
    name = ""

    def __init__(self, id, name):
        self.id = id
        self.name = name

student = Student(21,'Leo')
setattr(student, 'email', 'fgh@tyu.gh')
print(getattr(student, 'email'))

#11
print('-------------11--------------')
class Celsius:
    def __init__(self, temperature=0):
        self._temperature = temperature

    @property
    def fahr(self):
        return (self._temperature * 1.8)+32

gradus = Celsius(40)
print(gradus.fahr)