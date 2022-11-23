"""
Пользователь с клавиатуры вводит трех значное число в переменную number.
Переставьте первую и последнюю цифру переменной number, полученный результат
запишите в переменную reversed_number. Важно, что переменная number обязательно
должна быть типа данных int и для решения задачи можно использовать преобразование
типов данных только при получении числа из функции input.
"""

# text_number = input('Введите трехзначное число: ')
# # 120
# # 012 -> 210
# if text_number.isdigit() and len(text_number) == 3:
#     number = int(text_number)
#     # print(number[::-1])
#
#     first_digit = number // 100  # 1
#     second_digit = number % 100 // 10  # 2
#     third_digit = number % 10  # 3
#
#     reversed_number = third_digit * 100 + second_digit * 10 + first_digit
#     print(reversed_number)
# else:
#     print('Error')


# bool_val = False
#
# if bool_val == True:
#     number = 1
# else:
#     number = 0
#
# print(number)
# number = 1 if bool_val == True else 0
# print(number)

# if True:
#     pass

# run_loop = True

# while True:
#     name = input('Enter your name: ')
#     if name == 'quit':
#         break
#     print(f'Hello {name}!')


# number = input('Enter a number: ')  # asd
# while (number := input('Enter a number: ')) and not (number.isdigit() and len(number) == 3):
#     print('Error number')

# count = int(input('Enter your number: '))
#
# i = 0
#
# while i < count:
#     i += 1
#     print(f'начало иттерации #{i}')
#     if i % 3 == 0:
#         continue
#     print(i)

# i = 0
#
# while i < 10:
#     i += 1
#     if i < 5:
#         break
#     print(i)
# else:
#     print('While is over')

# run_loop = True
#
# while run_loop:
#     name = input('Enter your name: ')
#     if name == 'quit':
#         run_loop = False  # break
#     print(f'Hello {name}!')
# else:
#     print('While is over')

# print(list(range(10)))  # 0 .. 10
# print(list(range(5, 10)))  # 5 .. 10
# print(list(range(10, 0, -3)))  # 10 .. 1 (от 10 до 0 с шагом -3)
# print(list(range(0, 10, 3)))  # от 0 до 10 с шагом 3

# for name in 'Petr', 'Sasha', 'Vasya':  # 5, 6, 7, 8, 9
#     print(f'Hello {name}')

# for _ in range(10):
#     print('Hello world')


# for i in range(10):
#     if i % 3 == 0:
#         continue
#     print(i)

# for i in range(10):  # 1
#     for j in range(10):  # 2
#         print(i, j)
#         if j == 5:
#             break


# pip
# poetry


import random
import os

# print(random.uniform(1, 10))

while True:
    url = input('Enter url: ')
    if url == 'quit':
        break
    os.system(f'open {url}')

# count = 10
#
# for _ in range(count):
#     random_number = random.randint(1, 10)
#     print(random_number)


print(f'End')
