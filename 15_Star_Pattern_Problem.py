"""
Write a program to take user defined input as number n to display star pattern
if user defined boolean input is True so pattern would be like

                *
                * *                       n=5
                * * *
                * * * *
                * * * * *

if user defined boolean input is False so pattern would be like  

               * * * * *
               * * * *
               * * *
               * *
               *

"""

n = int(input("Enter a number: \n"))
b = bool(int(input("Type 0 for False, 1 for True \n")))

if b == True:
    for i in range(1,n+1):
        for j in range(i):
            print("*",end=" ")
        print()
else:
    for i in range(1,n+1):
        for j in range((n+1)-i):
            print("*",end=" ")
        print()