"""
Whenever we write import modulename so we get the code of that particular module
in our code and then we can use their functions in our code.

Now the question from where import keyword brings the code of that module for us.

There must be one place where all the modules reside in python so how we can find
it out.
"""

import sys

print(sys.path) # It gives us a hierarchy path from where import brings the code of module for us.


"""
Note - import keyword always check the current working directory first to locate the module so
if we keep the file name as same as module name so it will confuse as he locates the module but
not getting the exact code and will not move further to check the next path due to which will
give an error.

That is why it is always recommended to keep the file name different from the module name.
"""