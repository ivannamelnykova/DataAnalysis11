# Task 1
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}
print(set_a.symmetric_difference(set_b))

diff_a = set_a.difference(set_b)
diff_b = set_b.difference(set_a)
print(diff_a)
print(diff_b)

# Task 2
names = ['Jack', 'Mary', 'Samantha', 'George', 'Simon', 'John']
print('\n'.join(names))

# Task 3
numbers = [2, 53, 12, 87, 65, 32, 12, 2, 65, 32]
total_sum = sum(numbers)
unique_sum = sum(set(numbers))

print(total_sum)
print(unique_sum)

# Task 4
studentsA = ['Jack', 'Bob', 'Mary']
studentsB = ['Bob', 'Sarah', 'Simon']

unique_students = list(set(studentsA + studentsB))
print(unique_students)

# Task 5
numbersA = (23, 52, 12, 75, 42)
numbersB = (75, 22, 42, 94, 70)
common_elements = set(numbersA).intersection(set(numbersB))
print(common_elements)

# Task 6
a = (1, 2, 3, 4, 6, 7, 8)
# print(a[1:3] + (5))

tup1 = list(a)
tup1.insert(4, 5)
a=tuple(tup1)
print(tup1)



# tup1 = (1, 2, 3, 4, 5, 6)
# print(tup1[2:5] +(1, 23, 43))