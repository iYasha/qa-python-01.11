

# for i in range(0, 10, 2):  # 5
#     print(i)
#
#
# for i in 1, 'Hello', True, False, 2.5:  # 5
#     print(i)
#
#
# for char in 'Hello!':  # 6
#     print(char)

# print(list(range(0, 10)))

# for i in range(0, 100_000, 2):
#     print(i)

# for i in range(100_000):
#     if i % 2 == 0:
#         print(i)


# text = 'Hello\' world'
# text = "Hello world"

# \' => '
# \n => перенос строки
# \t => tab

# 'hello' + 'world' = 'helloworld'
# 'hello' * 3 = 'hellohellohello'

"""
username = 'Petr'
print(f'Hello {username}')
"""

# text = '''Hello
# world
# !
# '''

# text = 'Hello\n' \
#        'world\n' \
#        '!'

# print('Hello\n'
#       'world\n'
#       '!')

# print(text)


# text = 'Hello ! \t'
# str_len = len(text)
#
# print(text)
# print(str_len)


# text = 'Hello'
# range(0, 10)  # 0 .. 9
# print(text[1:3])  # 1 .. 3
# print(text[:3])
# print(text[3:])
# print(text[::2])
# print(text[::-1])

# print(text[5])
# print(text[-1])

# print('Hello'.find('llo'))
# print('Hello'.find('l', 3))  # 2
# print('Hello'.rfind('l'))  # 3
# len('Hello')

# text = 'Lorem ipsum dolor sit amet, consectetur sit adipiscing elit.'

# print(text.find('sit'))
# print(text.find('sit', 19, 25))
# print(text.find('Petr'))

# if text.find('Petr') == -1:
#     print('Petr not found')

# incorrect_url = 'd.comomahttps://in'
# url = 'https://domain.com'
#
# # url.index('asdasd')
# has_secure = url.startswith('https://')
# has_com = url.endswith('.com')
#
# if has_secure and has_com:
#     print('Url is OK!')
# else:
#     print('Not OK!')


# text = '1 cou23nt'
#
# print(text.isdigit())
#
# text.isalnum()
# text.isdecimal()
# print('1.5a'.isdecimal())

# text = '123 Hello 33 world 222'

# for char in text:
#     if char.isdigit():
#         print(char)


# text = 'Lorem ipsum dolor sit amet, consectetur sit adipiscing elit.'

# replaced_text = text.replace('o', '@').replace('sit', '___')

# print(text)
# print(replaced_text)

# print('123,Hello,33,world 222'.split(','))

# print(text.title())
# print(text.lower())
# print(text.casefold())
# print(text.upper())
# print(text.capitalize())
# print(text.swapcase())


# full_name = '   Petr Petrenko '
#
# print(full_name.lstrip())
# print(full_name.rstrip())
# print(full_name.strip())

# name = 'Petr'
#
# print('Petr'.rjust(10, '*'))
# print('Vasya'.rjust(10, '*'))
# print('Vova'.rjust(10, '*'))
# print('AKSDasldjaklsdjalskdajlksdlaksjdasd'.rjust(10, '*'))

# names = ''
#
# for i in range(5):
#     name = input(f'Enter name #{i}')
#     names += name + ','
# print(names)

# names = ['Petr', 'Vasya', 'Dima', 'Vova', 'Ivan']  # list

# for i in range(5):
#     name = input(f'Enter name #{i}')
#     names.append(name)

# print(names[1])
# print(names[2])
# print(names[1:3])

# for name in names:
#     print(name)
# print(len(names))
#
# for idx in range(len(names)):
#     print(names[idx])

# print(names)
# names[1] = 'Masha'
# print(names)


# print([1, 2] == [1, 2])
# print([3, 1, 4] <= [3, 2, 3])


# names = ['Petr', 'Vasya', 'Dima', 'Vova', 'Ivan']

# is <> in

# print('Petr' in names)
# print('Petr23' not in names)
# print(True is names[0])

numbers = [2, 3, 4, 5, 2, 2, 2, 5, 5, 5, 10, -1, 234, 2, 555]
#
# print(max(numbers))
# print(min(numbers))
# print(sorted(numbers))
# print(sorted(numbers, reverse=True))
# print(numbers)
# list_1 = [1, 2]

print(numbers)
# numbers.append(1)
# numbers.extend(['Hello', 'world'])  # numbers = numbers + ['Hello', 'world']
# numbers.insert(5, 'Hello')
# numbers.insert(5, 'Hello')
# numbers.insert(5, 'Hello')
# numbers.insert(5, 'Hello')
# numbers.remove(2)
# first_item = numbers.pop()
# print(numbers.index('Hello'))
# print(numbers.count('Hello'))
# numbers.sort()
# numbers.reverse()
print(numbers)

