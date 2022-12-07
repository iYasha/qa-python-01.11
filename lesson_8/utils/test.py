
A = 10


def greetings_v2(user_name, age=None):
    if age is None:
        print(f'Hello {user_name}!')
    else:
        print(f'Hello {user_name}! Your age is {age}')

