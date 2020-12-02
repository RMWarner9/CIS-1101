"""
Rachel Warner
November 14th, 2020
Program Name: Guessing Game Modify
Project 3.3
Purpose of Program: Play a guessing game against the computer!
        There is no input value for the computer to compare numbers to.
        Cheating causes the computer to automatically win.
Output: The output will be the number the user guessed or a statement calling them a
        cheater.
"""
# import modules from libraries
from random import randint, choice
from math import log2

# set variables = 0
range_min = 0
range_max = 100
min_guess = range_min - 1
max_guess = range_max + 1
# text that will display if user is cheating
meanText = [
    "Cheaters never prosper. I win.",
    "Cheating isn't how we make friends. I win.",
    "Cheater, cheater, pumpkin eater. I win.",
    "Really? Cheating? This is supposed to be just a fun game... I win.",
]

selection = choice(meanText)

print(f"Think of a number between {range_min} and {range_max}. I will try to guess it.")
count = 0
possible_values = (range_max - range_min) + 1
min_guesses = round(log2(possible_values))
userAnswer = ""


def get_user_answer():

    # loop over until user gives valid input.
    # returns the imputed answer which should be H, Y, or L
    inputted_answer = ""
    while inputted_answer != "Y" and inputted_answer != "H" and inputted_answer != "L":
        inputted_answer = str.upper(
            input(
                f"If my guess is correct: Press Y \n"
                + f"If my guess is too high: Press H \n"
                + f"If my guess is too low: Press L \n"
            )
        )
        if inputted_answer != "Y" and inputted_answer != "H" and inputted_answer != "L":
            print("Please enter a valid input.")
    return inputted_answer


print("It should take me this many guesses:", min_guesses)
while userAnswer != "Y" and (count < min_guesses):
    count += 1
    # this sets the guess to the only remaining number if the
    # min_guess and max_guess are only separated by one digit
    if min_guess + 1 == max_guess - 1:
        # Game should win on next guess
        guess = min_guess + 1
    else:
        # guess is a random integer
        guess = randint(min_guess + 1, max_guess - 1)
    print("Is this your number?", guess)
    userAnswer = get_user_answer()
    # if answer is too high, max_guess is set to guess
    # also compares max_guess to guess and range_min to guess to find a cheater
    if userAnswer == "H":
        if max_guess == guess or range_min == guess:
            print(selection)
            userAnswer = "Y"
        else:
            max_guess = guess
    # the same logic is here except in reverse
    elif userAnswer == "L":
        if min_guess == guess or range_max == guess:
            print(selection)
            userAnswer = "Y"
        else:
            min_guess = guess
    # this prevents an off by one error when comparing odd numbers
    if min_guess + 1 > max_guess - 1:
        userAnswer = "Y"
        print(selection)

# outputs the amount of turns it took to win
if userAnswer == "Y":
    print(f"I won in {count} turns! \n ")
# outputs if computer failed to guess within minimum guesses
else:
    print(f"I failed to guess your number within {min_guesses} guesses")
