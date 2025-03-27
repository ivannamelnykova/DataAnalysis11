# # empty = [] # List (list)
# # empty = list()
# # print(type(empty))
# #
# # random_list = [123, 12.32, 'Hello world', True, None, [1,2, [3,4,5], 6], True, True, True]
# # print(len(random_list))
# # print(random_list[0])
# # print(random_list[5][2][2] ** 2)
# # print(random_list[2].upper()[0:5].lower())
# #
# # print(random_list[1:4])
# #
# # # print(random_list[2:4])
# # # print(random_list[:])
# #
# # a = 10
# # b = 'Hello'
# # c = [a, b]
# # print(c)
# #
# # courses = ['English', 'Math', 'Physics', 'Programming']
# # print(courses[1])
# # courses[1] = 'Art'
# # print(courses)
# # print(courses)
# #
# # courses[1:3] = ['History']
# # print(courses)
# #
# # print(list('Hello world!'))
# #
# # cities = ['Tallinn', 'London', 'Madrid', 'Oslo', 'tallinn', '123', 'oslo', 'london']
# # nums = [1, 4, 6, 8, 3, 4, 2, 11, 111]
# #
# # # cities.append('Washington')
# # # print(cities)
# # # cities.insert(0, 'New-York')
# # # print(cities)
# #
# # # cities.extend(['Rio', 'Beijing'])
# # # print(cities)
# #
# # # cities.remove('Madrid')
# # # print(cities)
# # # deleted = cities.pop(0)
# # # print(cities)
# # # print(deleted)
# #
# # # cities.reverse()
# # # print(cities)
# # # print(cities[::-1])
# # # cities.sort(reverse=True)
# # # print(cities)
# # # nums.sort()
# # # print(nums)
# #
# # # print([1, 2, 3] + [4, 5, 6])
# #
# # print(cities.index('Oslo'))
# # print(cities.count('Oslo'))
# #
# # sample = 'Hello people of planet Earth, good bye!'
# # print(sample.split(', '))
# #
# # print('2000-12-02'.split('-'))
# # # print('***'.join(cities))
# # print('\n'.join(cities))
# #
# # # a = 5
# # # b = a
# # # a += 10
# # # print(a, b)
# #
# # # a = 'Hello'
# # # b = a
# # # a += 'World'
# # # print(a, b)
# #
# # a = [1, 2, 3]
# # b = a.copy()
# # a.append(4)
# # b.append(5)
# # print(a, b)
# # print(id(a))
# # print(id(b))
# #
# # a = 5
# # b = 5
# # print(id(a))
# # print(id(b))
# #
# # print(sum(nums))
# # print(min(nums))
# # print(max(nums))
# #
# # print(max(cities))
# # print(min(cities))
#
# empty = ()
# print(type(empty))

# tup1 = (1, 2, 3, 4, 5, 6)
# print(tup1[2:5] + (1, 23, 43))
# tup1 = list(tup1)
# print(tuple(tup1))
#
# print(sum(tup1, 1000))

courses = {'Math', 'Art', 'Physics', 'Programming', 'Art', 'Art'}
print(courses)

# x = [1, 1, 1, 2, 2, 2, 3, 3, 3]
# x = list(set(x))
# print(x)

set1 = {'Math', 'Art', 'Physics'}
set2 = {'Math', 'Physics', 'History'}

print(set1.difference(set2))
print(set2.difference(set1))

print(set1.intersection(set2))

print(set1.symmetric_difference(set2))


