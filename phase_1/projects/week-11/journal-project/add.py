def add_entry():
    topic = input("What did you learn today? ").strip()

    with open("learning_journal.txt", "a", encoding="utf-8") as file:
        file.write(topic + "\n")

    print("Entry saved successfully")