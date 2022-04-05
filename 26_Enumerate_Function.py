"""
Enumerate Function - This is built in function which is used for conveniance purpose.

It gives indexing which always starts from 0 and increment it automatically so we do 
not need to initialize variable and increment it manually by writing a code.

"""

List = ["Brinjal","Cabbage","Carrot","Potato","Jake Fruit","Raddish"]

# i = 0
# for item in List:
#     if i%2 !=0:
#         print(item, end=" ")
#     i+=1

for index, item in enumerate(List):
    if index%2 ==0:
        print(item, end=" ")
