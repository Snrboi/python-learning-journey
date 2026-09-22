def view_entry():
    try:
        with open("learning_journal.txt", "r", encoding="utf-8") as file:
            topics = file.readlines()
    except FileNotFoundError:
        print("No learning entries found")
    else:
        print("===Learning Entries===")
        for number, entry in enumerate(topics, start=1):
            topic = entry.strip()
            print(f"{number}. {topic}")