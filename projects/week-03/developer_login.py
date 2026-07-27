username = input("Enter your Github username: ").lower()
age = int(input("Enter age: "))

if username == "snrboi" and age >= 18:
    print("Developer access granted")
else: 
    print("Developer access denied")