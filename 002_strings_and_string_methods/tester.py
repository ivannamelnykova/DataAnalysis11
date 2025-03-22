# """
# I am a block comment
# This is my second line
# """
# example = "that's"
# example2 = "My favourite book \"Metro 2033\""
#
# # \" \' \\
#
# print('User\\new')
#
# print('Hello\nWorld')  # \n - new line
#
# new = '''ASdasd
# asd
#                 das
#             das
#         das
# das
# das
# das
# das'''
# print(new)

# print("Hello", 'World', 'planet', sep="***", end="")
# print('Hello planet!')

# name = 'Jack'
# salary = 2000
# popular = True
# text = '{}s salary is {:.2f}.'
# print(text.format(name, salary))
#
# text = 'This {product} costs {price:.2f}$.'
# print(text.format(product='Computer', price=1000.99))
#
# text = f'{name.upper()} salary is {salary:.2f}.'
# print(text)

# Formated string used in Python 2
# x = 12231.3456789
# y = 131.1314
# print('The value of x is %.4f' % x)
# print('The value of y is %.2f' % y)
#
# emp_name = 'John'
# emp_age = 30
# emp_salary = 1500
#
# emp_string = 'Hi, my name is %(name)s! I am %(age)s old. My salary is %(salary).2f' % {'name': emp_name, 'salary': emp_salary, 'age': emp_age}
# print(emp_string)


string_sample1 = 'Hello world world'
                # 012345678....
                    # ...-4-3-2-1
string_sample2 = 'fiRst leTTer is noT cApiTal'
string_sample3 = ' !!   extra whitespaces   **   '
string_sample4 = 'der Fluß'

# print(len(string_sample1))
# x = "that\'s"
# print(len(x))
#
# # [START:END:STEP]
# print(string_sample1[0])
# print(string_sample1[6:13])
# print(string_sample1[-6:-2])
# print(string_sample1[::-1])
#
# w = string_sample1[6:11]
# print(w)

# print(string_sample1.upper())
#
# print(string_sample4.lower())
# print(string_sample4.casefold())
#
# print(string_sample2.capitalize())
# print(string_sample2.title())
#
# print(string_sample3.strip(' *!'))
# print(string_sample3.lstrip(' *!'))
# print(string_sample3.rstrip(' *!'))

print(string_sample1.replace('world', 'planet', 1))
print(string_sample1.replace(' ', ''))

print(string_sample1.count('world', 8, 15))
print(string_sample1.find('world', 7))
print(string_sample1.replace('world', 'planet').replace(' ', '*').upper())
