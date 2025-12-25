

class Student:

    #default constructor
    def __init__(self):
        pass

    college_name = "IIT Kaanpur"    #class attribute
    name= "anonymous"
    #parameterized constructor
    def __init__(self, name, marks):
        self.name = name            #object attr > class attr
        self.marks = marks

    def welcome(self):
        print("welcome student", self.name)

    def get_marks(self):
        return self.marks


s1 = Student("Karan", 97)
print(s1.name, s1.marks)
s2 = Student("Arjun", 88)
print(s2.name, s2.marks)
print (s2.college_name)
s1.welcome()
print(s2.get_marks())