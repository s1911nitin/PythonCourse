"""
__init__() - This is dunder method which is known as Constructor

It is used to do some work which we wants to execute at the time of creating an object or instance.
"""

class Employee():
    leaves = 10

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role} ")

    
harry = Employee("Harry",500,"Instructor")
rohan = Employee("Rohan",400,"Programmer")

# print(harry.salary,rohan.role)
# print(rohan.printdetails())
print(harry.printdetails())
