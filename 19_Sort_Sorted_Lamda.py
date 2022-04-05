"""
sort() - This is a built in function which is made for iterable [] only.

This can be applied on a list which will have same nature of elements.

It changes in original list.
"""

from re import T
from tkinter import Y


List = [9,1,66,32,55,9,4]

# List.sort()
# print(List)

# List.sort(reverse=True)
# print(List)

L1 = [[1,5],[4,2],[9,17],[5,3]]

# L1.sort()
# print(L1)

# def func(x):
#     return(x[1])

# L1.sort(key=func, reverse=True)
# print(L1)

L2 = ["aa","dddd","b","ccc"]

# L2.sort()
# print(L2)

# L2.sort(key=len, reverse=True)
# print(L2)


"""
sorted() - This is a built in function which is made for all the iterables.

It gives us a new list means it does not change into an original list.
"""

List1 = [5,9,33,67,17,55,9,88,12]

# List2 = sorted(List1)
# print(List1,List2)

# List2 = sorted(List1,reverse=True)
# print(List2)

# Original = [[1,5],[4,2],[9,17],[5,3]]

# def func1(x):
#     return(x[1])

# NewList = sorted(Original, key=func1, reverse=True)
# print(Original,NewList)


# Lamda or Anonymous function - This is one liner function which is used for conveniance purpose.

# def sq(x):
#     return(x**2)
# x = int(input("Enter a number: \n"))
# print("Square:",sq(x))

# sq = lambda x : x**2
# x = int(input("Enter a number: \n"))
# print("Square:",sq(x))


# add_sub = lambda x,y : ((x+y),(x-y))
# x = int(input("Enter the first number: \n"))
# y = int(input("Enter the second number: \n"))
# V1,V2 = add_sub(x,y)
# print(V1,V2)

# Original = [[1,5],[4,2],[9,17],[5,3]]

# Original.sort(key=lambda x : x[1], reverse=True)
# print(Original)

