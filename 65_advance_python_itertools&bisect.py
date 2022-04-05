from itertools import product, permutations, combinations, combinations_with_replacement

L1 = [2,5,9,1]
# cartesan_product = product(L1,repeat=2)
# print(list(cartesan_product))

# print(list(permutations(L1,r=2)))

# print(list(combinations(L1,r=2)))
# print(list(combinations_with_replacement(L1,r=2)))


import bisect

L2 = [5,9,11,19,55,66,72,98,105,121]

a = 23
index = bisect.bisect(L2,a)
print(index)

bisect.insort(L2,a)

print("List After Adding Element",L2)