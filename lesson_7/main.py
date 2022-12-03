
# file = open('data.txt')
# print('File data: ', file.read())
# print('File data: ', file.read())
# print('File data: ', file.read())
# first_line = file.readline()
# print(file.readlines()[5])
# first_line = open('data.txt', 'r').readline()
# print(file.read())

# file = open('img.jpg', 'rb')
# # file.writelines(['Hello\n', 'world\n',])
# binary_data = file.read()
# file.close()
#
# open('img_2.jpg', 'w').write(binary_data.decode())


# text = input('Enter text: ')
#
# file = open('text.txt', 'w')
# file.write(text)

# file_name = input('FileName: ')

# line_count = input('Enter line count: ')
# if not line_count.isdigit():
#     raise ValueError('Line count must be a number')
#
# file = open('2022-12-02.txt', 'x')
#
# for i in range(int(line_count)):
#     line = input('Enter line: ')
#     file.write(line + '\n')

# import pickle
import json


user = {
    'name': 'John',
    'age': 25,
    'address': 'New York',
    'asd': True,
    'none_object': None,
    'children': ['Maria', 'Alex']
}
file_name = 'john.json'

# JSON
# Serializer
# f = open(file_name, 'w')
# json.dump(user, f)
# user_json = json.dumps(user)
# print(user_json, type(user_json))

# Deserializer
# f = open(file_name, 'r')
# user_obj = json.load(f)
# user_obj = json.loads(f.read())
# print(user_obj, type(user_obj))

# Pickle
# Serializer
# f = open(file_name, 'wb')
# pickle.dump(user, f)
# bytes_data = pickle.dumps(user)
# f.write(bytes_data)

# Deserializer
# f = open(file_name, 'rb')
# user_obj = pickle.load(f)
# user_obj = pickle.loads(f.read())
# print(user_obj)

# Serializer
# f = open(file_name, 'w')
# f.write(user['name'] + '\n')
# f.write(str(user['age']) + '\n')
# f.write(user['address'] + '\n')

# Deserializer
# user = {}
# f = open(file_name, 'r')
# user['name'] = f.readline().strip()
# user['age'] = int(f.readline().strip())
# user['address'] = f.readline().strip()

# print(user)


# with open(file_name, 'r') as f:
#     print(f.read())
#     print(f.closed)
#
# print(f.closed)
# print('end')


# a = 'Value if true' if 5 > 10 else 'Value if false'
# print(a)

import random
#
# numbers = [x ** 2 for x in range(10) if (x ** 2) % 2 != 0]
# random_numbers = [random.randint(1, 100) for _ in range(50)]
# print(random_numbers)
#
# numbers = []
# for x in range(10):
#     if (x ** 2) % 2 != 0:
#         numbers.append(x ** 2)

# unique_random_numbers = {random.randint(1, 100) for _ in range(50)}
# print(unique_random_numbers, type(unique_random_numbers))

# indexed_random_numbers = {i: random.randint(1, 100) for i in range(50)}
# users = {input('Enter name: '): input('Enter phone number: ') for i in range(2)}
# print(users)

# gen = (x for x in range(10))
# print(next(gen))
# print(next(gen))

# print(abs(-123.4))
# print(abs(123))

# values = [True, False, True, True]
# names = ['Petr', '', 'Vasya', 'Sasha']
#
# print(all(names))  # True and False and True and True
# print(any(values))  # True or False or True or True
# breakpoint()

# value = 'Hello'
#
# print(callable(value))

# print(chr(65))
# print(ord('A'))
#
# for i in range(65, 91):
#     print(chr(i), end=' ')

# print(dir(random))


# values = ['Hello', 'petr', 123, 4, 5, 6]
#
# for idx, value in enumerate(values):
#     print(idx, value)

# expression = input('Math expression: ')
#
# print(eval(expression))
# print(exec(expression))

# values = ['Hello', 'petr', None, 123, 4, 5, 6]
# numbers = [12, 23, -23, 2, 3, 4, 5, 6, 700, 8, 9, 10]


# print(sum(numbers))
# new_numbers = list(reversed(numbers))
# print(new_numbers, type(new_numbers))

# import math
#
# print(math.floor(12.5))
# print(math.ceil(12.5))

# print(round(123.456124142, 2))
# print(round(123.5, 2))

# print(max(numbers))
# print(min(numbers))

# slice(numbers, 2, 5)  # numbers[2:5]

# print(pow(2, 10))
# print(2 ** 10)
# print(list(filter(None, values)))
# print(list(filter(lambda x: x % 2 == 0, numbers)))
# print(globals())
# print(list(map(lambda x: x ** 2, numbers)))
# print(list(map(str, numbers)))

# print(hash('Hello'))
# print(help(print))

# number = '20'
#
# print(isinstance(number, int))

# keys = ['name', 'age', 'address']
# values = ['Petr', 25, 'New York']
#
# dictionary = dict(zip(keys, values))
# print(dictionary)


# while True:
#     try:
#         number = int(input('Enter number: '))
#         break
#     except ValueError:
#         print('Value must be a number')


user_numbers = [input('Enter number: ') for _ in range(5)]
numbers = sum(map(int, user_numbers))

print(numbers)



