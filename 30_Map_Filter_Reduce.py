"""
map() - This is used to apply required function on all the items or elements of an iterable like list.
"""

List = ["55","67","32","15","67","26","5"]

# List1 = []

# for item in List:
#     item = int(item)
#     List1.append(item)

# print(List1[2]+List1[6])

# List1 = list(map(int,List))
# print(List1[2]+List1[6])


# L1 = [2,4,7,9,15,17,22,25]

# L2 = list(map(lambda x : x**2, L1))

# print(L2)


"""
filter() - It is used to filter the items or elements of a given iterable list or tuple.
"""

L1 = [2,4,7,9,15,17,22,25,1,4,66,37]

# def func(x):
#     return(x>=7)

# L2 = tuple(filter(func,L1))
# print(L2)

# L2 = list(filter(lambda x : x>=7,L1))
# print(L2)

"""
reduce() - It is used to get commulative addition, substraction, multiplication and division of an elements of an iterable.

We cannot use it directly as it is inside the module functools.
"""

List = [1,2,3,4]

# print(sum(List))            First approach to get commulative addition

# sum = 0
# for item in List:
#     sum = sum + item
# print(sum)

from functools import reduce

sum = reduce(lambda x,y : (x+y),List)             # Commulative addition
print("Addition:",sum)


