# import random library
import random

# generate random number
genNum = random.randrange(1, 100)
# initialize bool to test if game condition has been met
correctGuess = False
# print instructions
print("Welcome to the number guessing game! We've generated a number between 0 and 100.")
# create while loop containing game function
while not correctGuess:
    userGuess = input("Please enter your guess: ")
    userGuessToInt = int(userGuess)

    if userGuessToInt > genNum:
        print("The generated number is lower.")
    elif userGuessToInt < genNum:
        print("The generated number is higher.")
    else:
        print("Spot on! You guessed it!")
        correctGuess = True

