# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass


# class Square(Shape):
#     def __init__(self, side):
#         self.side = side


#     def area(self):
#         return self.side ** 2

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         import math
#         return math.pi *  (self.radius ** 2)

# sq = Square(4)
# print(f'Площадь квадрата: {sq.area()}')









# # class Dog:
# #     def make_sound(self):
# #         return 'Гав-гав'

# # class Cat:
# #     def make_sound(self):
# #         return 'Мяу-Мяу'

# # class Cow:
# #     def make_sound(self):
# #         return 'Му-му'


# # def sound_animal(animal_object):
# #     print(f'Животное говорит {animal_object.make_sound()}')


# # dog = Dog()
# # cat = Cat()
# # cow = Cow()

# # sound_animal(dog)
# # sound_animal(cat)
# # sound_animal(cow)








# # class BankAccount:
# #     def __init__(self, owner, balance):
# #         self.owner = owner
# #         self.__balance = balance

# #     def get_balace(self):
# #         return self.__balance

# #     def deposit(self, amount):
# #         if amount > 0:
# #             self.__balance += amount
# #         else:
# #             print('Сумма пополнения должна быть больше 0')

# # account = BankAccount('Иван', 1000)
# # account.deposit(500)
# # print(account.get_balace())
# # #print(account.__balance)
        