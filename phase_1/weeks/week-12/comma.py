import csv


with open("/home/dell/python-learning-journey/phase_1/weeks/week-12/practice.csv", "r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row["name"])
        print(row["tokens"])