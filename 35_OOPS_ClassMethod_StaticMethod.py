
class Employee:
    leaves = 10

    def __init__(self,aname,asalary,arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return(f"The details of an employee: Name-{self.name}, Salary-{self.salary} and Role-{self.role}")

    @classmethod
    def change_leaves(cls,value):
        cls.leaves = value

    @classmethod
    def alternate_constructor(cls,string):
        List = string.split("-")
        # return(cls(List[0],List[1],List[2]))
        return(cls(*List))

    @staticmethod
    def normal_method(string,*args,**kwargs):
        print(type(args))
        for item in args:
            print(item)
        print(type(kwargs))
        for key,value in kwargs.items():
            print(key,":",value)
        return(f"This is normal method which we used to access outside class earlier in this course- {string}")

    @classmethod
    def change_leaves_value_args_kwargs(cls,value,*args,**kwargs):
        cls.leaves = value
        print(type(args))
        for item in args:
            print(item)
        print(type(kwargs))
        for key,value in kwargs.items():
            print(key,":",value)




harry = Employee("Harry",500,"Instructor")
rohan = Employee("Rohan",400,"Programmer")
hamad = rohan.alternate_constructor("Hamad-350-JuniorEngineer")


# print(rohan.printdetails())

# harry.leaves = 5
# print(harry.leaves)

# print(harry.leaves)
# rohan.change_leaves(20)
# print(harry.leaves)
# print(rohan.leaves)

# print(hamad.printdetails())

# L1 = ["Carry","Larry","Sherry"]
# d1 = {
#     "Python":"Programming Language",
#     "Django":"Python Web Framework"
# }
# print(hamad.normal_method("Yes, it is correct",*L1,**d1))


L1 = ["Carry","Larry","Sherry"]
d1 = {
    "Python":"Programming Language",
    "Django":"Python Web Framework"
}

harry.change_leaves_value_args_kwargs(25,*L1,**d1)
print(hamad.leaves)