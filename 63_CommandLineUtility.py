"""
Suppose I am asking you to write a program which opens up an excel which is GUI app and do
computations and whatever result comes takes it back to a program , it can be done but this
would be too difficult as we are getting an output of GUI to Command Line.

To avoid this, we create a command line utility for the output we are looking for and it does
not matter in which programming language we are creating command line utility and taking output
of that into different programming language or command line utility.

Ex: We are creating a Java app and our project needs of some machine learning output and we know
python is superb for machine learning due to library tenserflow so java programmer will come to
python and will create command line utility for which he is looking for and then there are several
techniques to pass code between two command line utility or two programming languages.

We can create command line utility in python using inbuilt module called argparse

Note - Command line utility is used to pass arguements at run time.
"""

import argparse
import sys

parser = argparse.ArgumentParser()

parser.add_argument("--x",type=float,default=5.0,help="Enter the first number")
parser.add_argument("--y",type=float,default=4.0,help="Enter the second number")
parser.add_argument("--o",type=str,default="+",help="Enter the operator")

arg = parser.parse_args()


def func(arg):
    if arg.o == "+":
        return(arg.x+arg.y)
    elif arg.o == "-":
        return(arg.x-arg.y)
    elif arg.o == "*":
        return(arg.x*arg.y)
    else:
        return(arg.x/arg.y)


obj = func(arg)
sys.stdout.write(str(obj))
