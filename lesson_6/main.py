# import copy
#
# A = [
#     [1, 2],
#     [3, 4]
# ]
# # B = A[:]  # A.copy()
# B = copy.deepcopy(A)  # A.copy()
# # print(bin(10))
# print(hex(id(A[0])), hex(id(B[0])))
# print(f'A = {A} | id(A) = {hex(id(A))}\nB = {B} | id(B) = {hex(id(B))}\n')
# A[0] += [1, 2]
# print(f'A = {A} | id(A) = {hex(id(A))}\nB = {B} | id(B)

# raise KeyError('Error')

# while True:
#     try:
#         a = int(input('Enter number: '))  # 1
#         b = int(input('Enter number: '))
#         print(a / b)  # 2
#         break
#     except Exception as e:
#         print(f'Error: ValueError... Detail Info: {e}')
#         break
#     except KeyboardInterrupt:
#         print('U can\'t interrupt programm')
# except ArithmeticError as e:
#     print(f'Error: ZeroDivisionError!!! Detail Info: {e}')


# a = 4.5
#
# print(isinstance(a, (int, float)))

# number = input('Enter number: ')
# if not number.isdigit():
#     raise ValueError('Only numbers')

# import sys
#
# numbers = [1, 2, 3, 4]
# tuple_numbers = (1, 2, 3, 4)
# numbers = tuple(numbers)
# tuple_numbers = list(tuple_numbers)
# tuple_numbers.append(5)
# tuple_numbers = tuple(tuple_numbers)
#
# print(sys.getsizeof(numbers))
# print(sys.getsizeof(tuple_numbers))
#
# print(numbers)
# print(tuple_numbers)

# print(type(numbers), type(tuple_numbers))
# print(numbers, tuple_numbers)


# for i in a:
#     print(i)
# print(a)
# a.add(123)
# a.remove(123)
# a.discard(123)
# item = a.pop()
# print(a, item)
# a.update({123, 124, 125})
# print(a)
# a = {1, 2, 3, 4, 5}
# b = {5, 2, 3, 123, 124}

# print(a.intersection(b))
# print(a.difference(b))
# print(b.difference(a))
# print(a.symmetric_difference(b))

# print(3123 in b)

# print(b.issubset(a))
# print(a.issuperset(b))


# a = frozenset({1, 2, 3})
#
# print(a)

# user = ['first_name', 'last_name', ...]
# a = {
#     'first_name': 'Petr',
#     'last_name': 'Petrov',
#     123: {
#         '1': 100,
#         '2': 200
#     }
# }

# a['first_name'] = 123
# a['age'] = 30
# print('first_name' in a)
# print(a.get('first_name', 'Not found'))
# print(a.keys())
# print(a.values())
# print(a.items())
# item = a.pop('first_name', 'Not found')
# item = a.popitem()
# a.update({'age': 35, 'first_name': 'Ivan'})
# d = dict.fromkeys(['key_1', 'name'], None)
# print( d)
# print(user[1])
# print(a[123]['1'])


users = [
    {
        'first_name': 'Petr',
        'last_name': 'Petrov',
        'age': 30,
        'email': 'petr@example.com'
    },
    {
        'first_name': 'Ivan',
        'last_name': 'Petrov',
        'age': 35,
        'email': 'ivan@example.com'
    },
    {
        'first_name': 'Sasha',
        'last_name': 'Petrov',
        'age': 25,
        'email': 'sasha@example.com'
    }
]

for user in users:
    print(user['email'])

print('End')
