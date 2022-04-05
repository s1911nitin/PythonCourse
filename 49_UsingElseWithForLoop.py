"""
We can use else condition with for loop if for loop iterates all the elements of an iterable
like list, tuple etc.

If we break the for loop some how so we cannot use else condition.
"""

List = ["Dal","Paneer","Brinjal","GajarKaHalwa","Salad"]

# for item in List:
#     print(item)
# else:
#     print("Else condition can only execute with for loop when for loop iterates all the elements of an iterable !!")


for item in List:
    if item == "Brinjal":
        break
else:
    print("Else condition cannot execute this time as for loop did not execute completely !")