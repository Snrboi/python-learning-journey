numbers = [1, 2, 3, 4]

def double(x):
    return x * 2

result = list(map(double, numbers))

print(result) # there wasnt a return statement so the function sent none so it doesnt run the exact function logic. it only runs None
