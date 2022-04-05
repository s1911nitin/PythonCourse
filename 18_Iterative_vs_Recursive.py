
# Iterative approach - When we use function through loop to iterate items.

"""
Factorial:              n! =  n*n-1*n-2*....1

Formula of factorial:   n! =  n*(n-1)!

"""


# def iter_fac(n):
#     fac = 1
#     for i in range(n):
#         fac = fac*(i+1)
#     return(fac)
# n = int(input("Enter a number: \n"))
# print("Factorial:",iter_fac(n))


"""
Recursive approach - When we call function inside the decalaration of a given
function so that function is called deeper into deeper to find out where that
function will be break if it executes maximum recurssion and function is not
break so it gives a maximum recursion error.

Note- We can break recursion by appling condition.
"""

# def func_rec():
#     print("Nitin is a good boy")
#     func_rec()                     # func_rec is not breaking here.
# func_rec()


# def rec_fac(n):
#     if n == 1:
#         return(1)
#     else:
#         fac = n*rec_fac(n-1)
#         return(fac)

# n = int(input("Enter a number: \n"))
# print("Factorial:",rec_fac(n))


"""
Fibonacci series :    0 1 1 2 3 5 8.........

Formula:              (n-1) + (n-2)
"""


# def iter_fib(n):
#     a,b = 0,1
#     if n == 0:
#         return(a)
#     elif n == 1:
#         return(b)
#     else:
#         for i in range(2,n+1):
#             c = a+b
#             a = b
#             b = c
#         return(b)
# n = int(input("Enter a number: \n"))
# print("Fibonacci:",iter_fib(n))



# def rec_fib(n):
#     if n == 0:
#         return(0)
#     elif n == 1:
#         return(1)
#     else:
#         fib = rec_fib(n-1) + rec_fib(n-2)
#         return(fib)

# n = int(input("Enter a number: \n"))
# print("Fibonacci:",rec_fib(n))



# Pythonic approach of fibonacci-   Beauty of python

# def pythonic_fib(n):
#     a,b = 0,1
#     for i in range(n):
#         a,b = b,a+b
#     return(a)

# n = int(input("Enter a number: \n"))
# print("Pythonic Fibonnaci:",pythonic_fib(n))


"""
Write a program to find out a given number is prime or not ?

Prime Number- Those numbers which are divisble by 1 and itself and make sure 1 is not a prime number.

2 3 5 7 11 13 17 19 23......

"""

# counter = 0
# def prime_number(n):
#     if n == 1:
#         print("Not a prime number")
#     else:
#         for i in range(1,n+1):
#             if n%i==0:
#                 global counter
#                 counter+=1
#         if counter == 2:
#             print("Prime Number")
#         else:
#             print("Not a prime number")
# n = int(input("Enter a number: \n"))
# prime_number(n)



def prime_number(n):
    if n == 1:
        print("Not a prime number")
    else:
        counter = 0
        for i in range(1,n+1):
            if n%i==0:
                counter+=1
        if counter == 2:
            print("Prime Number")
        else:
            print("Not a prime number")
n = int(input("Enter a number: \n"))
prime_number(n)







