
# for - It is a loop which continues till all the elements or items of an iterable are iterated.

L1 = [["Harry",2],["Larry",4],["Carry",8],["Merry",16]]

# for item in L1:
#     print(item)

# for key, value in L1:
#     print(key,":",value)

d1 = dict(L1)

# print(type(d1))

# for key, value in d1.items():
#     print(key,"=",value)


# Write a program to print an items which ends with "rry" only ?

List = ["Harry","Larry","Carry","Harpic","Vimbar",5,9,"Sherry"]

# for item in List:
#     if str(item).isalpha() and str(item).endswith("rry"):
#         print(item)

# Write a program to print all the numbers which are greater than equal to 6 ?

List1 = ["Harry","Sam",55,8,2,5,6,"Sherry",6,25,10]

for item in List1:
    if str(item).isnumeric() and item>=6:
        print(item, end=" ")
