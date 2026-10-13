PASS_MARK = 50
NUM_COURSES = 5

name = input("Enter student name: ")

total = 0
highest = 0
lowest = 100
passed = 0

for course_number in range(1, NUM_COURSES + 1):
    mark = float(input("Enter marks for course " + str(course_number) + " (0-100): "))
    while mark < 0 or mark > 100:
        print("Marks must be between 0 and 100.")
        mark = float(input("Enter marks for course " + str(course_number) + " (0-100): "))

    total += mark
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    if mark >= PASS_MARK:
        passed += 1

average = total / NUM_COURSES

if average >= 80:
    performance = "Excellent"
elif average >= 70:
    performance = "Good"
elif average >= 60:
    performance = "Satisfactory"
elif average >= 50:
    performance = "Pass"
else:
    performance = "Needs Improvement"

print()
print("Student:", name)
print("Total:", round(total, 2))
print("Average:", round(average, 2))
print("Highest:", highest)
print("Lowest:", lowest)
print("Courses passed:", passed, "of", NUM_COURSES)
print("Performance:", performance)
