logged_in = False

while not logged_in:
    github = input("Enter Github name: ").strip().lower()
    if github == "":
        print("Username cannot be empty")
        continue
    if github == "snrboi":
        print("Github profile verified")
        logged_in = True
    else:
        print("Unknown Github user")