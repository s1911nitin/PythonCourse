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







or second solution






# OhSoldierPrettifyMyFolder in python

import os

folder_path = os.getcwd() + "\solider"
not_touch_file = folder_path + "\harry.txt"

print(folder_path)

index = 0


def solider(folderpath, nottouchfile, extension):

    my_folder_list = os.listdir(folderpath)
    
    for item in my_folder_list:

        print("My item is ", item)

        f = open(nottouchfile, "rt")
        content = f.read()


        if item.split(".")[0] in content:
            print("not touch hurray")
            if item == "harry.txt":
                print("Done")
                pass
            else:
                os.rename(f"{folderpath}\{item}", f"{folderpath}\{item}")
                print("Done")
        else:
            if item.endswith(extension):
                global index
                print("Hurray2")
                os.rename(f"{folderpath}\{item}", f"{folderpath}\{index}.jpg")     
                index +=1
            else:
                print("Hurray")
                os.rename(f"{folderpath}\{item}", f"{folderpath}\{item.capitalize()}")


solider(folder_path, not_touch_file, ".jpg")


