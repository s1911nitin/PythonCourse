"""
Single Inheritance - When one class is derived from another class is known as Inheritance.

Here, Derived class will have both base class property as well as its own.

Real Example - If Father has long nose so his daughter or son may have long nose.
"""


class Employee:
    leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")



class Programmer(Employee):
    def __init__(self, bname, bsalary, brole, blanguage):
        self.name = bname
        self.salary = bsalary
        self.role = brole
        self.language = blanguage

    def printdetails1(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary}, Role-{self.role} and Language-{self.language}")

harry = Employee("Harry",500,"Instructor")
rohan = Employee("Rohan",400,"Junior Engineer")
hamad = Programmer("Hamad",450,"Programmer","Python")

# print(hamad.printdetails())
# print(hamad.printdetails1())

# print(harry.printdetails())