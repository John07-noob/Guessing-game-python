# This project created by John07-noob
# Sep/13/2020

import random

print("Welcome to The Number Guessing Game")
print("You have 7 Guess only.")
random_number = random.randint(1, 20)
for i in range(7):
    answer = int(input("Try to Guess: "))
    if answer < random_number:
        print("To Low")
    elif answer > random_number:
        print("To High")
    elif answer == random_number:
        print(f"Good job.. you found number {random_number}")
        break
