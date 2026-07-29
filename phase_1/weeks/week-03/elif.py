# Exercise 1
score = 49

if score >= 70:
    print("excellent")
elif score >= 50:
    print("pass")
else:
    print("fail")

# Exercise 2
age = 13
if age >= 18:
    print("adult")
elif age >= 13:
    print("teenager")
else:
    print("child")

# Exercise 3
score = int(input("Enter Score: "))

if score >= 70:
    print("Distinction")
elif score >= 60:
    print("credit")
elif score >= 50:
    print("pass")
else:
    print("fail")

# Exercise 4
temperature = 32

if temperature >= 30:
    print("hot")
elif temperature >= 20:
    print("warm")
else:
    print("cold")

# Exercise 5
fav_club = input("Please enter your favourite club: ").lower()

if fav_club == "chelsea":
    print("London Blue Member")
elif fav_club == "barcelona":
    print("Catalonia Member")
elif fav_club == "real madrid":
    print("Madrid member")
else:
    print("General football member")


python_learner = int(input("Please input learning level: "))

if python_learner > 10:
    print("AI Engineer in Training")
elif python_learner >= 6:
    print("Python Builder")
elif python_learner >= 3:
    print("Python Explorer")
else:
    print("Python Beginner")