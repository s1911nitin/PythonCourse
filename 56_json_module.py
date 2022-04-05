"""
json data - It looks like a python dictionary however it is quiet different from python dictionary.

We have None in python but we have null in json
We have True in python but we have true in json
We have False in python but we have false in json

Why do we need of it ?

Suppose we have one text line or some so we can parse it using slicing but in real world our data
is not so simple it could be larger where slicing could be difficult to perform so we started data
transmission through xml but it is not so feasible as we create <open_tag>Data</close_tag> so this
approach slows down the data trasmission and then json came into a role which looks like a python
dictionary where no need to open tag close tag so data is transmitting easily between client & server.

json_data = {
    "name":"Harry",
    "Is_programmer":true,
    "salary":500,
}

It is language independent means it is suitable for all the languages and it is quiet popular nowadays
to transfer data over an internet.

As this is not a python object so we cannot parse it directly like we do with python dictionary so we 
have one inbuilt python module called json which is used to convert it python dictionary and then we can
use the data as per our requirements.

There are 4 major functions or methods we need to focus of json module.

loads() - It converts json string into python dictionary.
dumps() - It converts python dictionary into json string.
load() - It pulls json string data from a file and converts it into python dictionary.
dump() - It dumps python dictionary data into a file in a form of json string data.
"""
import json

Employee = """{
    "emp1":{
        "name":"Harry",
        "salary":500,
        "is_programmer":true
        },
    "emp2":{
        "name":"Naveen",
        "salary":400,
        "is_programmer":false
    }
}
"""

# print(type(Employee))
# print(Employee)

# python_dict = json.loads(Employee)
# print(type(python_dict))

# print(python_dict)

# new_json_string = json.dumps(python_dict,indent=2)

# print(type(new_json_string))
# print(new_json_string)

# with open("json_data","wt") as f:
#     json.dump(python_dict,f,indent=2)

# with open("json_data","rt") as f:
#     python_dictionary = json.load(f)
# print(python_dictionary)


# We have one external module which is used for text to speech called pywin32

# from win32com.client import Dispatch

# text = "Once upon a time there was a king called Ashoka"


# def speech(text):
#     speaker = Dispatch("SAPI.SpVoice")
#     speaker.speak(text)
# speech(text)


# Akbhar padhke sunao using newsapi.org

import requests
import os
from win32com.client import Dispatch

r = requests.get(os.environ.get('NEWSPAPER_API'))

# print(type(r.text))

# python_dict = json.loads(r.text)

# print(type(python_dict))
# print(python_dict)

# python_dict = json.loads(r.text)

# for item in range(5):
#     print(f"Headline number: {item + 1}")
#     print("Title:",python_dict["articles"][item]["title"])
#     print("Description:",python_dict["articles"][item]["description"])
#     print()


python_dict = json.loads(r.text)

def text1_to_speech(text1):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.speak(text1)

def text2_to_speech(text2):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.speak(text2)

def text3_to_speech(text3):
    speaker = Dispatch("SAPI.SpVoice")
    speaker.speak(text3)


for item in range(5):
    text1_to_speech(f"Headline number: {item + 1}")
    text2_to_speech(python_dict["articles"][item]["title"])
    text3_to_speech(python_dict["articles"][item]["description"])
    






















