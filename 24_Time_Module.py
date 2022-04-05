
import time

# print(time.time())  # It finds out the time travel in secs or ticks from some old day.

# Write a program to find out the execution time of our program ?

# initial_time = time.time()
# for item in range(11):
#     print(item)
# current_time = time.time()
# print("Program execution time:",(current_time-initial_time))

# def func(val):
#     print("Real code means val value will return after 5 seconds.")
#     time.sleep(5)
#     print(val)
# func("Nitin is using python programming.")

print("Human Readable Time:",time.asctime(time.localtime(time.time())))