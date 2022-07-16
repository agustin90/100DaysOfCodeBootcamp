# 5_1 Average Height

# Instructions
# You are going to write a program that calculates the average student height from a List of heights.
# e.g. student_heights = [180, 124, 165, 173, 189, 169, 146]
# The average height can be calculated by adding all the heights together and dividing by the total number of heights.
# e.g.
# 180 + 124 + 165 + 173 + 189 + 169 + 146 = 1146
# There are a total of 7 heights in student_heights
# 1146 ÷ 7 = 163.71428571428572
# Average height rounded to the nearest whole number = 164
# Important You should not use the sum() or len() functions in your answer. You should try to replicate their functionality using what you have learnt about for loops.

# Example Input
# 156 178 165 171 187
# In this case, student_heights would be a list that looks like: [156, 178, 165, 171, 187]

# Example Output
# 171

# Hint
# 1. Remember to use the round() function to round the average height before you print it.

# sum_heights = 0
# total_students = 0

# student_heights = input("Input a list of student heights ").split()
# for n in range(0, len(student_heights)):
#   student_heights[n] = int(student_heights[n])

# for height in student_heights:
#     sum_heights += height
#     total_students += 1

# average_height = sum_heights/total_students

# print (f"{round(average_height)}")


# 5_2 Highest Score

# Instructions
# You are going to write a program that calculates the highest score from a List of scores.
# e.g. student_scores = [78, 65, 89, 86, 55, 91, 64, 89]
# Important you are not allowed to use the max or min functions. The output words must match the example.
# i.e 
# The highest score in the class is: x

# Example Input
# 78 65 89 86 55 91 64 89
# In this case, student_scores would be a list that looks like: [78, 65, 89, 86, 55, 91, 64, 89]
# Example Output
# The highest score in the class is: 91

# Hint
# 1. Think about the logic before writing code. How can you compare numbers against each other to see which one is larger?

# max_score = 0

# student_scores = input("Input a list of student scores ").split()
# for n in range(0, len(student_scores)):
#   student_scores[n] = int(student_scores[n])
# print(student_scores)

# for score in student_scores:
#     if (score>max_score):
#         max_score = score

# print(f"The highest score in the class is: {max_score}")


# 5_3 Adding Evens

# Instructions
# You are going to write a program that calculates the sum of all the even numbers from 1 to 100. 
# Thus, the first even number would be 2 and the last one is 100:
# i.e. 2 + 4 + 6 + 8 +10 ... + 98 + 100
# Important, there should only be 1 print statement in your console output. 
# It should just print the final total and not every step of the calculation.

# Hint
# 1. There are quite a few ways of solving this problem, but you will need to use the range() function in any of the solutions.
# sum_evens = 0

# for even in range(1,101):
#     if (even%2 == 0):
#         sum_evens += even

# for even in range(2,101,2):
#     sum_evens += even


# print(f"{sum_evens}")


# 5_4 FizzBuzz

# Instructions
# You are going to write a program that automatically prints the solution to the FizzBuzz game.
#     Your program should print each number from 1 to 100 in turn.
#     When the number is divisible by 3 then instead of printing the number it should print "Fizz".
#     `When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
#     `And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"`

# e.g. it might start off like this:
# `1
# 2
# Fizz
# 4
# Buzz
# Fizz
# 7
# 8
# Fizz
# Buzz
# 11
# Fizz
# 13
# 14
# FizzBuzz`

# .... etc.

# Hint
# 1. Remember your answer should start from 1 and go up to and including 100.
# 2. Each number/text should be printed on a separate line.

# for number in range(1,101):
#     if number%3 == 0 and number%5 == 0:
#         print("FizzBuzz")
#     elif number%3 == 0:
#         print("Fizz")
#     elif number%5 == 0:
#         print("Buzz")
#     else:
#         print(number)


# 5_4 PyPassword Generator Proyect

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
password = ''
password_hard = []

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

for nletters in range(0, nr_letters):
    random_integer_l = random.randint(0,len(letters)-1)
    password += letters[random_integer_l]

for nsymbols in range(0, nr_symbols):
    random_integer_s = random.randint(0,len(symbols)-1)
    password += symbols[random_integer_s]

for nnumbers in range(0, nr_numbers):
    random_integer_n = random.randint(0,len(numbers)-1)
    password += numbers[random_integer_n]

print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for char in password:
    password_hard.append(char)
print(password_hard)
random.shuffle(password_hard)
print(password_hard)
print((''.join(password_hard)))

# new_password = random.sample(password,len(password)) 
# print((''.join(new_password)))