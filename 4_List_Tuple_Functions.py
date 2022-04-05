
L1 = ["Harry","Larry","Carry","Merry", 145.5, 20, "Vimbar",20]

# print(type(L1))
# print(L1)

# print(len(L1))  # It tells the length of the variable which starts from 1.

# List Slicing - It is as similar as string slicing

# print(L1[:8:2]) # It includes Harry at 0 index and will go on till 7 along with skipping by 1.

L1.append("Sugar")
L1.extend([15,5.5,"Salt","Jam"])
L1.insert(2,"Sherry")
L1.pop()
L1.remove("Sherry")
L1.remove(20)
# print(L1)

L2 = [10,25,5,10,9,77,65,14]
L2.reverse()
# print(L2)
L2.sort()
# print(L2)
L2.reverse()
# print(L2)

List = [5,9,10,1,66,9]

List1 = List.copy()

List1.pop()

# print(List, List1)

# Mutable - List is a mutable data type means we can change the value of its item or element.

L3 = [99,1,5.5,99,50,15]

L3[3] = 100
# print(L3) 

# Tuple - It is denoted by paranthesis () and it is immutable means we cannot change the value of its items.

tp = (5,6.6,15,19,5)

# print(type(tp))
# print(tp)

# tp[2] = 25   # TypeError: 'tuple' object does not support item assignment

tp1 = (5,)     # It is a single element tuple.

# print(type(tp1))
# print(tp1)


# Traditional way to swap two numbers

# a = 5
# b = 10
# c = b
# b = a
# a = c

# print(a,b)

# Pythonic way to swap the values of two numbers

a = 5
b = 10

a,b = b,a
print(a,b)


