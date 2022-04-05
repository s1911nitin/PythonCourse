"""
OOPS - It stands for object oriented programming.

We can solve the problem by writing a code directly as we did in past
like using function but whenever we do some work so we want to execute
the task in a systematic manner.

So, oops is a technique or way to write a code in a systematic manner
due to which our code looks clean and easy to readable.

class - It is just a like a template where some of the information are already written like RTGS Form of Bank.

When we put some information into that form or template to get a useful information, that information is an instance
or object of that class.

Advantages of class - 

1) Based on DRY (Do Not Repeat Yourself) concept.
2) To restrict an access of a function.

"""
class Employee:
    leaves = 10
    
harry = Employee()
rohan = Employee()

harry.name = "Harry"
harry.salary = 500
harry.role = "Instructor"

rohan.name = "Rohan"
rohan.salary = 400
rohan.role = "Programmer"
rohan.salary = 450

# print(harry.salary, rohan.role)
# print(rohan.leaves)
# print(Employee.leaves)


# print(rohan.salary)
# rohan.leaves = 5
# print(rohan.leaves)
# print(harry.leaves)

# Employee.leaves = 5
# print(harry.leaves)

"""
Note - instance cannot change the value or class variable as it creates instance variable itself.

Instance checks the variable inside its scope first if finds so not to check further in class variable.
"""