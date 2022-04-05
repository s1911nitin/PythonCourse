"""
shallow copy - It can handle the change of value at one level only.

deep copy - It can handle the change of value at both one level as well as deeper level.
"""
from copy import copy, deepcopy

L1 = [[1,5],[9,4],[2,7],[6,5]]

L2 = copy(L1)
# L2[1] = 100
# L2[1][1] = 100

# print(L1,L2)

L3 = deepcopy(L1)
# L3[1]=100
# L3[1][1] = 100

# print(L1,L3)



