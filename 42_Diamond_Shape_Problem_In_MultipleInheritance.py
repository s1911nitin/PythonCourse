"""
Multiple Inheritance does not exist in some of the languages like c++, Java etc.

But python is a language where it can be handled very cleanly so we do not face any
problem to handle Diamond Shape Problem.

                                 class A

                        class B(A)     class C(A)

                               class D(B,C)
"""

class A:
    var = 5

class B(A):
    # var = 10
    pass

class C(A):
    # var = 15
    pass

class D(B,C):
    # var = 20
    pass

a = A()
b = B()
c = C()
d = D()
    

print(d.var)