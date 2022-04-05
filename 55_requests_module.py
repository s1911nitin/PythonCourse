"""
requests - It is an external python module which is used to get the content of a web page unicode
or image content in terms of bytes.

It is also known as HTTP for Humans

It is very useful if we want some of the content which are available on internet like webpage into our
python program.
"""

import requests

r = requests.get("https://xkcd.com/353/")

# print(r)
# print(type(r.text))
# print(r.text)
# print(r.status_code)

# r = requests.get("https://xkcd.com/353/450")

# print(r.status_code)

# r = requests.get("https://imgs.xkcd.com/comics/python.png")

# with open("comic.jpg","wb") as f:
#     f.write(r.content)

# payload = {"page":2,"count":4}
# r = requests.get("https://httpbin.org/get",payload)
# print(r.text)

# payload = {"username":"Naveen","password":"DUBAI2021"}
# r = requests.post("https://httpbin.org/post",payload)
# print(r.text)
# print(r.headers)


# r = requests.get("https://httpbin.org/basic-auth/Naveen/Dubai",auth=("Naveen","Dubai"))
# print(r.text)