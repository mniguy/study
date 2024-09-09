from typing import Self

class Car:
    total_cars: int = 0

    def __init__(self, brand: str, top_speed: int) -> None:
        self.brand = brand
        self.top_speed = top_speed
        Car.total_cars += 1

    @classmethod
    def auto_top_spped(cls, brand: str) -> Self:
        database: dict[str, int] = {"bmw": 250, "volvo": 270}
        top_speed: int | None = database.get(brand.lower())

        if top_speed:
            print(f"Setting top speed to: {top_speed}.")
        else:
            print(f"Could not find: '{brand}' in our database. Using default speed.")
            top_speed = 200
        
        return cls(brand=brand, top_speed=top_speed)
    
    @classmethod
    def total_cars_created(cls) -> int:
        return cls.total_cars

    def __str__(self) -> str:
        return f"{self.brand} ({self.top_speed}km/h)"


'''
#bmw.total_cars = 100 -> Car.total_cars 는 바뀌지 않고 bmw거만 바뀜
bmw: Car = Car(brand="BMW", top_speed=250)
Car.total_cars = 100
print(Car.total_cars)

volvo: Car = Car(brand="Volvo", top_speed=270)
print(Car.total_cars)
'''

bmw: Car = Car.auto_top_spped("BMW")
print(bmw)
print(Car.total_cars_created())

volvo: Car = Car.auto_top_spped("Volvo")
print(volvo)
print(Car.total_cars_created())

mercedes: Car = Car.auto_top_spped("Mercedes")
print(mercedes)
print(Car.total_cars_created())