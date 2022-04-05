"""
__slots__ - It restricts dynamic creation of instance variable means those instance variables
are created at the time of creating an object through constructor will be considered only.
"""

class Employee:
    __slots__ = ["name","salary","role"]
    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
    def printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")

harry = Employee("Harry",500,"Senior Programmer")
rohan = Employee("Rohan",400,"Junior Programmer")

# print(rohan.role)
# harry.special = "Special"
# print(harry.special)

# print(harry.printdetails())

# print(harry.__dict__)   # It returns dictionary representation of instance variable values if __slots__ is not present only.