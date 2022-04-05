"""
== - When two object having same values either pointing to same or different memory location, == will be True.

is - When two object is refrencing to same memory location, is will be True in this condition only.
"""

L1 = [5,7,2,6]

L2 = L1

L3 = [2,7,5,6]

L4 = [5,7,2,6]

# print(L1 is L2)
# print(L1 == L2)

# print(L1 is L3)
# print(L1 == L3)

# print(L2 is L3)
# print(L2 == L3)

# print(L2 is L4)
# print(L2 == L4)

