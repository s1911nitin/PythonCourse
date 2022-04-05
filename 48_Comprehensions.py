"""
Comprehensions - This is a way or an approach which is used for convenient purpose.
"""

# List = []

# for item in range(1,11):
#     if item%2 !=0:
#         List.append(item)

# print(List)

# List = [item for item in range(1,11) if item%2 !=0]
# print(List)


# d1 = {}

# for item in range(1,11):
#     if item%2 == 0:
#         d1.update({f"item{item}":item})

# print(d1)

# d2 = {}

# for key,value in d1.items():
#     d2[value] = key

# print(d2)


# d1 = {f"item{item}":item for item in range(1,11) if item%2 == 0}

# print(d1)

# d2 = {value:key for key,value in d1.items()}

# print(d2)


# s1 = set()

# for item in range(1,11):
#     if item%2 !=0:
#         s1.add(f"Dress{item}")

# print(s1)

# s1 = {f"Dress{item}" for item in range(1,11) if item%2 != 0}

# print(type(s1))
# print(s1)


# def gen(n):
#     for item in range(1,n+1):
#         yield(item)
# n = int(input("Enter a number: \n"))
# g = gen(n)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())


# g = (item for item in range(1,6))

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# g = (item for item in range(1,int(input("Enter a number: \n"))+1))

# print(type(g))

# for item in g:
#     print(item)





class Comprehension:
    def list_comp(self):
        i = int(input("Enter a number: \n"))
        List = [item for item in range(i) if item%2 == 0]
        return(List)

    def dict_comp(self):
        i = int(input("Enter a number: \n"))
        d1 = {f"item{item}":item for item in range(i) if item%2 == 0}
        return(d1)

    def set_comp(self):
        i = int(input("Enter a number: \n"))
        s1 = {f"Dress{item}" for item in range(i) if item%2 == 0}
        return(s1)

    def gen_comp(self):
        i = int(input("Enter a number: \n"))
        g = (item for item in range(i) if item%2 == 0)
        return(g)


comp = Comprehension()
while(True):
    n = int(input("Type 1 for List, 2 for Dict, 3 for Set and 4 for Generator Comprehension: \n"))
    if n == 1:
        print(comp.list_comp())
    elif n == 2:
        print(comp.dict_comp())
    elif n == 3:
        print(comp.set_comp())
    else:
        print(comp.gen_comp())
        for item in comp.gen_comp():
            print(item)


