students = [
    {"name": "Rahim", "department": "CSE", "marks": 78, "attendance": 85},
    {"name": "Karim", "department": "EEE", "marks": 64, "attendance": 72},
    {"name": "Nusrat", "department": "Data Science", "marks": 91, "attendance": 95},
    {"name": "Tania", "department": "BBA", "marks": 55, "attendance": 78},
    {"name": "Sabbir", "department": "CSE", "marks": 83, "attendance": 88},
]


def average_marks(data):
    total = 0
    for s in data:
        total += s["marks"]
    return total / len(data)


def top_student(data):
    best = data[0]
    for s in data:
        if s["marks"] > best["marks"]:
            best = s
    return best


def low_attendance_count(data):
    count = 0
    for s in data:
        if s["attendance"] < 80:
            count += 1
    return count


best = top_student(students)

print("----- SUMMARY -----")
print("Total students          :", len(students))
print("Average marks           :", average_marks(students))
print("Highest marks           :", best["name"], "with", best["marks"])
print("Attendance below 80%    :", low_attendance_count(students), "students")