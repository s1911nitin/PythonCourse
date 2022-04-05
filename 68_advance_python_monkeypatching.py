"""
Monkey patching - To dynamically change the value of a method which is defined inside class.
"""

class Employee:
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")

harry = Employee("Harry",500,"Senior Programmer")
rohan = Employee("Rohan",400,"Junior Programmer")

# print(harry.printdetails())

def who_is_nitin():
    return("Nitin is a good programmer too !")

harry.printdetails = who_is_nitin
print(harry.printdetails())

