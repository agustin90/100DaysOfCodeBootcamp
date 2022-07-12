# 4_1 Heads or Tails

# Instructions
# You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
# Important, the first letter should be capitalised and spelt exactly like in the example e.g. Heads, not heads.
# There are many ways of doing this. But to practice what we learnt in the last lesson, you should generate
#  a random number, either 0 or 1. Then use that number to print out Heads or Tails.

# e.g. 1 means Heads 0 means Tails
# Example Output
# Heads
# or
# Tails

# import random

# random_integer = random.randint(0,1)

# if random_integer == 1:
#     print("Heads")
# else:
#     print("Tails")


# 4_2 Who's Paying

# Instructions
# You are going to write a program which will select a random name from a list of names.
# The person selected will have to pay for everybody's food bill.
# Important: You are not allowed to use the choice() function.
# Line 8 splits the string names_string into individual names and puts them inside a List called names. For this to work, you must enter all the names as name followed by comma then space. e.g. name, name, name

# Example Input
# Angela, Ben, Jenny, Michael, Chloe
# Note: notice that there is a space between the comma and the next name.

# Example Output
# Michael is going to buy the meal today!

# Hint
# 1. You might need the help of the len() function.
# https://stackoverflow.com/questions/1712227/how-do-i-get-the-number-of-elements-in-a-list
# 2. Remember that Lists start at index 0!

# import random

# # Split string method
# names_string = input("Give me everybody's names, separated by a comma. ")
# names = names_string.split(", ")
# print(names)
# random_int = random.randint(0, len(names)-1)
# print(f"{names[random_int]} is going to buy the meal today!")
#print(f"{random.choice(names)} is going to buy the meal today!")


# 4_3 Treasure Map

# Instructions
# You are going to write a program which will mark a spot with an X.
# In the starting code, you will find a variable called map.
# This map contains a nested list. When map is printed this is what the nested list looks like:
# ['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️'],['⬜️', '⬜️', '⬜️']

# In the starting code, we have used new lines (\n) to format the three rows into a square, like this:
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# This is to try and simulate the coordinates on a real map.

# Your job is to write a program that allows you to mark a square on the map using a two-digit system.
# The first digit is the vertical column number and the second digit is the horizontal row number. e.g.:
# https://cdn.fs.teachablecdn.com/2vnboIYTFFruvl9FJ2w5

# First your program must take the user input and convert it to a usable format.
# Next, you need to use it to update your nested list with an "x".

# Example Input 1
# column 2, row 3 would be entered as:
# 23

# Example Output 1
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', 'X', '⬜️']

# Example Input 2
# column 3, row 1 would be entered as:
# 31

# Example Output 2
# ['⬜️', '⬜️', 'X']
# ['⬜️', '⬜️', '⬜️']
# ['⬜️', '⬜️', '⬜️']

# Hint
# 1. Remember that Lists start at index 0!
# 2. map is just a variable that contains a nested list. It's not related to the map function in Python.

# row1 = ["⬜️","⬜️","⬜️"]
# row2 = ["⬜️","⬜️","⬜️"]
# row3 = ["⬜️","⬜️","⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# map[int(position[1])-1][int(position[0])-1] = 'X'
# print(f"{row1}\n{row2}\n{row3}")


# Rock Paper Scissors

# Instructions
# Make a rock, paper, scissors game.
# Inside the main.py file, you'll find the ASCII art for the hand signals already saved to a corresponding
#  variable: rock, paper, and scissors. This will make it easy to print them out to the console.
# Start the game by asking the player:
# "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."
# From there you will need to figure out:
#     How you will store the user's input.
#     How you will generate a random choice for the computer.
#     How you will compare the user's and the computer's choice to determine the winner (or a draw).
#     And also how you will give feedback to the player.
# You can find the "official" rules of the game on the World Rock Paper Scissors Association website.

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_images = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)


while choice>= 3 or choice<0:
    print("You typed an invalid number, you lose!")
    choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

print(game_images[choice])

print("Computer chose:")
print(game_images[computer_choice])

# if (choice >= 3 or choice<0):
#     print("You typed an invalid number, you lose!")
# elif choice == computer_choice:
#     print("Draw.")
# elif choice == 0 and computer_choice == 1:
#     print("You lose.")
# elif choice == 0 and computer_choice == 2:
#     print("You win.")
# elif choice == 1 and computer_choice == 0:
#     print("You win.")
# elif choice == 1 and computer_choice == 2:
#     print("You lose.")
# elif choice == 2 and computer_choice == 1:
#     print("You win.")
# elif choice == 2 and computer_choice == 0:
#     print("You lose.")

if (choice >= 3 or choice<0):
    print("You typed an invalid number, you lose!")
elif choice == computer_choice:
    print("Draw.")
elif choice == 0 and computer_choice == 2:
    print("You win.")
elif choice == 2 and computer_choice == 0:
    print("You lose.")
elif (choice > computer_choice):
    print("You win.")
elif (choice < computer_choice):
    print("You lose.")

