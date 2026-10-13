def calculate_grade(marks):
    average = sum(marks) / len(marks)
    if average >= 80:
        grade = "A"
    elif average >= 70:
        grade = "B"
    elif average >= 60:
        grade = "C"
    elif average >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade


marks = [85, 72, 90, 68, 77]
print("Marks :", marks)
print("Grade :", calculate_grade(marks))