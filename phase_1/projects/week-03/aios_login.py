line = "=" * 30
username = input("Enter Github Username: ").lower()
password = input("Enter password: ")

if username == "snrboi":
    if password == "python123":
        print(line)
        print("     AIOS Login Successful")
        print(line)
        print("Welcome back, Lead AI Engineer!")
    else:
        print("Incorrect Password")
else:
    print("Unknown Username")

    