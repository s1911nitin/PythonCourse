
# while - It is a loop which continues till the time condition is true.

# i=0
# while(i<45):
#     print(i)

# i=0
# while(i<45):
#     print(i, end="")
#     i+=1              # We can break the while loop by assignment operator.


# break - It describes itself break keyword means break the current loop.

# continue - It executes the continue statement till the time it is true using while loop and not to execute the rest of the code.


# Write a program to print numbers from 5 to 44 in above code ?

# i=0
# while(i<45):
#     if i<5:
#         i+=1
#         continue
#     print(i, end=" ")
#     i+=1  

# while(1) or while(true) - These are the loops which always run and we use them to define condition under it.

# i=0
# while(1):
#     if i<5:
#         i+=1
#         continue
#     print(i, end=" ")
#     i+=1
#     if i==45:
#         break

# i=0
# while(True):
#     if i<5:
#         i+=1
#         continue
#     print(i, end=" ")
#     i+=1
#     if i==45:
#         break


"""
Write a program to take user defined input in a range of 1 to 100 and it keeps asking to enter a number
till the time you enter a number greater than 100 and if you enter greater than 100 so output comes up
Congrats you entered a number greater than 100 ?
"""

# while(True):
#     i = int(input("Enter a number: \n"))
#     if i<101:
#         continue
#     else:
#         print("Congrats you entered a number greater than 100")
#         break



# Write a program to guess a number which is 16 and there will be 5 turns to guess a number ?

guess=1
print("You would have five guesses only")
while(True):
    i = int(input("Enter a number: \n"))
    if i<16:
        print("Number you entered is smaller")
    elif i>16:
        print("Number you entered is greater")
    else:
        print("You hit the magic number 16")
        print("You took guesses to guess a number", guess)
        break
    print("Number of guesses:", 5-guess)
    guess+=1
    if guess==6:
        print("Game over")
        break


