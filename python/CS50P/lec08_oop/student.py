def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")

# tuple does not support assignment -> immutability of tuple
def get_student():
    #01
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student
    # 02
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()