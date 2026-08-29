def calculate_average(scores):
    total = 0

    for score in scores:
        total += score

    average = total / len(scores)

    return average # No return statement

result = calculate_average([80, 90, 100])

print(result + 10)