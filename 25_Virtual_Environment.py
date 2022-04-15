"""
Virtual Environment - 

Suppose I am creating a website which use flask version 2.0 and
I built it and after 4 years one of my friend wants to create a
website so he asks me for a code.

I share the code to him and he installs all the required modules
so this code may not execute properly because when he will be
installing dependent module like flask so might be version has 4.1
so this could be the reason for compatibility issue.

To avoid this, he can create a virtual environment so his root or
system environment will be separate and he can install the required
version module which was used before 4 years at the time of creating
website and due to which no compatibility issue will be raised.

Note - Whenever you provide the code to somebody please provide
requirements.txt as well where all the modules are listed which
were used to create that app or website along with their versions.


We have one module virtualenv in python which is responsible for virtual environment.

pip install virtualenv

We can decide the folder first where we need to create a virtual environment.
Move to the path or directory folder which you created just and then follow this command

virtualenv nitz    

To activate virtual environment nitz follow this command and make sure to move to the path
first where you have virtual environment otherwise it won't work

.\nitz\Scripts\activate

When it activates so you will see path like this (nitz) C:\Users\Nitin Manali\Python3.10\Nitz>

You can install modules now inside this environment using pip

To deactivate virtual environment follow command

deactivate

To create requirements.txt in a same folder where our virtual environment exists follow this command
make sure to move to the path where virtual environment exists first then command would be

pip freeze > .\requirements.txt

To install modules from requirements.txt follow this command in a same path where environment exists.

pip install -r .\requirements.txt


Is there a way to create a virtual environment which comes up with shipping of all the modules exists
in system environment ?

Yes, please follow this command for this

virtualenv --system-site-packages nitz
"""

