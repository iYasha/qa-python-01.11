

# class Engine:
#     def __init__(self, model: str):
#         self.model = model
#
#
# class Car:
#     def __init__(self, brand_name: str):
#         self.__engine = Engine('V8')
#         self.brand = brand_name
#         self.__color = 'red'
#
#     @property
#     def engine_model(self) -> str:
#         return self.__engine.model
#
#     @engine_model.setter
#     def engine_model(self, model: str) -> None:
#         print('Changing engine model')
#         if not isinstance(model, str) or len(model) < 2:
#             raise ValueError('Incorrect model')
#         self.__engine.model = model
#
#     @engine_model.deleter
#     def engine_model(self) -> None:
#         print('delete attr')
#         self.__engine.model = None
#
#     @property
#     def test(self):
#         return 'Hello'
#
#     obj.test = ...
#     @test.setter
#     def test(self, value):
#         print('setter')
#
#     del obj.test
#     @test.deleter
#     def test(self):
#         print('deleter')

    # def get_engine_model(self) -> str:
    #     return self.__engine.model
    #
    # def set_engine_model(self, model: str) -> None:
    #     if not isinstance(model, str) or len(model) < 2:
    #         raise ValueError('Incorrect model')
    #     self.__engine.model = model


# tesla = Car('Tesla')
# print(tesla.engine_model)
# tesla.engine_model = 'V3'
# print(tesla.engine_model)
# del tesla.engine_model
# print(tesla.engine_model)
# tesla.set_engine_model('V12')
# print(tesla.get_engine_model())
import json


class Human:

    def __init__(self, name: str, age: int, *args, **kwargs):
        self.name = name
        self.age = age

    def eat(self, food_name: str):
        print(f'{self.name} is eating {food_name}')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def work(self):
        print(f'{self.name} is working')

    def play(self):
        print(f'{self.name} is playing')


class McDonaldsWorker:

    def __init__(self, *args, position: str, **kwargs):
        self.position = position

    def work(self):
        print(f'{self.position} is cooking')


class Student(Human, McDonaldsWorker):
    def __init__(self, *args, mark: int, **kwargs):
        # super(Human, self).__init__(*args, **kwargs)
        # super(McDonaldsWorker, self).__init__(*args, **kwargs)
        McDonaldsWorker.__init__(self, *args, **kwargs)
        Human.__init__(self, *args, **kwargs)
        self.mark = mark

    def learn(self):
        print(f'{self.name} is learning')


class Teacher(Human):

    def teach(self):
        print(f'{self.name} is teaching')


def eat_fruit(fruit_name: str, human: Human):
    human.eat(fruit_name)


users = [
    Student('John', 25, mark=100, position='master cef'),
    Teacher('Bob', 30),
    Teacher('Petya', 25),
]

for user in users:
    eat_fruit('Banana', user)


# john = Student('John', 25, position='Main Cef', mark=100)  # Student
# bob = Teacher('Bob', 30)  # Teacher

# john.work()


class Zero:

    def foo(self):
        print('ZERO foo')


class A:

    def foo(self):
        print('A foo')


class B(A):
    pass
    # def foo(self):
    #     print('B foo')


class C(A):

    def foo(self):
        print('C foo')


class D(B, C):
    pass

# d = D()
# print(D.__mro__)
# d.foo()


class Data:
    filename: str

    def set_file_name(self, filename: str) -> None:
        self.filename = filename

    def save(self) -> None:
        raise NotImplementedError

    def load(self) -> None:
        raise NotImplementedError


class Human(Data):
    filename: str = 'human.json'

    def __init__(self, name: str, age: int, *args, **kwargs):
        self.name = name
        self.age = age

    def eat(self, food_name: str):
        print(f'{self.name} is eating {food_name}')

    def sleep(self):
        print(f'{self.name} is sleeping')

    def work(self):
        print(f'{self.name} is working')

    def play(self):
        print(f'{self.name} is playing')

    def save(self) -> None:
        with open(self.filename, 'w') as f:
            json.dump({'name': self.name, 'age': self.age}, f)

    def load(self) -> None:
        with open(self.filename) as f:
            data = json.load(f)
            self.name = data.get('name')
            self.age = data.get('age')


class Car:
    pass


def save_all_data(obj: Data):
    if not isinstance(obj, Data):
        raise ValueError
    obj.save()


save_all_data(Human('John', 30))

