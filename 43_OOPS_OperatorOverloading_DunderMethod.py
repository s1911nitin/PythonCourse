"""
Operator overloading - When we use operator like + - * / between two instances of a class,
this is known as operator overloading and we can handle it with the help of some dunder
methods.

Dunder methods - It always starts and ends with double __

They are special methods which are used for some specific task like __init__()
"""

class Employee:
    leaves = 10

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def __printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")

    def __add__(self,obj):
        return((self.salary)+(obj.salary))

    def __sub__(self,obj):
        return((self.salary)-(obj.salary))
    
    def __mul__(self,obj):
        return((self.salary)*(obj.salary))

    def __truediv__(self,obj):
        return((self.salary)/(obj.salary))



class Programmer(Employee):
    def __init__(self, bname, bsalary, brole, blanguage):
        super().__init__(bname, bsalary, brole)
        self.language = blanguage

    def printdetails1(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary}, Role-{self.role} and Language-{self.language}")

    def __add__(self, obj):
        return super().__add__(obj)

    def __repr__(self):
        return(f"Programmer({self.name},{self.salary},{self.role},{self.language})")

    def __str__(self):
        return(f"Object details are : {self.name},{self.salary},{self.role},{self.language}")

harry = Employee("Harry",500,"Instructor")
rohan = Employee("Rohan",400,"Junior Engineer")
hamad = Programmer("Hamad",450,"Programmer","Python")

# print(hamad._Employee__printdetails())

# print(harry, hamad)

# print((harry.salary)+(hamad.salary))

# print(harry+rohan)
# print(harry/rohan)

# print(harry+hamad)
# print(harry-hamad)
# print(harry*hamad)
# print(harry/hamad)

# print(hamad+harry)        

# print(hamad, harry)

# print(hamad.__repr__())

# print(str(hamad))



"""
print(obj1+obj2) 

Note - 1) It must be to define __add__() in that class whose object is obj1.

2) If __str__() and __repr__() both are defined so priority will go with __str__().
"""