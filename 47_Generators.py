"""
Iterables - Those entities or objects on which we can apply loop to iterate their elements like list, tuple etc.

Iterators - These are those objects which are returned when we apply __iter__() on iterables.

When we apply __next__() on iterator object so it will return first indexing element of an iterable and so on
make sure when you have accessed all the elements of an iterable by applying __next__() on iterator object and
you apply __next__() again on iterator object so it gives an error stop iteration error.

We can apply loop directly on iterator object to return items on iterables and when we apply loop there is a
beauty of for loop which handle the iteration without giving stop iteration error.

Iteration - When we apply loop on iterables or iterators to iterate an items of an iterables, this process is
known as Iteration.

"""

# List = ["Harry","Larry","Carry"]

# iter_obj = List.__iter__()
# print(type(iter_obj))
# print(iter_obj.__next__())
# print(iter_obj.__next__())
# print(iter_obj.__next__())
# print(iter_obj.__next__())

# for item in iter_obj:
#     print(item)

# a = 5
# b = a.__iter__()            # It gives an error as int object has no attribute __iter__()
# print(b)


"""
Generator - These are those objects which is created using yield keyword in python.

As generators are iterators so we can use them for the future purpose when we will
need of them using for loop or by applying __next__().

We simply create generators using yield keyword to make them capable for using in
future when we will need of it (We are not using them right now but we can in future as we have made them capable to use).
"""

def gen(n):
    for i in range(1,n+1):
        yield(i)

n = int(input("Enter a number: \n"))
g = gen(n)

print(type(g))            
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

for item in g:
    print(item)