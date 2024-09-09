# inheritance
class Wizard:
    def __init__(self, name=str) -> None:
        if not name:
            raise ValueError("Missing name")
        self.name = name

# nested
class Student(Wizard):
    def __init__(self, name=str, house=str) -> None:
        super().__init__(name)
        self.house = house

# nested 
class Professor(Wizard):
    def __init__(self, name=str, subject=str) -> None:
        super().__init__(name)
        self.subject = subject

wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")