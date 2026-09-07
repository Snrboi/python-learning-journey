scores = [40, 60, 75, 90]

def passed(score):
    return score >= 50

result = list(filter(passed, scores))

print(result)