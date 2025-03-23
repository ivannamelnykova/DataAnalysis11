# Task 1
example_string1 = "Hello bro"
a = example_string1[0:2]
b = example_string1[-2:]
print(a+b)

# Task 2
example_string2 = "jack Is My NAME"
example_string2_res = example_string2[0].upper() + example_string2[1:].lower()
print(example_string2_res)

# Task 3
example_string3 = "%-*Get rid of *junk* please*-L%*"
print(len(example_string3))
print(example_string3[3:14], example_string3[15:19], example_string3[21:27])

# Task 4
example_string4 = "hello my name is jack"
print(len(example_string4))
example_string4_res = (example_string4[0].upper() + example_string4[1:17] + example_string4[17].upper() +
                       example_string4[18:21])
print(example_string4_res)

print(example_string4[:-4].capitalize() + example_string4[-4:].capitalize())


# Task 5
example_string5 = "Welcome to estonia. Estonia is awesome, isn't it? I moved to ESTONIA 5 years ago."
example_string5_ignore_case = example_string5.lower()
word_to_find = 'estonia'
word_length = len(word_to_find)
first_word_idx = example_string5_ignore_case.find(word_to_find)
first_word = example_string5[first_word_idx: first_word_idx + word_length]

second_word_find_start_idx = first_word_idx + word_length + 1
second_word_idx = example_string5_ignore_case.find(word_to_find, second_word_find_start_idx)
second_word = example_string5[second_word_idx: second_word_idx + word_length]

third_word_find_start_idx = second_word_idx + word_length + 1
third_word_idx = example_string5_ignore_case.find(word_to_find, third_word_find_start_idx)
third_word = example_string5[third_word_idx: third_word_idx + word_length]

print(first_word)
print(second_word)
print(third_word)

#Task 6
var1 = "jack"
var2 = "hello"
var3 = "MY NAME IS"
print(f'{var2.capitalize()}, {var3.lower()} {var1.capitalize()}')

