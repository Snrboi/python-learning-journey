# Exercise 1
num = 1

while num >= 1:
    print(num)
    if num == 5:
        break
    num += 1

# Exercise 2
logged_in = False

while not logged_in:
    password = input("Enter password: ")
    if password == "python123":
        print("Access Granted")
        break
    else:
        print("Incorrect Password")

# Exercise 3
module = 1 

while module >= 1:
    print(f"Searching Module {module}")
    if module == 4:
        print("Module found!")
        break
    module += 1

# exercise 4
logged_in = True

while logged_in:
    command = input("Type a command: ")
    if command == "exit":
        print("Shutting down AIOS")
        break
    else:
        print("Unknown Command")

# Exercise 5
logged_in = False
count = 0 
while count < 3:
    pin = input("Enter Pin: ")
    if pin == "4321":
        logged_in = True
        print("Access Granted")
        break
    else:
        print("Incorrect Pin")

    count += 1

if not logged_in:
    print("Account blocked")

# exercise 6
component = 1

while component >= 1:
    print(f"Checking Component {component}...")
    if component == 3:
        print("Critical Error Detected!")
        break
    component += 1
