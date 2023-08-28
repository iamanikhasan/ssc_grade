

# student mark
marks = int(input("Enter your marks : "))

# grade and grade point
grade = None
grade_point = None

# calculate grade and grade point using if-else statements
if marks >= 80 and marks <=100:
    grade = "A+"
    grade_point = 5.00
elif marks >= 70 and marks <=79:
    grade = "A"
    grade_point = 4.00
elif marks >= 60 and marks <=69:
    grade = "A-"
    grade_point = 3.50
elif marks >= 50 and marks <=59:
    grade = "B"
    grade_point = 3.00
elif marks >= 40 and marks <=49:
    grade = "C"
    grade_point = 2.00
elif marks >= 33 and marks <=39:
    grade = "D"
    grade_point = 1.00
elif marks >= 0 and marks <= 32:
    grade = "F"
    grade_point = 0.00
else:
    print("Your marks totally garbage!")

# marks percentage
if grade == "A+":
    percentage_range = "80% - 100%"
elif grade == "A":
    percentage_range = "70% - 79%"
elif grade == "A-":
    percentage_range = "60% - 69%"
elif grade == "B":
    percentage_range = "50% - 59%"
elif grade == "C":
    percentage_range = "40% - 49%"
elif grade == "D":
    percentage_range = "33% - 39%"
elif grade == "F":
    percentage_range = "0% - 32%"
else:
    pass

# result
print("Grade: ", grade)
print("Grade Point: ", grade_point)
print("Percentage Range: ", percentage_range)
