import csv

def add_request():
    try:
        prompt = input("Prompt: ").strip()
        model = input("Model: ").strip()
        tokens = int(input("Tokens: "))
        successful = input("Successful ? (yes/no): ").strip().lower()
    except ValueError:
        print("Tokens must be a number")
    else:
        if successful == "yes":
            successful = True
        elif successful == "no":
            successful = False
        else:
            print("Successful must be yes or no")
            return

        request = {
            "prompt": prompt,
            "model": model,
            "tokens": tokens,
            "successful": successful
        }

        fieldnames = ["prompt", "model", "tokens", "successful"]

        with open("models.csv", "a+", encoding="utf-8", newline="") as file:
            file.seek(0)
            has_content = bool(file.read(1))
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            if not has_content:
                writer.writeheader()

            file.seek(0, 2)
            writer.writerow(request)

        print("Request added successfully!")

def show_requests():
    try:
        with open("models.csv", "r", encoding="utf-8", newline="") as file:
            request = csv.DictReader(file)
            for row in request:
                prompt = row["prompt"]
                model = row["model"]
                tokens = int(row["tokens"])
                successful = row["successful"] == "true"
                print(f"Prompt: {prompt}")
                print(f"Model: {model}")
                print(f"Tokens: {tokens}")
                print(f"Success: {successful}")
                print()
    except FileNotFoundError:
        print("File not found")


def request_summary():
    try:
        with open("models.csv", "r", encoding="utf-8", newline="") as file:
            request = csv.DictReader(file)
            list_request = list(request)


        total_request = len(list_request)
        tokens = [int(req["tokens"]) for req in list_request]
        success = [req["successful"] for req in list_request if req["successful"] == "True"]
        unsuccessful = [req["successful"] for req in list_request if req["successful"] == "False"]
    except FileNotFoundError:
        print("File not found")
    else:
        print(f"Total requests: {total_request}")
        print(f"Total Tokens: {sum(tokens)}")
        print(f"Successful requests: {len(success)}")
        print(f"Failed requests: {len(unsuccessful)}")


running = True

while running:
    print("=== AI Request Tracker ===")
    print("1. Add request")
    print("2. Show requests")
    print("3. Request summary")
    print("4. Exit")

    choice = input("Choose an option: ").strip()
    print()
    if choice == "1":
        add_request()
    elif choice == "2":
        show_requests()
    elif choice == "3":
        request_summary()
    elif choice == "4":
        running = False
        print("Registry Closed")
    else:
        print("Invalid option selected! Try again.")

