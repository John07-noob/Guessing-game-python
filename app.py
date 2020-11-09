"""
Author     : John07-noob
Date       : Sep/13/2020
LastUpdate : Nov/10/2020
"""
import random

def inputNumber(number):
    while True:
        try:
            userInput = int(input(number))
        except ValueError:
            print("Not an Interger! Try Again")
            continue
        else:
            return userInput
            break

if __name__=='__main__':
    print("Welcome to The Number Guessing Game")
    print("Guess the number between 1~20")
    print("You have 7 Guess only.")
    random_number = random.randint(1, 20)
    for i in range(7):
        answer = inputNumber("Try to Guess: ")
        if answer < random_number:
            print("To Low")
        elif answer > random_number:
            print("To High")
        elif answer == random_number:
            print(f"Good job.. you found number {random_number}")
            break
