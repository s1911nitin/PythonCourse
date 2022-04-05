"""
Polymorphism - To obtain various forms is known as Polymorphism.

Real Life Example - Sometimes Shaktiman Sometimes Gangadhar
"""

# class Employee:
#     leaves = 10

#     def __init__(self, aname, asalary, arole):
#         self.name = aname
#         self.salary = asalary
#         self.role = arole
#         self.special = "Special"

#     def printdetails(self):
#         return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")



# class Programmer(Employee):
#     def __init__(self, bname, bsalary, brole, blanguage):
#         self.name = bname
#         self.salary = bsalary
#         self.role = brole
#         self.language = blanguage

#     def printdetails(self):
#         return(f"The details of an employee: Name-{self.name}, Salary-{self.salary}, Role-{self.role} and Language-{self.language}")

# harry = Employee("Harry",500,"Instructor")
# rohan = Employee("Rohan",400,"Junior Engineer")
# hamad = Programmer("Hamad",450,"Programmer","Python")

"""
Here, printdetails() method inside derived class will be different from the same name method inside base class,
this is known as Polymorphism.

There is bad thing as we are not able to access the same name variables and methods of base class
as our interpreter do not move to base class for same entity.

And polymorphism is not a good approach because its override and it is always recommend to use super() which helps
us to use the base class properties along with derived class.

"""

# print(harry.special, rohan.role)
# print(hamad.special)  # It will error as hamad has no attribute special and it cannot check in base class constructor due to polymorphism.


class Employee:
    leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole
        self.special = "Special"

    def printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")



class Programmer(Employee):
    def __init__(self, bname, bsalary, brole, blanguage):
        super().__init__(bname, bsalary, brole)
        self.language = blanguage


    def printdetails(self):
        print(super().printdetails())
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary}, Role-{self.role} and Language-{self.language}")

harry = Employee("Harry",500,"Instructor")
rohan = Employee("Rohan",400,"Junior Engineer")
hamad = Programmer("Hamad",450,"Programmer","Python")

# print(rohan.special)
# print(hamad.language, hamad.salary, hamad.special)

print(hamad.printdetails())
print(hamad.leaves)

"""
Note- Polymorphism or Overriding can be avoided by using super()
"""