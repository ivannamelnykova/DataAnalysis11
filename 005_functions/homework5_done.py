# Task 1
def square_list(lst):
    return list(map(lambda num: num ** 2, lst))

def square_list2(lst):
    result_list = []
    for i in range(len(lst)):
        result_list.append(lst[i] ** 2)
    return result_list

print(square_list([1, 2, 3, 4, 5]))
print(square_list2([1, 2, 3, 4, 5]))

# Task 2
def odd_even_count(lst):
    even_count = 0
    odd_count = 0

    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    return odd_count, even_count

print(odd_even_count([1, 2, 3, 4, 5]))

# Task 3
def largest(lst):
    if len(lst) == 0:
        return None

    maximum = lst[0]
    for i in range(len(lst)):
        if lst[i] > maximum:
            maximum = lst[i]

    return maximum

print(largest([1, 5, 10, 3, -1]))
print(largest([]))

# Task 4
def fizz_buzz(start, end):
    for num in range(start, end + 1):
        if num % 3 == 0 and num % 5 == 0:
            print(num, 'FIZZBUZZ')
        elif num % 3 == 0:
            print(num, 'FIZZ')
        elif num % 5 == 0:
            print(num, 'BUZZ')

fizz_buzz(1, 100)


