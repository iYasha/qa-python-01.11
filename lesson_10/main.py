
"""
public
protected
private
"""
from typing import List


class Person:
    country = 'Ukraine'

    def __init__(self, name: str, age: int, phone_number: str):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.__friends = []

    def say_hello(self):
        print(f'Hello! {self.name} {self.age} {self.country}')

    def add_friend(self, other_person):
        self.__friends.append(other_person)

    def print_all_friends(self):
        for friend in self.__friends:
            print(friend.name)

    def _print_country_code(self):
        print(self.phone_number.split()[0])

    def __str__(self):
        return f'<Person name={self.name} age={self.age} phone_number={self.phone_number}>'

    def __int__(self):
        return self.age

    def __add__(self, other):
        if isinstance(other, str):
            return self.name + other
        else:
            return self.age + other

    def __iadd__(self, other):
        self.age += other
        return self

    def __gt__(self, other):
        if isinstance(other, (int, float)):
            return self.age > other
        elif isinstance(other, Person):
            return self.age > other.age
        else:
            return False


class Student(Person):

    def __init__(self, name: str, age: int, phone_number: str, avg_mark: float):
        self.name = name
        self.age = age
        self.phone_number = phone_number
        self.__friends = []
        self.avg_mark = avg_mark

    def do_homework(self):
        print(f'{self.name} doing homework')


bob = Student('Bob', 25, '+1 123412512412', 100)
tom = Person('Tom', 32, '+380 661234124')
john = Person('John', 35, '+380 55123124')


bob.say_hello()
bob.do_homework()
# tom.do_homework()


# def myprint(*args):
#     print(f'args {args}')
#     print(*args)


# class NewDict(dict):
#     def __hash__(self):
#         return hash(tuple(self.values()) + tuple(self.keys()))



# dict_1 = NewDict({
#     'key1': 'value1'
# })
# print(hash(dict_1))  # 10
# print(hash(dict_1))  # 10
# dictionary = {
#     'key': 'value',
#     dict_1: 'value2'
# }
# dict_1['key2'] = '...'
# print(hash(dict_1))  # 15
# print(dictionary[dict_1])


# def do_smt(obj):
#     print(...)

# [1, 2] >= [0, 3]

# bob = Person('Bob', 25, '+1 123412512412')
# tom = Person('Tom', 32, '+380 661234124')
# john = Person('John', 35, '+380 55123124')
#
# print(bob < tom)


# print(bob, tom, john)
# print(bob + 'Hello')
# print(4 + bob)

# print(bob, 'int =', int(bob))


# bob.add_friend(tom)
# print(bob._Person__friends)
# bob.add_friend(john)

# bob._print_country_code()


# bob.print_all_friends()

