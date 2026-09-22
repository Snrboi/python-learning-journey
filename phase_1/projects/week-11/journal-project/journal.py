from add import add_entry
from view import view_entry

running = True

while logged_in:
    print("===AI Learning Journal===")
    print("1. Add learning entry")
    print("2. View all entries")
    print("3. Exit")

    choice = input("Choose an option: ").strip()
    if choice == "1":
        add_entry()
    elif choice == "2":
        view_entry()
    elif choice == "3":
        running = False
        print("Journal Closed.")
    else:
        print("Invalid option selected! Try again")