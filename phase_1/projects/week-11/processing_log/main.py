from processor import add_doc
from processor import view_doc

running = True

while running:
    print("=== AI Document Processor ===")
    print("1. Process document")
    print("2. View processing history")
    print("3. Exit")
    print()

    choice = input("Choose an option: ").strip()
    if choice == "1":
        add_doc()
    elif choice == "2":
        view_doc()
    elif choice == "3":
        running = False
        print("Journal Closed.")
    else:
        print("Invalid option selected! Try again")