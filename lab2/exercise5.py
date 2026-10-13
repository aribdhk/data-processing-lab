student = {
    "name": "Arib Ahammed",
    "id": "23-12345-1",
    "department": "Data Science",
    "cgpa": 3.20,
}

for key, value in student.items():
    print(key, ":", value)

if student["cgpa"] >= 2.50:
    print("Good Standing")
else:
    print("Academic Warning")