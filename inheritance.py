

class Vehicle:

    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

class Car(Vehicle):
    def  __init__(self, brand, model, year, no_of_doors, no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_doors = no_of_doors
        self.no_of_wheels = no_of_wheels

class Bike(Vehicle):
    def __init__(self, brand, model, year, no_of_wheels):
        super().__init__(brand, model, year)
        self.no_of_wheels = no_of_wheels

car = Car("Ford", "Focus", 2008, 5, 4)
bike = Bike("Honda", "Scoopy", 2018, 2)
print(car.__dict__)
print(bike.__dict__)
car.start()
bike.start()




