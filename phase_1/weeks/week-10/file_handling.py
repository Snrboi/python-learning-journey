# exercise 1
scores = []
try:
    with open("/home/dell/python-learning-journey/phase_1/weeks/week-10/scores.txt", "r") as file:
        newfile = file.readlines()
        for line in newfile:
            score = int(line.strip())
            scores.append(score)
    print(scores)
    highest = max(scores)
    print(highest)
    average = sum(scores) / len(scores)
    print(average)
except FileNotFoundError:
    print("File not Found")
except ValueError:
    print("Invalid Score")
except Exception as e:
    print(e)