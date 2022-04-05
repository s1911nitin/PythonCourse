"""
Coroutines - These are those functions which execute in two phases in which first phase will be
executed once and it will be in start mode means first phase won't execute again and it will not
stop and second phase we will use to do further task.

Coroutines are generators so we can generate on the fly value here as we get in iterators.

Ex: Suppose we have a function which reads a book and it takes 5 seconds so that work is done in
initial phase means we do not want to execute this reading task by our function again, it works
one time and it will be in start mode and in next phase we will search the word from this book.

Real life example : When we see a signal which is about to green in a few seconds so we do not
stop the engine of a vehicle usually and waits for the signal to be green and then moves ahead to
our destination.

First phase is starting an engine and it will keep starting and in next phase we will move ahead.
"""

import time

def coroutines():
    book = "Once upon a time there was a king called Ashoka who was very kind !"
    t = time.sleep(5)
    while(True):
        word = yield(t)
        # if word in book:
        #     print("Yes, it is in book")
        # else:
        #     print("Not present in book")
        print("Yes, it is in book") if word in book else print("Not present in book")




g = coroutines()
print("Initial phase: Reading a book is taking time....")
g.__next__()
print("Initial phase has been set means book won't be read again !")
g.send("Ashoka")
g.send("Babar")
g.close()
g.send("king")
