"""
open() - This is the built in function which is used to do operations with file in python.

f = open("filename", "r")

open function is opening the file filename in read mode and f is the file handler which will
have all the contents of the filename.

There are several file modes which are listed below:

r - To read a file
w - To write a file
a - To append a file
r+ - To update(read or write a file)
t - Text mode
b - Binary mode

Note: r and t both are default mode.
"""

# f = open("rough.txt","w")
# f.write("This is best python & django tutorial ever !")   # It wipes out the content in file.
# f.close()

# f = open("rough.txt","rt")
# content = f.read()
# print(content)
# f.close()

# f = open("rough.txt","a")
# f.write("\nYou will be able to learn beauty of python here. \n")
# f.write("Nitin would be the tutor of python and django course. \n")
# f.close()

# f = open("rough.txt")
# print(f.read())
# f.close()

# f = open("rough.txt","rt")
# content = f.readline()
# content2 = f.readline()
# print(content, end="")
# print(content2)
# f.close()

# f = open("rough.txt","rt")
# print("1:",f.read())
# print("2",f.readline())
# f.close()

# f = open("rough.txt")
# content = f.read()
# for item in content:
#     print(item)
# f.close()

# f = open("rough.txt")
# for item in f:
#     print(item, end="")
# f.close()

# tell - It tells indexing where our handler is pointing right now in a file.

# f = open("rough.txt")
# print(f.readline(), end="")
# print(f.tell())
# f.close()

# seek- Suppose we have read multiple lines or content and we wish to read the file again by shuffling the handler location.

# f = open("rough.txt")
# print(f.read(45))
# f.seek(10)
# print(f.read())
# f.close()

# f = open("rough.txt")
# print(f.readlines())
# f.close()

# with open("rough.txt","rt") as f:
#     print(f.read())


# Note- We do not need to close the file like f.close() if we are using with block as it closes file automatically.

