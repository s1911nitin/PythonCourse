"""
raise - This is a keyword in python which is used to raise exception manually
"""

# def divide_func(x,y):
#     divide = x/y
#     return(divide)

# x = int(input("Enter the first number: \n"))
# y = int(input("Enter the second number: \n"))
# if y == 0:
#     raise ZeroDivisionError
# print(divide_func(x,y))

# name = "Harry"

# val = input("Enter your name: \n")
# if val == name:
#     raise ValueError("You are not allowed")
# print(val, "Welcome into the website")

# dict1 = {
#     "Harry":2,
#     "Carry":4,
#     "Larry":8
# }

# val = input("Enter the key name: \n")
# if val == "Sherry":
#     raise KeyError
# else:
#     print("Value of key:",dict1[val])



try:
    def divide_func(x,y):   
        divide = x/y
        return(divide)
    x = int(input("Enter the first number: \n"))
    y = int(input("Enter the second number: \n"))
    if y == 0:
        raise ZeroDivisionError
    print(divide_func(x,y))
except Exception as e:
    print(e)
else:
    print("This will only run when try executes !")
finally:
    print("It will always run either try or except executes !")
