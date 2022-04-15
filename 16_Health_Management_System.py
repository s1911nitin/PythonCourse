
from datetime import datetime

def client_log(client):
    if client == 1:
        print("You have selected client Harry \n")
        n2 = int(input("What would you like to do ?, Type 1 to Log diet, 2 to Log exercise \n"))
        if n2 == 1:
            with open("harry_diet.txt","a") as f:
                f.write(input("Enter the diet name: \n") + " at " + str(datetime.now()) + "\n")
                print("Diet of Harry has been successfully saved !!")
        else:
            with open("harry_exercise.txt","a") as f:
                f.write(input("Enter the exercise name: \n") + " at " + str(datetime.now()) + "\n")
                print("Exercise of Harry has been successfully saved !!")
    elif client == 2:
        print("You have selected client Rohan \n")
        n2 = int(input("What would you like to do ?, Type 1 to Log diet, 2 to Log exercise \n"))
        if n2 == 1:
            with open("rohan_diet.txt","a") as f:
                f.write(input("Enter the diet name: \n") + " at " + str(datetime.now()) + "\n")
                print("Diet of Rohan has been successfully saved !!")
        else:
            with open("rohan_exercise.txt","a") as f:
                f.write(input("Enter the exercise name: \n") + " at" + str(datetime.now()) + "\n")
                print("Exercise of Rohan has been successfully saved !!")
    else:
        print("You have selected client Hamad \n")
        n2 = int(input("What would you like to do ?, Type 1 to Log diet, 2 to Log exercise \n"))
        if n2 == 1:
            with open("hamad_diet.txt","a") as f:
                f.write(input("Enter the diet name: \n") + " at " + str(datetime.now()) + "\n")
                print("Diet of Hamad has been successfully saved !!")
        else:
            with open("hamad_exercise.txt","a") as f:
                f.write(input("Enter the exercise name: \n") + " at " + str(datetime.now()) + "\n")
                print("Exercise of Hamad has been successfully saved !!")

def client_fetch(client):
    if client == 1:
        print("You have selected client Harry \n")
        n2 = int(input("What would you like to do ?, Type 1 to Fetch diet, 2 to Fetch exercise \n"))
        if n2 == 1:
            with open("harry_diet.txt","r") as f:
                print(f.read())
        else:
            with open("harry_exercise.txt","r") as f:
                print(f.read())
    elif client == 2:
        print("You have selected client Rohan \n")
        n2 = int(input("What would you like to do ?, Type 1 to Fetch diet, 2 to Fetch exercise \n"))
        if n2 == 1:
            with open("rohan_diet.txt","r") as f:
                print(f.read())
        else:
            with open("rohan_exercise.txt","r") as f:
                print(f.read())
    else:
        print("You have selected client Hamad \n")
        n2 = int(input("What would you like to do ?, Type 1 to Fetch diet, 2 to Fetch exercise \n"))
        if n2 == 1:
            with open("hamad_diet.txt","r") as f:
                print(f.read())
        else:
            with open("hamad_exercise.txt","r") as f:
                print(f.read())

print("Welcome to Health Management System by Instructor Nitin \n")
n1 = int(input("What would like to do ?, Type 1 for Log client details, 2 to Fetch client details \n"))
if n1 == 1:
    client = int(input("Type 1 for Harry, 2 for Rohan and 3 for Hamad \n"))
    client_log(client)
else:
    client = int(input("Type 1 for Harry, 2 for Rohan and 3 for Hamad \n"))
    client_fetch(client)
