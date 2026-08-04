count = 1

while count <= 5:
    if count == 3:
        count += 1 # this line was missing in the conditional which makes it an infinite loop because if count == 3, there isnt any count that would update it to 4 as continue sends the loop back to the top so with the code like this, count would forever remain = 3 and is an infinite loop.
        continue

    print(count)
    count += 1