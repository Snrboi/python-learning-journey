age = int(input("Age: ")) # int() not used 

if age >= 18: # no colon
    print("Adult")

elif age >= 13:
 print("Teenager") # indentation error

elif age >= 0:
    print("Child")

else: # no colon
    print("Invalid")