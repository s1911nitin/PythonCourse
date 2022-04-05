"""
Multilevel Inheritance - When class B is inherited class A and class C is inherited class B
so class C will have its own property as well as previous two level classes B and A.

So, here inheritance occurs at level basis.
"""

class Father():
    var = 2

class Son(Father):
    # var = 5
    pass

class Grandson(Son):
    # var = 10
    pass

harry = Father()
rohan = Son()
hamad = Grandson()

print(hamad.var)