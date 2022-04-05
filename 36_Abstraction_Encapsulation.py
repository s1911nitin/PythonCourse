"""
Data Abstraction - Hiding a real mechanism of anything from the general user 
and to provide only that information which is required to perform some task.

General Example - Television remote 

We do not know how remote is working actually to change channels , volume up and down and 
even we are not interested to know about it we simply use it to operate television which 
information is provided by company.

Similary, It happens in code like we are creating one game so one of the employee will create
one class Player and will define methods to move left and right, up and down the player and
will pass this code to the next employee who will create a class City where our player will
move road layout and all.

So, first employee will tell to the next employee I have created Player class and you do not
need to worry how it is moving left, right, up and down, you simply need to use these methods
to use the functionality of Player and you can do further task which is creating a City class.

This is called Data Abstraction.


Encapsulation - A technique which is used to achieve data abstraction is known as Encapsulation.
"""