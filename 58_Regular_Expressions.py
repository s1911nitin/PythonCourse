"""
We can parse a few lines of string using slicing but it would be difficult for use if
we have a long text file or string suppose 1000 of words in a text file.

So, we have one concept called regular expression which is used to get useful information
from a long string or a long text file.

We have one inbuilt module called re in python to use regular expression.
"""

import re

text_to_search = """
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890

Ha HaHa

_

Meta characters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( ) 

coreyms.com

CoreyMSchafer@gmail.com
corey.schafer@university.edu
corey-321-schafer@my-work.net

321-555-4321
123.555.1234
231*444*3421
810-444-3421
900-444-3421
543--32-2341
657**45*3241
854..23.7652

cat
mat
pat
bat

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
"""

Sentence = "Start a sentence and then bring it to an end"

url ="""
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
"""

# pattern = re.compile(r'def')
# pattern = re.compile(r'DCB')
# pattern = re.compile(r'.')
# pattern = re.compile(r'\.')
# pattern = re.compile(r'\d')
# pattern = re.compile(r'\D')
# pattern = re.compile(r'\w')
# pattern = re.compile(r'\W')
# pattern = re.compile(r'\s')
# pattern = re.compile(r'\S')
# pattern = re.compile(r'\bHa')
# pattern = re.compile(r'Ha\b')
# pattern = re.compile(r'coreyms\.com')
# pattern = re.compile(r'\d\d\d.\d\d\d.\d\d\d\d')
# pattern = re.compile(r'\d\d\d[.*]\d\d\d[.*]\d\d\d\d')
# pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')
# pattern = re.compile(r'\d{3}[-]\d{3}[-]\d{4}')
# pattern = re.compile(r'\d{3}[.*-][.*-]\d{2}.\d{4}')
# pattern = re.compile(r'[89]\d{2}.\d{3}.\d{4}')
# pattern = re.compile(r'[\w.-]+@[\w-]+\.(com|edu|net)')
# pattern = re.compile(r'[^b]at')
# pattern = re.compile(r'M(r|s|rs)\.?\s\w+')

# pattern = re.compile(r'M(r|s|rs)\.?\s\w+')

# matches = pattern.finditer(text_to_search)

# for match in matches:
#     print(match)


# pattern = re.compile(r'^Start')
# pattern = re.compile(r'end$')

# matches = pattern.finditer(Sentence)

# for match in matches:
#     print(match)

# pattern = re.compile(r'https?://(www.)?\w+(.com|.gov)')
# pattern = re.compile(r'(https?://)((www.)?)(\w+(.com|.gov))')

# matches = pattern.finditer(url)

# for match in matches:
#     print(match)

pattern = re.compile(r'https?://(www.)?(\w+\.)(com|gov)')

# matches = pattern.finditer(url)

# for match in matches:
#     print(match)

# matches = pattern.finditer(url)

# for match in matches:
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))

sub_pattern = pattern.sub(r'\2\3',url)
print(sub_pattern)















