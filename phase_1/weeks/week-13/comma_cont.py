import csv

models = [
    {
        "name": "ResearchBot",
        "provider": "Local",
        "tokens": 5000
    },
    {
        "name": "CodeBot",
        "provider": "Cloud",
        "tokens": 8000
    }
]

filename = ["name", "provider", "tokens"]

with open("models.csv", "w", encoding="utf-8", newline="") as file:
    files = csv.DictWriter(file, fieldnames= filename)

    files.writeheader()
    files.writerows(models)