# # # # # # # # # # a = 0
# # # # # # # # # # b = 10
# # # # # # # # # # print(a + b)
# # # # # # # # # #
# # # # # # # # # # a = 8
# # # # # # # # # # b = 9
# # # # # # # # # # print(a + b)
# # # # # # # # #
# # # # # # # # # a = 0
# # # # # # # # # b = 10
# # # # # # # # #
# # # # # # # # # def sum_to_numbers(a: int,  b: int):
# # # # # # # # #     print(a + b)
# # # # # # # # #
# # # # # # # # # sum_to_numbers(10, 23)
# # # # # # # # # sum_to_numbers(a, b)
# # # # # # # # # sum_to_numbers(b, a)
# # # # # # # # # sum_to_numbers('Hello', 'World')
# # # # # # # #
# # # # # # # # # def say_hello():
# # # # # # # # #     return 'Hello world!'
# # # # # # # # #
# # # # # # # # # x = say_hello()
# # # # # # # # # print(x)
# # # # # # # # # # print(say_hello())
# # # # # # # # # #
# # # # # # # # # # print('hello'.upper())
# # # # # # # # # # print([].append('Hello'))
# # # # # # # #
# # # # # # # # # def say_hello(name: str):
# # # # # # # # #     print(f'Hello {name}!')
# # # # # # # # #
# # # # # # # # # say_hello('Ivanna')
# # # # # # # # #
# # # # # # # # #
# # # # # # # # # names = ['Sarah', 'Jack', 'Bob', 'Mary']
# # # # # # # # # for name in names:
# # # # # # # # #     say_hello(name)
# # # # # # # #
# # # # # # # # def area(side_a: float, side_b: float) -> float:
# # # # # # # #     return side_a * side_b
# # # # # # # #
# # # # # # # # def count_total_material(carpet_area: float, qty: int) -> float:
# # # # # # # #     return carpet_area * qty
# # # # # # # #
# # # # # # # #
# # # # # # # # def print_results(order: list):
# # # # # # # #     carpet_area = area(order[0], order[1])
# # # # # # # #     total = count_total_material(carpet_area, order[2])
# # # # # # # #     print(f'Total material needed: {total}cm2')
# # # # # # # #
# # # # # # # #
# # # # # # # # order = [50, 80, 37] # [width, height, qty]
# # # # # # # #
# # # # # # # # print_results(order)
# # # # # # # # print(area(12, 23))
# # # # # # #
# # # # # # #
# # # # # # # # def number_sign(num: int) -> str:
# # # # # # # #     if num < 0:
# # # # # # # #         return f'{num} is negative'
# # # # # # # #     elif num > 0:
# # # # # # # #         return f'{num} is positive'
# # # # # # # #     return f'{num} is zero'
# # # # # # # #
# # # # # # # # print(number_sign(0))
# # # # # # #
# # # # # # # a, b, c = 10, 20, 30
# # # # # # #
# # # # # # # def example():
# # # # # # #     a, b, c = 1, 2, 3
# # # # # # #     print('func', a, b, c)
# # # # # # #
# # # # # # # example()
# # # # # # # print('global', a, b, c)
# # # # # # #
# # # # # # # del a, b, c
# # # # # # #
# # # # # # # def asd():
# # # # # # #     x = 50
# # # # # # #     return x
# # # # # # #
# # # # # # # x = asd()
# # # # # #
# # # # # # def example(a, b, c=0):
# # # # # #     return a + b + c
# # # # # #
# # # # # # print(example(123, 123))
# # # # # # print(example(c=100, b=23, a=123))
# # # # #
# # # # #
# # # # # def remove_duplicates_and_sort(iterable: list | set | tuple, desc=None) -> list:
# # # # #     iterable = list(set(iterable))
# # # # #     if desc:
# # # # #         iterable.sort(reverse=True)
# # # # #     else:
# # # # #         iterable.sort()
# # # # #     return iterable
# # # # #
# # # # # print(remove_duplicates_and_sort([3, 3, 2, 1, 5, 7, 7, 7, 8, 4, 3, 4, 4, 2], desc=True))
# # # #
# # # # def print_many(a , b, *args): # arguments
# # # #     print('A', a)
# # # #     print('B', b)
# # # #     print(args)
# # # #
# # # #
# # # # print_many(123, 123, 32, 'asdas d', [1, 2, 3, 4], 'asdf')
# # #
# # # def kwarks_func(**kwargs):
# # #     print(kwargs)
# # #
# # # kwarks_func(name='Jack', surname='Smith', age=20, salary=2000)
# #
# #
# # x = [1, 2, 3]
# # y = [0, *x, 4]
# # print(y)
# # var1, var2, *var3 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# # print(var1)
# # print(var2)
# # print(var3)
#
# import helpers
# quadruple = 123
# print(helpers.quadruple(123))
#
# from helpers import triple, quadruple
from helpers_2 import *

print(triple(123))
print(quadruple(123))


########
def simple(start, middle, end):
    return sum([start, middle, end]) / 3

print(simple(5, 6, 10))


def average(lst):
    return sum(lst) / len(lst)

x = average([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(x)


def average2(lst):
    s = 0
    n = 0
    for i in range(len(lst)):
        s = s + lst[i]
        n = n + 1

    return s / n


print(average2([1, 2, 43, 54, 55]))

