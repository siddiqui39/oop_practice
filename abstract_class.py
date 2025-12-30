from abc import ABC, abstractmethod

class Vehicle(ABC):

   @abstractmethod
   def go(self):
       pass

   @abstractmethod
   def stop(self):
       pass

class Car(Vehicle):
    def go(self):
        print("you drive the car")

    def stop(self):
        print("you stop the car")

class Bike(Vehicle):
    def go(self):
        print("you ride the bike")

    def stop(self):
        print("you stop the bike")

class Boat(Vehicle):

    def go(self):
        print("You sail the boat")

    def stop(self):
        print("you stop the boat")

bike = Bike()

boat= Boat()
bike.go()
bike.go()
boat.go()
boat.stop()