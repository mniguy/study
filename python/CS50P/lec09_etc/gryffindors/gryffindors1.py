students = ["Hermione", "Harry", "Ron"]

# list comprehension
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]

gryffindors = {student: "Gryffindor" for student in students}

# enumerate(iterable, start=0)
for i, student in enumerate(students):
    print(i+1, student)

print(gryffindors)