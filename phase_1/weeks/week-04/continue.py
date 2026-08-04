# exercise 1
count = 1

while count <= 5:
    if count == 3:
        count += 1
        continue
    print(count)
    count += 1

# Exercise 2
num = 1

while num <= 10:
    if num % 2 == 0:
        num += 1
        continue
    print(num)
    num += 1

# Exercise 3
logged_in = False

while  not logged_in:
    name = input("Enter name: ").strip()
    if name == "":
        print("Name cannot be empty")
        continue
    print(f"Welcome, {name}")
    logged_in = True

# Exercise 4
logged_in = True

while logged_in:
    command = input("Enter command: ").strip().lower()
    if command == "help":
        print("Availiable commands:")
        print("Profile")
        print("Calculator")
        print("exit")
        continue
    if command == "exit":
        logged_in = False
        print("Shutting down AIOS...")
    else:
        print("Unknown Command")

# Exercise 5
number = -3 

while number <= 3:
    if number < 0:
        number += 1
        continue
    print(number)
    number += 1

# Exercise 6
module = 1

while module <= 6:
    if module == 4:
        print("Module 4 unavailable.")
        module += 1
        continue
    print(f"Scanning Module {module}")
    module += 1