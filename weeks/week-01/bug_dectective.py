"""
Bug Detective Challenge #1

Original bugs:
1. age was stored as a string.
2. Tried to concatenate an integer with a string.
3. Variable name had incorrect capitalization.
4. Inputs were not grouped together logically.
"""

name = input("What is your name? ")

age = int(input("How old are you? "))

club = input("Favourite club: ")

print("================================")
print("          WELCOME")
print("================================")

print("Hello " + name)

print("Next year you will be " + str(age + 1))

print("You support " + club)

print("Goodbye!")