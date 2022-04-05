"""
When we define or declare a function so there are three parameters exists mainly
first would be normal argument second is *args third is **kwargs.

Sequence matters means we cannot define **kwargs first then normal argument then *args.

Syntax -

def func(normal,*args,**kwargs):
    print(normal)
func("normal")

Note - *args and **kwargs are optional.
"""

# def func(a,b,c,d):
#     print(a,b,c,d)
# func("Virat","Rohit","Pandaya","Pant")              Not a right approach to display users

# def func(*args):
#     print(type(args))
#     for item in args:
#         print(item,end=" ")

# L1 = ["Virat","Rohit","Pandaya","Pant"]
# func(*L1)

# def func(*args,**kwargs):
#     print(type(args))
#     for item in args:
#         print(item,end=" ")
#     print(type(kwargs))
#     for key,value in kwargs.items():
#         print(key,":",value)

# L1 = ["Virat","Rohit","Pandaya","Pant"]
# d1 = {"Harry":2,"Larry":4,"Carry":8}
# func(*L1,**d1)



def func(normal,*args,**kwargs):
    print(type(args))
    for item in args:
        print(item,end=" ")
    print(type(kwargs))
    for key,value in kwargs.items():
        print(key,":",value)
    print(normal)

L1 = ["Virat","Rohit","Pandaya","Pant"]
d1 = {"Harry":2,"Larry":4,"Carry":8}
normal = "Nitin is a good programmer !"
func(normal,*L1,**d1)



