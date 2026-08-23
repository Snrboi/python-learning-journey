# Ai thinking 
# goal: return the average of scores
# input: list
# output: average
# steps: get the total of numbers in the list and divide it by the length of the list.
# Python concepts: on looking at this initially i thoght sum() and len() but after the instuctions i thought loop, len() so i did both just to know if they would work.
scores = [80, 90, 70, 60, 100]

# solution 1
def calculate_average(scores):
    result = sum(scores) / len(scores)
    return result
a = calculate_average(scores)
print(a)

# solution 2
def calculate_average(scores):
    total = 0
    for score in scores:
        total += score
    result = total/ len(scores) 
    return result
a = calculate_average(scores)
print(a)   