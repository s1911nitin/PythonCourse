"""
Write a program which will help programmer to stay healthy ?

When programmer comes on desk, he/she will execute this code which
will notify by sounding audio of water as Drinking water time in some
time interval, similarly for eyes exercise and physical activity.

Once programmer is done with any acitiviy so program will prompt to 
write like Drank water so this will be recored in one text file to
track activities.

Note - To play mp3 files we have one module in python called pygame
so we will install it using pip.
"""





import time
from pygame import mixer
from datetime import datetime


def play_sound(file,word):
    if word == "Drank Water":
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while(True):
            user_input = input("Type Drank Water to stop music \n")
            if user_input == word:
                mixer.music.stop()
                break
    elif word == "Eye Exercise Done":
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while(True):
            user_input = input("Type Eye Exercise Done to stop music \n")
            if user_input == word:
                mixer.music.stop()
                break
    else:
        mixer.init()
        mixer.music.load(file)
        mixer.music.play()
        while(True):
            user_input = input("Type Physical Exercise Done to stop music \n")
            if user_input == word:
                mixer.music.stop()
                break

def log_file(msg):
    with open("log_data.txt","a") as f:
        f.write(f"{msg} at {datetime.now()} \n")
        f.close()


initial_water = time.time()
initial_eye = time.time()
initial_physical = time.time()

print("Welcome into the Healthy Programmer Program !!")
while(True):
    if time.time()-initial_water>10:
        print("Drinking Water Time....")
        play_sound("Water.mp3","Drank Water")
        log_file("Drank Water")
        initial_water = time.time()
    elif time.time()-initial_eye>18:
        play_sound("Eye.mp3","Eye Exercise Done")
        log_file("Eye Exercise Done")
        initial_eye = time.time()
    elif time.time()-initial_physical>30:
        play_sound("Physical.mp3","Physical Exercise Done")
        log_file("Physical Exercise Done")
        initial_physical = time.time()


 








