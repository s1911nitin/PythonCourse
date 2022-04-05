
# z = 30
# def harry():
#     a = 5
#     def rohan():
#         b = 10
#         print(b)
#     rohan()
#     print(a)
# harry()
# print(b)                 # local variable can be accessed inside function only


# z = 30
# def harry():
#     a = 5
#     def rohan():
#         b = 10
#         z = 45            # Z is local variable here first local variable has been checked if not so global variable is checked.
#         print(b,z)
#     rohan()
#     print(a)
# harry()


# z = 30
# def harry():
#     a = 5
#     z = 45 
#     def rohan():
#         b = 10
#         print(b,z)      # First z is checked inside rohan() if does not find so local variable z of harry() will be considered.
#     rohan()
#     print(a,z)
# harry()

# z = 30
# def harry():
#     a = 5
#     z = 45 
#     def rohan():
#         b = 10
#         b+=2           # Local variable value can be changed by assignment operator inside function.
#         print(b,z)      
#     rohan()
#     print(a,z)
# harry()


# z = 30
# def harry():
#     a = 5 
#     def rohan():
#         b = 10
#         b+=2           
#         print(b,z)      # First local variable z will check in rohan() if not so checks in harry() if not so global variable will be considered.
#     rohan()
#     print(a,z)
# harry()


# z = 30
# def harry():
#     a = 5 
#     def rohan():
#         b = 10
#         b+=2
#         z+=5             # We cannot change the global variable value directly straight however it can be done using global keyword.           
#         print(b,z)
#     rohan()
#     print(a,z)
# harry()

# Output : Error like UnboundLocalError: local variable 'z' referenced before assignment


z = 30
def harry():
    a = 5 
    def rohan():
        b = 10
        b+=2
        global z            # Now global variable value will be changed as we used global keyword.
        z+=5                      
        print(b,z)
    rohan()
    print(a,z)
harry()
print(z)                    # Now z will be 35 inside the function as well as outside.

