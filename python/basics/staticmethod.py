class Calculator:
    def __init__(self, name: str, version: int) -> None:
        self.name = name
        self.version = version

    def get_calculator_info(self) -> str:
        return f"{self.name} V.{self.version}"
    
    # *args -> *numbers 이름 바꿔도 상관 X
    # in this case the method might be static because you are not actually using self
    # sol 1 : move it outside of class
    # sol 2: add @staticmethod
    '''
    def add_all(self, *numbers: int) -> int:
        return sum(numbers)
    '''
    
    # telling python we know we can use it outside of class but just wants to keep it inside of class
    @staticmethod
    def add_all(*numbers: int) -> int:
        return sum(numbers)
    
calc: Calculator = Calculator(name="BobCalculator", version=1)
print(calc.get_calculator_info())
print(calc.add_all(1, 2, 3, 4))
print(Calculator.add_all(1, 2, 3, 4, 5))



    
