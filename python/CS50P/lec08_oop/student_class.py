# class int(x, base=10)
# class str(object='')
# str.lower()
# str.strip([chars])
# class list([iterable])
# list.append(x)
class Student:
    # class supoorts attributes -> instance variables ex) name, house
    # methods
    def __init__(self, name=str, house=str, patronus=str) -> None:
        # initialize the content within a class
        # instance variables to objects
        if not name:
            # raise -> handle error
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name = name
        self.house = house
        self.patronus = patronus
    
    def __str__(self) -> str:
        return f"{self.name} from {self.house}"
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name
    
    # Getter -> gets some attributes
    @property
    def house(self) -> None:
        return self._house
    
    # Setter -> sets some attributes
    @house.setter
    def house(self, house) -> None:
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        # instance and the function's names collide
        # instance variable is _house but the attribute is still house
        self._house = house

    def charm(self):
        match self.patronus:
            case "Stag":
                return "🐴"
            case "Otter":
                return "🦦"
            case "Jack Russell terrier":
                return "🐶"
            case _:
                return "🪄"

def main():
    student = get_student()
    student._house = "Number Four, Privet Drive"
    print(student)

    print("Expecto Patronum!")
    print(student.charm())

def get_student():
    # 01
    student = Student()
    student.name = input("Name: ")
    student.house = input("House: ")
    student.patronus = input("Patronus: ")
    return student
    #02
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    # this will instantiate student oobject for me
    # return Student(name, house) -> it's okay too
    student = Student(name, hous, patronus)
    return student

if __name__ == "__main__":
    main()