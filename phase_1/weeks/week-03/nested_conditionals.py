# Exercise 1
age = 22
club = "chelsea"

if age >= 18:
    if club == "chelsea":
        print("Adult football fan")
else:
        print("minor")

# Exercise 2
logged_in = True
github = "snrboi"

if logged_in:
     if github == "snrboi":
          print("Welcome back Developer!")
     else:
          print("Unkown Github User")
else:
     print("Please log in")


# exercise 3
python_sprint = int(input("How many sprints have you completed? "))
if python_sprint >= 3 :
     aios = input("Have you built Aios today? (yes/no) ").lower().strip()
     if aios == "yes":
          print("Excellent Consistency") 
     else:
          print("Remember to improve Aios today")
else:
     print("Keep Learning the Fundamentals")

# Exercise 4
user_name = input("Enter Name: ")
age = int(input("Enter Age: "))
if age >= 18:
     student_id = input("Do you have a student ID? (yes/no) ").lower()
     if student_id == "yes":
          print(f"Access Granted, Welcome! {user_name.title()}")
     else:
          print("Student ID required")
else:
     print("Access Denied")

# Exercise 5
logged_in = True
role = "engineer"

if logged_in:
    if role == "admin":
        print("Welcome to Admin Panel")
    elif role == "engineer":
        print("Welcome to AI Engineering Workspace")
    else:
        print("Welcome to the Community")
else:
    print("Please log in")

# Exercise 6
fav_club = input("Please enter your favourite football club: ").lower()
age = int(input("Enter Age: "))

if fav_club == "chelsea":
    if age >= 18:
        print("Premium Chelsea Member")
    else: 
        print("Junior Chelsea Member")
else:
    print(f"Hmmm.... {fav_club.title()} fan")