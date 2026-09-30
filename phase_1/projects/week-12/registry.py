import json

def load_models():
    try: 
        with open("/home/dell/python-learning-journey/phase_1/projects/week-12/model.json", "r", encoding="utf-8") as file:
            models = json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Print invalid JSON document")
        return []
    else:
        return models

def add_models():
    try:
        model_name = input("Model name: ").strip()
        provider = input("Provider: ").strip()
        maximum_tokens = int(input("Maximum tokens: "))
    except ValueError:
        print("Tokens must be a number")
    else:
        model = {
            "model name": model_name,
            "provider": provider,
            "maximum tokens": maximum_tokens,
            "active": True
        }
        models = load_models()
        if models:
            models.append(model)
            with open("/home/dell/python-learning-journey/phase_1/projects/week-12/model.json", "w", encoding="utf-8") as file:
                json.dump(models, file, indent=4)
        else:
            models = []
            models.append(model)
            with open("/home/dell/python-learning-journey/phase_1/projects/week-12/model.json", "w", encoding="utf-8") as file:
                json.dump(models, file, indent=4)
        print("Model successfully entered")

def show_models():
    if load_models():
        for model in load_models():
            for key, value in model.items():
                print(f"{key.title()}: {value}")
            print()
    else:
        pass



running = True

while running:
    print("=== AI MODEL REGISTRY ===")
    print("1. Add model")
    print("2. Show models")
    print("3. Exit")

    choice = input("Choose an option: ").strip()
    print()
    if choice == "1":
        add_models()
    elif choice == "2":
        show_models()
    elif choice == "3":
        running = False
        print("Registry Closed")
    else:
        print("Invalid option selected! Try again.")