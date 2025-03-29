# x = 0
#
#
# if x > 5:
#     print('X is greater than 5')
# elif x > 0:
#     print('X is positive')
# else:
#     print('X is either 0 or negative')
#
# print('Good bye!')

# user_input = input('Enter name: ')
# # if len(user_input) > 0:
# if user_input:
#     print(f'Hello {user_input}!')
# else:
#     print('Hello stranger!')

# id_code = input('Please enter Estonian national ID: ')
# if len(id_code) == 11:
#     print('ID', id_code)
# else:
#     if len(id_code) > 11:
#         print('ID is too long')
#     else:
#         print('ID is too short')

# if len(id_code) == 11:
#     print('ID', id_code)
# elif len(id_code) < 11:
#     print('ID is too short')
# else:
#     print('ID is too long')

# x = 100

# if x > 0:
#     print('X > 0')
# if x > 5:
#     print('X > 5')
# if x == 100:
#     print('X == 100')

# name = "JACK"
# if name.istitle():
#     pass
# else:
#     name = name.title()
#
# print(f'Hello {name}!')
#
# print('123.23'.isnumeric())


# example = 'Hello world!'
# if 'world' in example:
#     print('YES')
# else:
#     print('NO')
#
# example = [1, 2, 3, 4, 5]
# if 3 in example:
#     print('YES')
#

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# for num in nums:
#     if (num ** 2) % 2 == 0:
#         print(num)
#

# for letter in 'Hello world!':
#     print(letter.upper())

# for n in (1, 2, 3, 4, 5, 6):
#     print(n)


# print(list(range(100, 200, 2)))
# for num in range(10000):
#     print(num ** 2)

# for num in range(1, 101):
#     if num % 3 == 0 and num % 5 == 0:
#         print(num, 'FIZZBUZZ')
#     elif num % 3 == 0:
#         print(num, 'FIZZ')
#     elif num % 5 == 0:
#         print(num, 'BUZZ')

# x = 20
# print(x > 0 and x < 20)
# print(0 < x < 20)
#
# if x is not None:
#     print('YES')
#
# name = ""
# if not name:
#     print('Please enter name')


# people = [
#     ('Jack', 'Smith', 25),
#     ('Mary', 'Gold', 20),
#     ('Simon', 'Cole', 45),
#     ('Sarah', 'Green', 30),
# ]
#
# for name, surname, age in people:
#     print(f'This is {name} {surname}. Age: {age}')
#

# x = 11
#
# while x > 0:
#     x -= 1
#     if x == 8:
#         continue
#     if x == 5:
#         break
#     print(x)

for char in "Python":
    if char == 'h':
        continue
    if char == 'o':
        break
    print(char)
