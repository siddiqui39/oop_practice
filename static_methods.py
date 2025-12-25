
class Student:
    def __init__(self, name, marks):
        self.name= name
        self.marks = marks

    @staticmethod
    def hello():
        print("hello")

    def get_avg(self):
        sum =0
        for value in self.marks:
            sum += value
        print("Hi!", self.name, "your avg score is:", sum/3)

s1= Student("Tony", [99,98,56])
s1.get_avg()

s1.name = "Ironman"
s1.get_avg()

s2= Student("Himu", [90,80,67])
s2.get_avg()
s2.hello()