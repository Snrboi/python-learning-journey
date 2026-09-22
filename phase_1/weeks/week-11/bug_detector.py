try:
    with open("ai_models.txt", "a", encoding="utf-8") as file: # "w" overwrites what was previously there but "a" adds to the exisiting entries
        file.write("Llama")

    with open("ai_models.txt", "r", encoding="utf-8") as file:
        models = file.readlines()

        for model in models: # this isnt really an error but an else statement would be ideal to put this in as a try block should only contain inputs that can fail
            print(model)
except FileNotFoundError: # this should not be value error as that is the wrong error category
    print("File could not be found.")