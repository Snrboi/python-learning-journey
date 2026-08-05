# Exercise 1
classroom = 1 

while classroom <= 2:
    print(f"Classroom {classroom}")
    student = 1
    while student <= 3:
        print(f"Student {student}")
        student += 1
    classroom += 1

# Exercise 2
floor = 1

while floor <= 3:
    print(f"Floor {floor}")
    room = 1 
    while room <= 2:
        print(f"Room {room}")
        room += 1
    floor += 1

# Exercise 3
project = 1 

while project <= 2:
    print(f"Scanning Project {project}")
    file = 1
    while file <= 4:
        print(f"File: {file}")
        file += 1
    project += 1

# Exercise 4
team = 1

while team <= 2:
    print(f"Team {team}")
    player = 1
    while player <= 3:
        print(f"Player {player}")
        player += 1
    team += 1

# Exercise 5
department = 1

while department <= 2:
    print(f"Department {department}")
    employee = 1
    while employee <= 3:
        if employee == 2:
            employee += 1
            continue
        print(f"Employee {employee}")
        employee += 1
    department += 1