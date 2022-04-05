# Snake Water Gun Game Development -

import random

List = ["Snake","Water","Gun"]

tie_count = 0
user_count = 0
computer_count = 0
turns = 1

while(True):
    user_choice = input("Choose Snake or Water or Gun \n")
    computer_choice = random.choice(List)
    if user_choice == "Snake" and computer_choice == "Snake":
        print("Tie breaker")
        tie_count+=1
    elif user_choice == "Snake" and computer_choice == "Water":
        print("User Won")
        user_count+=1
    elif user_choice == "Snake" and computer_choice == "Gun":
        print("Computer Won")
        computer_count+=1
    elif user_choice == "Water" and computer_choice == "Water":
        print("Tie breaker")
        tie_count+=1
    elif user_choice == "Water" and computer_choice == "Snake":
        print("Computer Won")
        computer_count+=1
    elif user_choice == "Water" and computer_choice == "Gun":
        print("User Won")
        user_count+=1
    elif user_choice == "Gun" and computer_choice == "Gun":
        print("Tie breaker")
        tie_count+=1
    elif user_choice == "Gun" and computer_choice == "Snake":
        print("User Won")
        user_count+=1
    elif user_choice == "Gun" and computer_choice == "Water":
        print("Computer Won")
        computer_count+=1
    print("Number of turns left:", 5-turns)
    turns+=1
    if turns == 6:
        print("Game Over \n")
        print(f"User Won: {user_count}, Computer Won: {computer_count}, Tie Breaker: {tie_count}")
        break
    



