def add_bonus(score):
    return score + 5

scores = [50, 65, 80, 90, 75]

result = list(map(add_bonus, scores))
print(result)