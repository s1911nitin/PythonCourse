"""
Function Caching - Suppose we have a function which opens up a web browser and takes an input
as url in url resolver to access a website which will prompt to download a book and it takes
5 minutes to download.

So, if we are repeating the same process means providing the same input so it is obvious to get
the same output and it will take 5 minutes, we do not want to spend 5 minutes if we know an expecting
output so function caching comes up in role.

We will cache the function if same input is providing otherwise normal time will be taken.

We can achieve function caching using decorator lru_cache which reside inside package functools.
@lru_cache(maxsize=int)  this decorator has attribute maxsize=3 so it will cache previous three calls.
"""

import time
from functools import lru_cache

@lru_cache(maxsize=3)
def func(x):
    time.sleep(3)
    return(x)

print("Took Time",func(5))
print("Took Time",func(10))
print("Took Time",func(15))
print("Cache Record",func(5))
print("Took Time",func(12))
print("Took Time",func(10))
print("Cache Record",func(5))