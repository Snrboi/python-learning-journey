age = int(input("Age: "))
club = input("Club: ").lower()

if age >= 18 or club == "chelsea":
    print("Welcome Adult Chelsea Member") # it doesnt make sense if the operator isn't and
else: #missing colon
    print("Requirements not met")

