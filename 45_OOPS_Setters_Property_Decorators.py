
class Employee:
    leaves = 10

    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{fname}.{lname}@gmail.com"

    @property
    def email(self):
        if self.fname == None and self.lname == None:
            return("Please use setter to set an email attribute....")
        else:
            return(f"{self.fname}.{self.lname}@gmail.com")

    @email.setter
    def email(self,string):
        new_string = string.split("@")[0]
        self.fname = new_string.split(".")[0]
        self.lname = new_string.split(".")[1]

    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None



harry = Employee("Hindustani","supporter")

# print(harry.email)
# harry.fname = "US"
# print(harry.fname)
# print(harry.email)

# print(harry.email())
# harry.fname = "US"
# print(harry.email())

# print(harry.email)
# harry.fname = "US"
# print(harry.email)

# harry.email = "this.that@gmail.com"
# print(harry.email)

# del harry.email
# print(harry.email)

# harry.email = "that.this@gmail.com"
# print(harry.email)




# Object Introspection-  Detailing of an object is known as Object Introspection.

# print(id(harry))
# print(dir(harry))
