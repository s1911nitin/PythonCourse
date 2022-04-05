"""
We have one external module pyinstaller which is used to convert .py to .exe in python programming.

syntax - pyninstaller pythonfile.py

It creates .exe file with all dependencies if we wish to get only one file so we can write this command

pyinstaller --oneline pythonfile.py 
"""

from win32com.client import Dispatch

def text_to_speech_func(text):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.speak(text)

text = "BAAR BAAR DIN AAYE BAAR BAAR DIL YE GAYE TUM JIYO HAZARO SAAL HAI MERI YE ARZOO HAPPY BIRTHDAY TO YOU NITIN HAPPY BIRTHDAY TO YOU NITIN HAPPY BIRTHDAY TO YOUUUUUUUUUUU"
text_to_speech_func(text)