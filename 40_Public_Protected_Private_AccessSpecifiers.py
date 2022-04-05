"""
Access Specifier- Basically, we do not have any access specifier in python however we have
some convention which we can use as access specifier.

Public - All the entities like variables, functions, instance variables, class variables, methods
in python are public by default.

Convention of Public - We do not need to put anything before instance variables, class variables and methods.

Protected - It will not protect anything but just a convention to tell to the others as this is protected
instance variables or class variables and methods.

Convention of Protected - We can put single _ before instance variables, class variables and methods.

Private - You cannot access private instance variable or class variable or method directly as python
do not stop us to execute anything so we can access private convention by Name Mangling Concept.

Convention of Private - We can put double __ to make instance variable or class variable pr method to be private.

Name Mangling Syntax - object._ClassNameOFPrivateEntity__PrivateEntity


"""

class Employee:
    leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def __printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")

class Player:
    __games = ["Cricket","Football"]
    def __init__(self,name):
        self.name = name 


class Programmer(Employee,Player):
    def __init__(self, bname, bsalary, brole, blanguage):
        self.name = bname
        self.salary = bsalary
        self.role = brole
        self._language = blanguage

    def printdetails1(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary}, Role-{self.role} and Language-{self._language}")

harry = Employee("Harry",500,"Instructor")
rohan = Employee("Rohan",400,"Junior Engineer")
virat = Player("Virat")
hamad = Programmer("Hamad",450,"Programmer","Python")

# print(hamad.printdetails1())
# print(hamad._language)

# print(virat.name)
# print(virat._Player__games)

# print(harry._Employee__printdetails())
print(hamad._Employee__printdetails())
print(hamad.printdetails1())