
class Vehicles:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")


class Car(Vehicles):
    def  __init__(self, brand, model, year, no_of_doors):
        super().__init__(brand, model, year)
        self.no_of_doors = no_of_doors

    def start(self):
        print("Car is starting")

    def stop(self):
       print("Car is stopping")

class Bike(Vehicles):
    def __init__(self, brand, model, year, no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_wheels

    def start(self):
       print("Bike is starting")

    def stop(self):
       print("Bike is stopping")

class Airplane(Vehicles):
    def __init__(self, brand, model, year, no_of_doors):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_doors

    def start(self):
       print("Airplane is starting")

    def stop(self):
       print("Airplane is stopping")

vehicles:  list[Vehicles] = [
    Car("Ford", "GT", 2008, 5),
    Bike("Honda", "Scoopy", 2009, 2),
    Airplane("Boeing", "787", 2011, 16)
]
for vehicle in vehicles:
    print(f"Inspecting {vehicle.brand} {vehicle.model} {type(vehicle).__name__}")
    vehicle.start()
    vehicle.stop()









