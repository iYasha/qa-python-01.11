"""
Comment 1
Comment 2
"""
# Comment 1

# a = 10
# b = 20
#
# print(a)
# print(13 >= b)
# print(13 != b)

# a += 2  # a = a + 2
# a += 1
#
# print(a)

# print(a + b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a ** b)
# print(a % b)
# print(a // b)
# print(a ^ b)

# status_code = 200  # 200 - 299

# print(status_code >= 200 and status_code <= 299)  # 200 <= status_code <= 299
# print(True and False and True)
# print(False or True or False)
# print(not (status_code >= 200 and status_code <= 299))

# a = 'Hello world'
# b = 'XOX'
#
# print('world' in a)
# print('world1' not in a)

# a = 'Hello world'
# b = 'Hello world'
#
# print(a in b)
# print(4 is not b)
# print(id(a))
# print(id(b))
# print(id(4))


# print('H\tello\nworld \\ ')

# name = input('Enter your name: ')
# age = input('Enter your age: ')
# template = 'Hello {}'
#
# print('Hello', name)
# print('Hello ' + name)
# print( 'Hello %s' % name )
# print( template.format(name) )
# print( f'Hello { name }' )


# a = int(input('Enter first number: '))  # '2' -> int('2') -> 2
# b = int(input('Enter second number: '))
#
# print(type(a), type(b))
#
# print(a + b)

# a = '50'  # 50.5 -> 50 | 50 -> 50
#
# b = int(float(a))
#
# print(bool(' '))
#
# print(f'A TYPE IS {type(a)} | B TYPE IS {type(b)}')
# print(f'A VALUE IS {a} | B VALUE IS {b}')

# status_code = int(input('Enter status code: '))

"""
100 - 199 (Information)
200 - 299 (OK)
300 - 399 (Redirect)
400 - 499 (Client error)
500 - 599 (Server Error)
"""

# if 100 <= status_code <= 199:
#     print('Response is Information')
# elif 200 <= status_code <= 299:
#     print('Response is OK')
#     name = input('Enter your name: ')
#     if not name:  # ''
#         print('Invalid name')
#     else:
#         print(f'Hello {name}')
# elif 300 <= status_code <= 399:
#     print('Response is Redirect')
# elif 400 <= status_code <= 499:
#     print('Response is Client error')
#
# elif 500 <= status_code <= 599:
#     print('Response is Server Error')
# else:
#     print('Invalid response')

# if True:
#     print('1')
# elif True:
#     print('2')
# elif True:
#     print('3')
# else:
#     print('Error')

print('end')

if ...:
    pass

if ...:
    pass
else:
    pass

if ...:
    pass
elif ...:
    ...

if ...:
    pass
elif ...:
    pass
else:
    pass


"""
1) Если переменная a равна 10, то выведите 'Верно', иначе выведите 'Неверно'.
"""

# a = 10
#
# if a == 10:
#     print('Верно')
# else:
#     print('Неверно')

"""
2) В переменной a лежит число от 0 до 59. Определите в какую четверть часа попадает это число 
(в первую, вторую, третью или четвертую).
"""

# a = 1000
#
# if 0 <= a <= 15:
#     print('First')
# elif 16 <= a <= 30:
#     print('Second')
# elif 31 <= a <= 45:
#     print('Third')
# elif 46 <= a <= 59:
#     print('Fourth')
# else:
#     print('Error')

a = 11
b = '+' if a % 2 == 0 else '-'
print(b)


"""
3) Если переменная test не равна true, то выведите 'Верно', иначе выведите 'Неверно'. 
Проверьте работу скрипта при test, равном true, false.
4) Переменная num может принимать 4 значения: 1, 2, 3 или 4. Если она имеет значение '1', 
то в переменную result запишем 'зима', если имеет значение '2' – 'весна' и так далее.
"""

