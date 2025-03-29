# Task 1
from operator import index

current_year = 2023
year_of_birth = 1988

age = current_year - year_of_birth
print(age)

# Task 2
code_1 = '354'
code_3 = 132

x = 152
y = 132

code_2 = int(((x / y) * 13) ** 0.5)
secret = code_1 + '-' + str(code_2) + '-' + str(code_3)

user_name = 'John'
user_surname = 'Smith'

message = 'Hello ' + user_name + ' ' + user_surname + '. You are ' + str(age) + ' years old. Your secret code is ' + str(secret) + '.'
print(message)