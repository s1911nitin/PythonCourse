"""
Function - There are two types of function we have in python.

1) Built in - print(), type(), len() and sum() etc.
2) User defined function - We can create our function using a keyword def in python.

"""

import re


List = [1,2,3,4]

# print(sum(List))    # sum() - It can sum up the elements or items of an iterable like list or tuple.

# def average(x,y):
#     z = (x+y)/2
#     print("Average:", z)
# average(5,4)

# def add_sub(x,y):
#     c = x+y
#     d = x-y
#     return(c,d)
# v1,v2 = add_sub(5,4)
# print(v1,v2)

"""
Docstring -  This is the first line which we declare under the declaration or definition of a function
to describe about the function and it is not read by python interpreter at run time.

It is mentioned as """""" under declaration and we can print it by print(funcname.__doc__)
"""

def exp(n,p):
    """This is a function to get an exponential of any number"""
    y = n**p
    return(y)
print(exp.__doc__)
n = int(input("Enter a number: \n"))
p = int(input("Enter a power: \n"))
print("Exponential is",exp(n,p))


