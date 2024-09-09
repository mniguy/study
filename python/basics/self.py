class Car:
    def __init__(self, brand: str, fuel_type: str) -> None:
        self.brand = brand
        self.fuel_type = fuel_type

    # method
    def drive(self, distance: float) -> None:
        print(f"Driving {self.brand} for {distance}km [{self.fuel_type}]")

    @staticmethod
    def test() -> None:
        print("Testing...")

# instance of Car
# self.brand -> volvo.brand로 바뀌는 것임
# you can call it 'this' not 'self'
volvo: Car = Car(brand="Volvo", fuel_type="Diesel")

print(volvo.brand)
print(volvo.fuel_type)
volvo.drive(distance=10)