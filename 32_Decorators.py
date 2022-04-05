"""
Decorators - These are those functions which take one function as an argument
and returns another function.

It is used to enhance the functionality of a function which is taken as an argument.
"""

# def welcome():
#     print("Nitin is a good programmer")
# welcome()

# def welcome():
#     print("Nitin is a good programmer")
# wel = welcome
# del welcome
# welcome()      # NameError: name 'welcome' is not defined

# def welcome():
#     print("Nitin is a good programmer")
# wel = welcome
# del welcome
# wel()


# def welcome(func):
#     func("Nitin is a good programmer")
# welcome(print)


# def welcome(x):
#     if x == 5:
#         print(int)
# welcome(5)


# Decorator-

def dec(func):
    def nowexec():
        print("Before calling func")
        func()
        print("After calling func")
    return(nowexec)


# def who_is_nitin():
#     print("Nitin is a good programmer")
# who_is_nitin = dec(who_is_nitin)
# who_is_nitin()

@dec
def who_is_nitin():
    print("Nitin is a good programmer")
# who_is_nitin = dec(who_is_nitin)
who_is_nitin()

