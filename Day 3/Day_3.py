# 3_1 Odd or Even

# Instructions
# Write a program that works out whether if a given number is an odd or even number.
# Even numbers can be divided by 2 with no remainder.
# e.g. 86 is even because 86 ÷ 2 = 43
# 43 does not have any decimal places. Therefore the division is clean.
# e.g. 59 is odd because 59 ÷ 2 = 29.5
# 29.5 is not a whole number, it has decimal places. Therefore there is a remainder of 0.5, so the division is not clean.
# The modulo is written as a percentage sign (%) in Python. It gives you the remainder after a division.
# e.g.
# 6 ÷ 2 = 3 with no remainder.
# 6 % 2 = 0
# 5 ÷ 2 = 2 x 2 + 1, remainder is 1.
# 5 % 2 = 1
# 14 ÷ 4 = 3 x 4 + 2, remainder is 2.
# 14 % 4 = 2

# Example Input 1
# 43
# Example Output 1
# This is an odd number.
# Example Input 2
# 94
# Example Output 2
# This is an even number.

# number = int(input("Which number do you want to check?"))

# if (number%2 == 0):
#     print("This is an odd number")
# else:
#     print("This is an even number")


# 3_2 BMI Calculator 2.0

# Instructions
# Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
# It should tell them the interpretation of their BMI based on the BMI value.
#     Under 18.5 they are underweight
#     Over 18.5 but below 25 they have a normal weight
#     Over 25 but below 30 they are slightly overweight
#     Over 30 but below 35 they are obese
#     Above 35 they are clinically obese.
# https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

# The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):
# https://cdn.fs.teachablecdn.com/jKHjnLrNQjqzdz3MTMyv
# Warning you should round the result to the nearest whole number. The interpretation message needs to include the words in bold from the interpretations above. e.g. underweight, normal weight, overweight, obese, clinically obese.

# Example Input
# weight = 85
# height = 1.75

# Example Output
# 85 ÷ (1.75 x 1.75) = 27.755102040816325
# Your BMI is 28, you are slightly overweight.

# height = input("Enter your height in meters: \n")
# weight = input("Enter your weight in kilograms: \n")

# bmi = round(float(weight) / (float(height))**2)

# if (bmi>=35):
#     print(f"Your BMI is {bmi}, you are clinically obese.")
# elif (bmi<35 and bmi>=30):
#     print(f"Your BMI is {bmi}, you are obese.")
# elif(bmi<30 and bmi>=25):
#     print(f"Your BMI is {bmi}, you are slightly overweight.")
# elif(bmi<25 and bmi>=18.5):
#     print(f"Your BMI is {bmi}, you have a normal weight.")
# else:
#     print(f"Your BMI is {bmi}, you are underweight.")


# 3_3 Leap Year

# 💪This is a Difficult Challenge 💪
# Instructions
# Write a program that works out whether if a given year is a leap year. A normal year has 365 days, 
# leap years have 366, with an extra day in February. 
# The reason why we have leap years is really fascinating, this video does it more justice:
# https://www.youtube.com/watch?v=xX96xng7sAE

# This is how you work out whether if a particular year is a leap year.
#     on every year that is evenly divisible by 4 **except** every year that is 
# evenly divisible by 100 **unless** the year is also evenly divisible by 400

# e.g. The year 2000:
# 2000 ÷ 4 = 500 (Leap)
# 2000 ÷ 100 = 20 (Not Leap)
# 2000 ÷ 400 = 5 (Leap!)
# So the year 2000 is a leap year.
# But the year 2100 is not a leap year because:
# 2100 ÷ 4 = 525 (Leap)
# 2100 ÷ 100 = 21 (Not Leap)
# 2100 ÷ 400 = 5.25 (Not Leap)

# year = int(input("Which year do you want to check?"))

# if (year%4 == 0):
#     if (year%400 ==0):
#         print("Leap year.")
#     else:
#         print("Not Leap year.")
# else:
#     print("Not Leap year")

# # Or
# if (year%4 == 0 and year%400 ==0):
#     print("Leap year.")
# else:
#     print("Not Leap year.")


# 3_4 Pizza Order

# Instructions
# Congratulations, you've got a job at Python Pizza. Your first job is to build an automatic pizza order program.
# Based on a user's order, work out their final bill.
# Small Pizza: $15
# Medium Pizza: $20
# Large Pizza: $25
# Pepperoni for Small Pizza: +$2
# Pepperoni for Medium or Large Pizza: +$3
# Extra cheese for any size pizza: + $1

# Example Input
# size = "L"
# add_pepperoni = "Y"
# extra_cheese = "N"

# Example Output
# Your final bill is: $28.

# print("Welcome to Python Pizza Deliveries!")

# size = input("What size pizza do you want? S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# bill = 0

# if (size == "S"):
#     bill = 15
#     if (add_pepperoni == "Y"):
#         bill += 2
# elif (size == "M"):
#     bill = 20
#     if (add_pepperoni == "Y"):
#         bill += 3
# else:
#     bill = 25
#     if (add_pepperoni == "Y"):
#         bill += 3

# if (extra_cheese == "Y"):
#     bill += 1

# print(f"Your final bill is: ${bill}.")


# 3_5 Love Calculator

# 💪 This is a Difficult Challenge 💪
# Instructions
# You are going to write a program that tests the compatibility between two people.
# To work out the love score between two people:
#     Take both people's names and check for the number of times the letters in the word TRUE occurs. Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
# For Love Scores less than 10 or greater than 90, the message should be:
# "Your score is **x**, you go together like coke and mentos."
# For Love Scores between 40 and 50, the message should be:
# "Your score is **y**, you are alright together."
# Otherwise, the message will just be their score. e.g.:
# "Your score is **z**."
# e.g.

# name1 = "Angela Yu"
# name2 = "Jack Bauer"
# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times
# Total = 5

# L occurs 1 time
# O occurs 0 times
# V occurs 0 times
# E occurs 2 times
# Total = 3

# Love Score = 53
# Print: "Your score is 53."

# Example Input 1
# name1 = "Kanye West"
# name2 = "Kim Kardashian"
# Example Output 1
# Your score is 42, you are alright together.

# Example Input 2
# name1 = "Brad Pitt"
# name2 = "Jennifer Aniston"
# Example Output 2
# Your score is 73.

# The testing code will check for print output that is formatted like one of the lines below:

# "Your score is 47, you are alright together."
# "Your score is 125, you go together like coke and mentos."
# "Your score is 54."

# Hint
#     The lower() function changes all the letters in a string to lower case.
# https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python
#     The count() function will give you the number of times a letter occurs in a string.
# https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string

# print("Welcome to the Love Calculator!")
# name1 = input("What is your name? \n")
# name2 = input("What is their name? \n")
# total_true = 0
# total_love = 0
# total = ''
# score = 0

# combined_string = name1 + name2
# lower_case_string = combined_string.lower()

# total_true = lower_case_string.count('t') + lower_case_string.count('r') + lower_case_string.count('u') + lower_case_string.count('e')
# total_love = lower_case_string.count('l') + lower_case_string.count('o') + lower_case_string.count('v') + lower_case_string.count('e')

# total = str(total_true) + str(total_love)
# score = int(total)

# if (score<10 or score>90):
#     print(f"Your score is {score}, you go together like coke and mentos.")
# elif (score>=40 and score<=50):
#     print(f"Your score is {score}, you are alright together.")
# else:
#     print(f"Your score is {score}.")


# Treasure Island

# Instructions
# Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements 
# to lay out the logic and the story's path in your program.
# To write your code according to my story, you can use this flow chart from draw.io to help you.

# However, I think the fun part is writing your own story 😊
# 🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

# That said if you'd like to continue with my example, feel free to use the text snippets below...
# Text Snippets from my example

#     'You're at a crossroad. Where do you want to go? Type "left" or "right"'
#     'You've come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.'
#     "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?"
#     "It's a room full of fire. Game Over."
#     "You found the treasure! You Win!"
#     "You enter a room of beasts. Game Over."
#     "You chose a door that doesn't exist. Game Over."
#     "You get attacked by an angry trout. Game Over."
#     "You fell into a hole. Game Over."

# Escaping Characters
# If you want to use multiple sets of quotes inside a single string, you might have to "escape" 
# some of them using the backslash \. You can see this in my first sentence: 'You're at a crossroad...'. More on escaping characters here.
# Extensions
# Have a think about how you might write your program to make a player's answers less case-sensitive. 
# In other words, your code should work regardless of whether your user answers "left" or "Left".
# You can also add your own ASCII art. Just remember to add three single quotes ''' at the start and 
# at the end of your artwork to turn it into a multi-line string.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("You're at a cross road. Where do you want to go? Type \"left\" or \"right\"\n")

if (choice.lower() == "right"):
    print("Fall into a hole. Game Over.")
elif (choice.lower() == "left"):
    choice_2 = input("You came to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n")
    if (choice_2.lower() == "wait"):
        choice_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Wich colour do you choose?")
        if (choice_3.lower() == "yellow"):
            print("You Win!")
        elif (choice_3.lower() == "red"):
            print("Burned by fire. Game Over")
        elif (choice_3.lower() == "blue"):
            print("Eaten by beasts. Game Over")
        else:
            print("Game Over.")
    else:
        print("Attacked by trout. Game Over.")
