#!/usr/bin/python3
#Blake Miller
#ILS-Z399
#02 : Guess the Number
# Fulfills requirements for the Guess the Number assignment
# Creativity: does not use while loop, shows when player is close

import sys, random

assert sys.version_info >= (3,4), "This script requires at least Python 3.4"

#variables
guesses = 10
guess_range = 20
#epsilon: distance for "large difference"
epsilon = 4


#generate a random integer between 1 and 20 (inclusive)...
# and store it in the variable [number]
number = random.randint(1,guess_range)


# Here, I define "coreGame," the core loop of the game
def coreGame(number, guesses):
    if guesses <= 0: #when you are finished with guessing
        print("You lose! The number was " + str(number)) #Displays what the correct answer was
        
    else:
        
        try:
            print("Guess a number!",guesses,"guesses left!")
            guess = int(input())
            
            if guess == number:
                print("Correct!")
                #This is the only case without another call to the fn. Ends the run
                
            else:
                if abs(number - guess) <= epsilon: #If near to the guess
                    print("Close!") 
                if (number - guess) > 0:
                    print("Too low!")
                elif (guess - number) > 0:
                    print("Too high!")
                coreGame(number, guesses - 1) #Runs the game with one less guess, decrements til 0
                
                
        except ValueError:
            print("Please input a whole number.")
            coreGame(number, guesses) #Retries to run the game

coreGame(number, guesses) #This actually runs the game.
#Without the above line, nothing happens
#Runs using the initial values as defined above
