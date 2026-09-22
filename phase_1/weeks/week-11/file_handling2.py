try: 
    with open("learning_log.txt", "a", encoding= "utf-8") as file:
        file.write("Functions" + "\n")
        file.write("Modules" + "\n")
        file.write("Error Handling\n")
        file.write("File Handling \n")

    with open("learning_log.txt", "r") as file:
        topics = file.readlines()
except FileNotFoundError:
    print("File not found!")
else:
    print("---Learning Log---")
    for line in topics:
        topic = line.strip()
        print(topic)