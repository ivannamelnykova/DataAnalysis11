# Task 1
long_names = []
short_names = []

names = ['Sarah', 'Jessica', 'Anthony', 'Jack', 'Simon', 'Arthur', 'Maria', 'Samantha']

for i in range(len(names)):
    word = names[i]
    if len(word) > 5:
        long_names.append(word)
    else:
        short_names.append(word)

print(long_names)
print(short_names)


# Task 2
years_list = [2012, 2011, 1492, 1861, 1600, 1700, 1800, 1900, 2000]

for i in range(len(years_list)):
    if years_list[i] % 100 == 0 and years_list[i] % 400 == 0:
        print(f"{years_list[i]}: YES")
    elif years_list[i] % 100 == 0:
        print(f"{years_list[i]}:NO")
    elif years_list[i] % 4 == 0:
        print(f"{years_list[i]}:YES")
    else:
        print(f"{years_list[i]}:NO")


# Task 3
people = [
    ('Jane', 'Smith', 26, 'female'),
    ('Jack', 'Green', 30, 'male'),
    ('Maria', 'Gold', 29, 'female'),
    ('Simon', 'Bloom', 35, 'male'),
]

for i in range(len(people)):
    person = people[i]
    if person[3] == 'female':
        print(f"This is {person[0]} {person[1]}. She is {person[2]} years old")
    else:
        print(f"This is {person[0]} {person[1]}. He is {person[2]} years old")
