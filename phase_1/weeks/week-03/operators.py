# Exercise 1
age = 20
club = "chelsea"

if age >= 18 and club == "chelsea":
    print("Access Granted") # Age is greater than 18 and is equal to chelsea

# Exercise 2
age = 16
club = "chelsea"

if age >= 18 and club == "chelsea":
    print("Access Granted")
else:
    print("Access Denied") # this runs because 16 isn't greater than or equal to 18

# Exercise 3
score = 45
bonus = True

if score >= 50 or bonus:
    print("Passed") # bonus is true so it would print passed

# exercise 4
age = int(input("Enter Age: "))
club = input("Enter Fav Club: ").lower()

if age >= 18 and club == "chelsea":
    print("Access Granted")
else:
    print("dont meet the requirements")

# Exercise 5
user = input("Are you a student? (yes/no) ").lower()
age = int(input("Enter age: "))

if user == "yes" or age <= 12: 
    print("Discount Applied")
else:
    print("No discount")

# Exercise 6
logged_in = False
print(not logged_in)
logged_in = True # if i run this now with the line above it will print false because the logged in is now true and not is the opposite of the boolean