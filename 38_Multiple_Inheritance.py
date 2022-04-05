"""
Multiple Inheritance - When one class is derived from two or more classes.

Derived class will have both properties of its own as well as inherit classes.

Note- Derived class will check variables first in its own and if not find so
will check in that class which comes up in first place.
"""

class Employee:
    leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")

class Player:
    games = ["Cricket","Football"]
    def __init__(self,name):
        self.name = name 


class Programmer(Employee,Player):
    def __init__(self, bname, bsalary, brole, blanguage):
        self.name = bname
        self.salary = bsalary
        self.role = brole
        self.language = blanguage

    def printdetails1(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary}, Role-{self.role} and Language-{self.language}")

harry = Employee("Harry",500,"Instructor")
rohan = Employee("Rohan",400,"Junior Engineer")
virat = Player("Virat")
hamad = Programmer("Hamad",450,"Programmer","Python")

# print(hamad.printdetails1())
# print(hamad.printdetails())

# print(virat.name)
print(hamad.games)




