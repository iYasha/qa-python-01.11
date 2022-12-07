

def greetings(user_name, age):
    print(f'Hello {user_name}! Your age is {age}')


# output = greetings(age=34, user_name='John')
# print(output)  # output is None
# greetings('Petr', 25)


def our_sum_func(numbers):
    if not isinstance(numbers, (list, set, tuple)):
        return
    result = 0
    for number in numbers:
        result += number
    return result


# summ = our_sum_func([1, 2, 4, 5, 6, 7])
# failed_result = our_sum_func(1)
# print(summ, failed_result)


# greetings_v2('John', 31)
# greetings_v2('Petr')


from typing import Union


def add_number(item: Union[int, float], numbers: list = None) -> list:
    if numbers is None:
        numbers = []
    numbers.append(item)
    return numbers


# new_list = add_number(1, [])
# print(new_list)
# print(add_number(3))
# print(add_number(2))
# print(add_number(2, [10, 8, 6, 4]))

# def print(*args)

# print(2, 1, 2, 4,5 ,5, 6, 7, 8 ,65, 4 , 4)

import operator


def get_operation(op_type):
    if op_type == '+':
        return operator.add
    elif op_type == '-':
        return operator.sub
    elif op_type == '*':
        return operator.mul
    elif op_type == '/':
        return operator.truediv


def calc(*args, op='+'):
    if not args:
        return None
    result = args[0]
    op_func = get_operation(op)
    for item in args[1:]:
        result = op_func(result, item)
    return result

# value = calc(1, 2, 3, 4, 6, 7, op='/')
# print(value)


def from_keys(dictionary=None, **kwargs):
    if dictionary is None:
        dictionary = {}
    dictionary.update(kwargs)
    return dictionary


def print_smt(content, **kwargs):
    if file_name := kwargs.get('file_name'):
        f = open(file_name, kwargs.get('mode', 'w'))
        f.write(content)
        f.close()
    else:
        print(content)


# d = {'hello': 'world'}
# d = from_keys(d, a=4, key='value', b=10)
# print(d)

def key_for_sort_users(item):
    return item['age']


# users = [
#     {
#         'name': 'John',
#         'age': 30,
#     },
#     {
#         'name': 'Petr',
#         'age': 25,
#     },
#     {
#         'name': 'Ivan',
#         'age': 40,
#     },
# ]

# sorted_users = sorted(users, key=lambda x: x['age'], reverse=True)
# sorted_users = sorted(users, key=key_for_sort_users, reverse=True)
# print(sorted_users)
# sum_func = lambda a, b: a + b
# print(sum_func(4, 5))

# from collections import Counter, defaultdict


# text = 'hello, world abc, hello,'

# counter = Counter(text)
# counter = Counter(a=10, b=20, c=30)
# print(counter.most_common(2))

# dictionary = defaultdict(int)
#
# for char in text:
#     dictionary[char] += 1
#
# print(dictionary)


# from utils import test

# from utils.test import greetings_v2, A


# test.greetings_v2('John', 24)
# print(test.A)
# test.A = 30
# print(test.A)

# greetings_v2('John')
# print(A)


# from auth import tests as auth_tests
# from module_1 import tests as module_1_tests
#
# print(auth_tests.A)
# print(module_1_tests.B)

from auth.tests import run_tests


print(run_tests())

