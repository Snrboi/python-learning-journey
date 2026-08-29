# AI Thinking
# Goal: return the total, average and highest score from a list of scores
# Input: list
# Output: total, average, highest
# Steps: find the total, then use it to calculate the average and find the max number in the list
# Python concepts: functions, sum(), len(), max(), print() and return
scores = [80, 90, 70, 100, 85]

def analyze_scores(scores):
    total = sum(scores)
    average = total / len(scores)
    highest = max(scores) 
    return total, average, highest

total, average, highest = analyze_scores(scores)
print(total)
print(average)
print(highest)