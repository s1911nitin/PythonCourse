
# Dictionary - It is a datatype which holds the items in a pair of keys and values and it is denoted by {}.

d1 = {
    "Harry":2,
    "Carry":4,
    "Larry":8,
    "Cherry":16
}

# print(type(d1))
# print(d1)

# d1[420] = "Prantha"
# print(d1)

# del d1["Carry"]
# print(d1)

# d1.update({"Sherry":32})
# print(d1)

# print(d1["Sherry"])
# print(d1.get("Larry"))

# print(d1["Merry"])        # KeyError: 'Merry'

# print(d1.get("Merry","Not Available"))  # If key does not exist so default is None however we can set it by a string.


# d2 = d1.copy()

# del d2["Carry"]

# print(d1, d2)

d3 = {
    "Nitin":"Rajma",
    "Pandey":"Chole Bhature",
    "Piyush":"Amritsari Naan",
    "Joginder":"Churma"
}

d3.update({"Shivpal":{"B":"Dosa","L":"Dal Rice","Dinner":"Salad"}})

# print(d3)
# print(d3["Shivpal"]["L"])
# print(d3.get("Shivpal").get("Dinner"))
# print(d3.get("Shivpal")["B"])


# Write a program to get the meaning of a word from a given dictionary using user defined input as a word ?

dict1 = {
    "Destroy":"Todna",
    "Abandon":"Radh",
    "Sweet":"Meetha",
    "Tangy":"Khatha"
}

print("We have an oxford dictionary having words : Destroy, Abandon, Sweet, Tangy \n")
n1 = input("Enter the word for a meaning: \n")
print("Meaning of your word:",dict1.get(n1))



