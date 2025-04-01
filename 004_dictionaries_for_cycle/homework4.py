# Create two empty lists (long_names, short_names)
# Iterate through names list and add names that are longer than 5 characters
# to long_names, and others to short names
names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']
long_names = []
short_names = []
for name in names:
    if len(name) > 5:
        long_names.append(name)
    else:
        short_names.append(name)

ln = [name for name in names if len(name) > 5]
print(ln)


# Given a list where each element is a year. Determine whether the given year is a leap year. If the year is a leap year,
# print YES, otherwise print NO. According to the Gregorian calendar, a year is a leap year if its number is a multiple of 4,
# but not a multiple of 100 OR if it is a multiple of 400.
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]
for year in years_list:
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        print(year, 'YES')
    else:
        print(year, 'NO')


# Write a program that prompts the user for a string and checks if the string contains only unique characters.
user_input = input('Enter something: ')
if len(user_input) == len(set(user_input)):
    print('All symbols are unique')
else:
    print('There are duplicates')


# Write a program that checks gender for each person.
# If person is a male, print "This is NAME SURNAME. He is AGE years old"
# If person is a female, print "This is NAME SURNAME. She is AGE years old"
people = [
    ('Jane', 'Smith', 26, 'female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'male'),
]
for person in people:
    if person[3] == 'male':
        print(f'This is {person[0]} {person[1]}. He is {person[2]} years old.')
    else:
        print(f'This is {person[0]} {person[1]}. She is {person[2]} years old.')

for name, surname, age, gender in people:
    if gender == 'male':
        print(f'This is {name} {surname}. He is {age} years old.')
    else:
        print(f'This is {name} {surname}. She is {age} years old.')