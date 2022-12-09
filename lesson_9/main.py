
# with open('numbers') as f:
#     f.read()
#     f.readlines()
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())
#     print(f.readline())

def foo(*args, **kwargs):
    print('')


numbers = [1, 2, 3, 4, 5, 6]  # O(N)
# 100 + 2 = 102
print(numbers[2])  # O(1)
dictionary = {
    'a': 4,
    'd': 3,
    'c': 2,
    'b': 1
}

dict_2 = {
    'name': 'Petr',
    'age': 35
}

new_dict = {**dict_2, **dictionary, 'a': 1000}  # dict_2 | dictionary
print(new_dict)

# a, *_, b = numbers
#
# print(a, b)

# text = ' '.join(map(str, numbers))
# print(text)
# foo(*numbers, 100)

