# String Formatting - It is a way by which we can add variable within a string.

# var = "king"

# a = "Once upon a time there was a %s called Ashoka !"%var
# print(a)

# var1 = "king"
# var2 = "time"

# a = "Once upon a %s there was a %s called Ashoka"%(var2,var1)
# print(a)

# var1 = "king"
# var2 = "time"

# a = "Once upon a {} there was a {} called Ashoka"
# formatted_string = a.format(var2,var1)
# print(formatted_string)


# Best string formatting technique is fstring

var1 = "king"
var2 = "time"

print(f"Once upon a {var2} there was a {var1} called Ashoka !")

