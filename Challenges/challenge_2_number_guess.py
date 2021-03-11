"""
Number guessing game
The number to guess will be from 1 to 20 (inclusive).
The user will have 4 guesses to guess the number correctly.
After each wrong guess, the user will be told whether to
guess higher or lower next time.
If the user doesn't win, tell them the number.
"""
import random


def run_game():
    answer = random.randint(1, 20)
    print("I'm thinking of a number between 1 and 20")

    count_number_of_tries =0
    while (count_number_of_tries <4):
        guess = int(input("Guess a number: "))
        if(guess==answer):
            print("You got it right")
            return
        elif(guess>answer):
            print("Guess lower")
        else:
            print("Guess higher")
        count_number_of_tries = count_number_of_tries+1
    print("the random number was "+str(answer))


run_game()
