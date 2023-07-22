# Oops Concept
# Class, Subclass, method, object

class Student:
    year = 2020

    # self excecuting constructor
    def __init__(self, name, age, place):
        self.name = name
        self.age = age
        self.place = place
    
    def add_age(self):
        self.age += 1

    def relocate(self, place):
        self.place = place

    def display(self):
        print("Current year: "+str(Student.year))
        print("Name: "+self.name)
        print("Age: "+str(self.age))
        print("Place: "+self.place)
        print("-------------------")
    
    # to pass class variable into a function
    @classmethod
    def add_year(cls):
        cls.year += 1

    # Making of static class method
    @staticmethod
    def welcome():
        print("Student Details")

# Object instantiation
student_1 = Student("Harry", 10, "US")
student_2 = Student("John", 8, "UK")

Student.welcome()

student_1.display()
student_2.display()

student_1.add_age()
student_2.add_age()

student_1.relocate("Hyderabad")
student_2.relocate("Bangalore")

student_1.display()
student_2.display()