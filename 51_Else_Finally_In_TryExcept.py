"""
else - else condition can only execute if try condition is True or we can say except block did not execute.

finally - It will always execute either try or except executes
"""

try:
    def divison(x,y):
        divide = x/y
        return(divide)
    x = int(input("Enter the first number: \n"))
    y = int(input("Enter the second number: \n"))
    print(divison(x,y))
except Exception as e:
    print(e)
else:
    print("It won't execute if except block condition is True")
finally:
    print("It will always run either try or except condition is True.")


