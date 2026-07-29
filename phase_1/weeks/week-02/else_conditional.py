# Exercise 1
age = 20

if age >= 20:
    print("adult") # this prints adult because the condition is true
else:
    print("minor") 


age = 12

if age >= 18:
    print("Adult")
else:
    print("Minor") # this print minor because the condition is false


score = 49

if score >= 50:
    print("Pass")
else:
    print("Fail") # this prints failed as the condition is false


user = int(input("Enter age: "))

if user >= 18:
    print("Eligible")
else:
    print("Access Denied")

club = input("What is your favourite club? ").lower()

if club == "chelsea":
    print("Welcome! Blue.")
else:
    print("Maybe next season")

user = int(input("Please input a number: "))

if user >= 0:
    print("positive number or zero")
else:
    print("Negative Number")

