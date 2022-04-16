"""
Abstract Base Class - It gives an order to the other classes which are derived classes of this class
to declare the same method inside them which is already defined inside abstract base class.

If we do not define the same method inside derived class so it gives an error and we cannot access
instance variables, class variables and methods of derived class.
"""

from abc import ABC, abstractmethod

class Order(ABC):
    @abstractmethod
    def important(self):
        return(0)

class Square(Order):
    def __init__(self,x):
        self.square = x**2

    def printdetail(self):
        return(f"Square of a number: {self.square}")

    def important(self):
        return super().important()

sq = Square(5)

# print(sq.square)
# print(sq.printdetail())
print("Mandate Method:",sq.important())