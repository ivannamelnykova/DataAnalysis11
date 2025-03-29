# # # # # # x = -10
# # # # #
# # # # # # if
# # # # #
# # # # # # # print(10 != 20)
# # # # # # # print('AAa' > 'AAA')
# # # # # #
# # # # # # if x > 5:
# # # # # #     print('X is greater than 5')
# # # # # # elif x > 0:
# # # # # #     print('X is positive')
# # # # # # else:
# # # # # #     print('X is either 0 or negative')
# # # # # #
# # # # # #
# # # # # # print('Good bye!')
# # # # #
# # # # # # user_input = input('Enter name: ')
# # # # # # # if len(user_input) > 0:
# # # # # # if user_input:
# # # # # #     print(f'Hello {user_input}!')
# # # # # # else:
# # # # # #     print('Hello stranger!')
# # # # #
# # # # # # id_code = input('Please enter Estonian national ID: ')
# # # # # # if len(id_code) == 11:
# # # # # #     print('ID', id_code)
# # # # # # else:
# # # # # #     if len(id_code) > 11:
# # # # # #         print('ID is too long')
# # # # # #     else:
# # # # # #         print('ID is too short')
# # # # #
# # # # # # elif len(id_code) < 11:
# # # # # #     print('ID is too short')
# # # # # # else:
# # # # # #     print('ID is too long')
# # # # #
# # # # # # x = 100
# # # # # #
# # # # # # if x > 0:
# # # # # #     print('x > 0')
# # # # # # if x > 5:
# # # # # #     print('x > 5')
# # # # # # if x == 100:
# # # # # #     print('x == 100')
# # # # #
# # # # #
# # # # # name = 'JACK'
# # # # # if name.istitle():
# # # # #     print('All good')
# # # # # else:
# # # # #     name = name.title()
# # # # #
# # # # # print(f'Hello {name}!')
# # # # #
# # # # # print('12323'.isdecimal())
# # # # # print('123.23'.isnumeric())
# # # #
# # # # example = 'Hello world!'
# # # # if 'world' in example:
# # # #     print('YES')
# # # # else:
# # # #     print('NO')
# # # #
# # # # example = [1, 2, 3, 4, 5]
# # # # if 3 in example:
# # # #     print('YES')
# # #
# # # # nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # # # for num in nums:
# # # #     # print(num ** 2)
# # # #     if (num ** 2) % 2 == 0:
# # # #         print(num)
# # #
# # # # for letter in 'Hello world!':
# # # #     print(letter.upper())
# # #
# # # for n in (1, 2, 3, 4, 5, 6):
# # #     print(n)
# #
# # print(list(range(100, 200, 2)))
# # for num in range (10000):
# #     print(num ** 2)
# #
# # x = -13
# # print(x > 0 or x < 20 and x != -13)
# # print(x > 0 and x < 20)
# # print(0 < x < 20)
# #
# # # if x is None:
# # if x != None:
# #     print('YES')
# #
# # name = 'Jack'
# # if name:
# #     print(name)
# #
# # name = ""
# # if not name:
# #     print('Please enter name')
#
#
# people = [
#     ('Jack', 'Smith', 25),
#     ('Mary', 'Gold', 20),
#     ('Simon', 'Cole', 45),
#     ('Sarah', 'Green', 30),
# ]
#
# for person in people:
#     print(person)
#
# for person in people:
#     print(f'This is {person[0]} {person[1]}. Age: {person[2]}')

x = 10

# while x > 0:
#     print(x, "I can't stop!")
#     x -= 1

while x > 0:
    if x == 8:
        continue
    if x == 5:
        break
    print(x)
    x -= 1