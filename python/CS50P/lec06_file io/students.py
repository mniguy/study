# 01
with open("students.csv") as file:
    for line in file:
        # 01
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

        # 02
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")

# 02 - 1
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        students.append(f"{name} is in {house}")

for student in sorted(students):
    print(student)

# 02 - 2
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

# sorted(students) => it's not possible because it's a dictionary
for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")

# 02 - 3
students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        student = {"name": name, "house": house}
        students.append(student)

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")

# 03 - 1 in case of house -> location of their home
import csv

students = []

with open("students.csv") as file:
    reader = csv.reader(file)
    # 01
    for row in reader:
        students.append({"name": row[0], "home": row[1]})
    # 02
    for name, home in reader:
        students.append({"name": name, "home": home})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")

# 03 - 2
import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")


# 04
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    # 01
    writer = csv.writer(file)
    writer.writerow([name, home])
    # 02
    writer.csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})