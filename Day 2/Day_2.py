# 2_1 Data Types

# Instructions
# Write a program that adds the digits in a 2 digit number. e.g. 
# if the input was 35, then the output should be 3 + 5 = 8

# num = input("Type a two digit number\n")

# sum = int(num[0]) + int(num[1])

# print(sum)


# 2_2 BMI Calculator

# Instructions
# Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.
# The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.
# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# Warning you should convert the result to a whole number.

# Example Input
# weight = 80
# height = 1.75

# Example Output
# 80 ÷ (1.75 x 1.75) = 26.122448979591837
# 26

# height = input("Enter your height in meters: \n")
# weight = input("Enter your weight in kilograms: \n")

# bmi = float(weight) / (float(height))**2

# print (f"Your mbi is {int(bmi)}")


# 2_3 Your Life in Weeks

# Instructions
# I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
# https://waitbutwhy.com/2014/05/life-weeks.html
# Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.
# It will take your current age as the input and output a message with our time left in this format:
#     You have x days, y weeks, and z months left.
# Where x, y and z are replaced with the actual calculated numbers.
# Warning your output should match the Example Output format exactly, even the positions of the commas and full stops.
# Example Input
# 56
# Example Output
# You have 12410 days, 1768 weeks, and 408 months left.

# age = input("What is your current age?\n")

# years_remaining = 90 - int(age)
# days_remaining = years_remaining * 365
# weeks_remaining = years_remaining * 52
# months_remaining = years_remaining * 12

# print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")


# 2_4 Final Proyect: Tip Calculator

# Instructions
# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Example Input
# Welcome to the tip calculator!
# What was the total bill? $124.56
# How much tip would you like to give? 10, 12, or 15? 12
# How many people to split the bill? 7

# Example Output
# Each person should pay: $19.93

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill? $"))
tip_bill = float(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

each_person_pay = (total_bill/people) * (1+(tip_bill/100))

print("Each person should pay: $" + "{0:.2f}".format(each_person_pay)) # This is the best option since if the number only has a decimal, add a 0 to complete the 2 digits.
print(f"Each person should pay: ${round(each_person_pay,2)}")