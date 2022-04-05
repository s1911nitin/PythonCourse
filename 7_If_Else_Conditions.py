
# var1 = 50

# var2 = int(input("Enter the number: \n"))

# if var2<var1:
#     print("Number entered by you is smaller")
# elif var2>var1:
#     print("Number you entered is greater")
# else:
#     print("You entered the same number")


# Write a program to get a driving license if you are 18 plus ?

# Age = int(input("Enter your age: \n"))

# if Age>18:
#     print("Yes, you can get a driving license")
# elif Age == 18:
#     print("We will think about it")
# else:
#     print("You cannot get a license")


"""
Design a faulty calculator which will solve all computations except following:

45*3 = 555, 56+9 = 77, 56/6 = 4, 20-5 = 16
"""


n1 = int(input("Enter the first number: \n"))
n2 = int(input("Enter the second number: \n"))
n3 = input("Enter the operator from : +,-,*,/ \n")

if n1==45 and n2==3 and n3=="*":
    print(555)
elif n3=="*":
    print(n1*n2)
elif n1==56 and n2==9 and n3=="+":
    print(77)
elif n3=="+":
    print(n1+n2)
elif n1==56 and n2==6 and n3=="/":
    print(4)
elif n3=="/":
    print(n1/n2)
elif n1==20 and n2==5 and n3=="-":
    print(16)
else:
    print(n1-n2)