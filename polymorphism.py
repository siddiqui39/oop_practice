
class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


class Car(Vehicle):
    def  __init__(self, brand, model, year, no_of_doors):
        super().__init__(brand, model, year)
        self.no_of_doors = no_of_doors

    def start(self):
        print("Car is starting")

    def stop(self):
        print("Car is stopping")

class Bike(Vehicle):
    def __init__(self, brand, model, year, no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_wheels

    def start(self):
        print("Bike is starting")

    def stop(self):
        print("Bike is stopping")

vehicles = [
    Car("Ford", "GT", 2008, 5),
    Bike("Honda", "Scoopy", 2009, 2)
]

for vehicle in vehicles:
    if isinstance(vehicle, Car):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()

    elif isinstance(vehicle, Bike):
        print(f"Inspecting {vehicle.brand} {vehicle.model} ({type(vehicle).__name__})")
        vehicle.start()
        vehicle.stop()

    else:
        raise Exception("Object is not a valid vehicle")
