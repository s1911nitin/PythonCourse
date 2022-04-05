"""
Write a program to prettify a folder as there will be a file inside the pretiffy folder 
carrying files names which will be out of this operation and apart from these files, 
rest will be captilized and those are with .jpg extension will be renamed by 1.jpg or 
2.jpg and so on ?
"""

import os

def soldier(path,filname,extension):
    cur_dir = os.chdir(path)
    List = os.listdir(cur_dir)
    with open(filname,"rt") as f:
        content = f.read()
    
    i=1
    for item in List:
        if item not in content:
            if item.endswith(extension):
                os.rename(item,f"{i}.jpg")
                i+=1
            else:   
                os.rename(item,item.capitalize())
        else:
            print("No operation")




soldier("C://Users/Nitin Manali/Python3.10/PythonCourse/Soldier","C://Users/Nitin Manali/Python3.10/PythonCourse/Soldier/naveen.txt",".jpg")