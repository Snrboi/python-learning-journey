logged_in = False

while not logged_in:
    username = input("Enter Username: ").strip().lower()
    password = input("Enter Password: ")
    if username == "snrboi":
        if password == "python123":
            print("Welcome back Lead AI Engineer!")
            break
        else:
            print("Incorrect Password!")
    else:
        print(f"'{username}' Username is invalid!")