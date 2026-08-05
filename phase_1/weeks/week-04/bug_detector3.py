team = 1

while team <= 2:
    print(f"Team {team}")
    player = 1 # This line needs to be here because when the outer loop goes for its second iteration this can reset so the inner loop condition would be true and it can run.
    while player <= 2:
        print(f"Player {player}")
        player += 1

    team += 1
