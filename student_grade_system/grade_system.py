# Build A Student Grade System

marks = int(input("Enter Your Marks : "))
grade = ''
if(marks >= 90):
    grade = "A"
elif(marks >= 80):
    grade = "B"
elif(marks >= 60):
    grade = "C"
elif(marks >= 35):
    grade = "D"
else:
    grade = "F"
print("Student Get",marks,"With",grade,"Grade.")