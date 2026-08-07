logged_in = True
line = "=" * 30
while logged_in:
    menu = ["profile", "calculator", "settings", "exit"]
    print(line)
    print("        MENU")
    print(line)
    for index, value in enumerate(menu, start=1):
        print(f"{index}: {value.title()}")
    choice = input("Select from the options above: ").strip().lower()
    if choice == "1" or choice == "profile":
        print("Loading profile....")
    elif choice == "2" or choice == "calculator":
        print("Loading Calculator")
    elif choice == "3" or choice == "settings":
        print("Loading Settings")
    elif choice == "4" or choice == "exit":
        logged_in = False
        print("Shutting down AIOS...")
    else:
        print("Unknown Command! Please select options from the menu.")
