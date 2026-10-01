import json

def add_result(result):
    try:
        with open("results.json", "r", encoding="utf-8") as file:
            results = json.load(file)

    except FileNotFoundError:
        results = []

    except json.JSONDecodeError:
        results = []
        print("invalid JSON format") # this was missing from the code.

    results.append(result)

    with open("results.json", "w", encoding="utf-8") as file: #this should be write not append
        json.dump(results, file, indent=4)


new_result = {
    "prompt": "Explain RAG",
    "success": True,
    "tokens": 320
}

add_result(new_result)