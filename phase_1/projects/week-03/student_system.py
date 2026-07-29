student_name = input("Enter name: ")
score = int(input("Enter score: "))

line = 40 * "="

print(line)
print("      Result")
print(line)
print(f"Student: {student_name}")
print(f"Score: {score}")
if score >= 70:
   print("Grade: Excellent")  
elif score >= 50:
    print("Grade: Pass")
else:
    print("Grade: Fail")

