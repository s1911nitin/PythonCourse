"""
join() - It is also one of the built in function which is used for convenieance purpose.

This is used to join the items or elements of an iterable like list or tuple by a string.

"""

tp = ("John Cena","Randy Orton","Shawn Micheal","The Undertaker","The Rock","Triple H")

# for item in tp:
#     print(f"{item} and ", end="")
# print("The other WWE Superstars !")

print(" and ".join(tp), end=" ")
print("and The Other WWE Superstars !")