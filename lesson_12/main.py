import abc
import random
import time
from typing import Union, Callable
from typing import List
import functools
import itertools


class Engine:

    def __init__(self, engine_name: str, engine_version: int):
        self.name = engine_name
        self.version = engine_version


class Browser:
    _engine = Engine('Chrome', 14)
    _min_version = 13

    def __init__(self, name: str, version: str):
        self.name = name
        self.version = version
        self._is_run = False

    @classmethod
    def check_version(cls):
        print(cls)
        if cls._engine.version < cls._min_version:
            raise Exception('Engine version is not supported')

    @staticmethod
    def open():
        print('Start browser')
        print(Browser._min_version)
        browser = Browser('Chrome', '1.0')
        browser._is_run = True
        return browser

    @staticmethod
    def foo():
        print('foo')

    def close(self):
        print('Close browser')
        self._is_run = False

    def go_to(self, link: str):
        if not self._is_run:
            raise Exception('Browser is not run')
        print(f'Open {link}')


class ICar(abc.ABC):

    @abc.abstractmethod
    def drive(self):
        raise NotImplementedError

    @abc.abstractmethod
    def stop(self):
        raise NotImplementedError


class IElectroCar(abc.ABC):

    @abc.abstractmethod
    def charge(self):
        raise NotImplementedError


class IFlyable(abc.ABC):

    @abc.abstractmethod
    def fly(self):
        pass

    @abc.abstractmethod
    def lend(self):
        pass


class Tesla(ICar, IElectroCar):

    def drive(self):
        print('Drive Tesla')

    def stop(self):
        print('Stop Tesla')

    def charge(self):
        print('Charge Tesla')


class Mercedes(ICar):

    def drive(self):
        print('Drive Mercedes')

    def stop(self):
        print('Stop Mercedes')


class Airplane(ICar, IFlyable):

    def drive(self):
        print('Drive Airplane')

    def stop(self):
        print('Stop Airplane')

    def fly(self):
        print('Fly Airplane')

    def lend(self):
        print('Lend Airplane')


def charge_smt(electro_car: IElectroCar):
    electro_car.charge()


def drive_smt(car: ICar):
    car.drive()
    car.stop()


class PowTwo:
    pass


class Range:

    def __init__(self, from_: int, to_: int):
        self.from_ = from_
        self.to_ = to_
        self.current_ = from_

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_ > self.to_:
            raise StopIteration
        current = self.current_
        self.current_ += 1
        return current


class TimeIt:

    def __init__(self, func: Callable) -> None:
        self.function = func
        self.results = {}

    def __call__(self, *args, **kwargs):
        start = time.time()
        result = self.function(*args, **kwargs)
        print(f'{self.function.__name__} - {time.time() - start}s')
        return result


def range_generator(from_: int, to_: int):
    number = from_
    while number < to_:
        yield number
        number += 1
    while True:
        yield None


@TimeIt
def pow_numbers(numbers: List[Union[int, float]]) -> float:
    result = .0
    for number in numbers:
        result += number ** number
    return result


# @functools.cache
# def factorial(n):
#     return n * factorial(n-1) if n else 1


class File:

    def __init__(self, file_name: str, mode: str) -> None:
        self.file_obj = open(file_name, mode)

    def __enter__(self):
        print('Open')
        return self.file_obj

    def __exit__(self, *args, **kwargs):
        print('Close')
        print(args, kwargs)
        self.file_obj.close()


class Phone:

    def __init__(self, phone_number: str):
        self.phone_number = phone_number

    def __call__(self, phone_number: str):
        print(f'{self.phone_number} call {phone_number}')


if __name__ == '__main__':
    phone = Phone('123')
    phone('456')
