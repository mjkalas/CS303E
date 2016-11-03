# File: Deal.py
# Description:
# Student Name: Minal Kalas
# Student UT EID: mjk863
# Course Name: CS 303E
# Unique Number: 50475
# Date Created: 10/05/15
# Date Last Modified: 10/07/15

import random

def main ():
    num_trials = int (input("Enter number of times you want to play:"))
    print('')
    count = 0
    success = 0
    print ("Prize      Guess      View    New Guess")
    for i in range (0, num_trials + 1):
        prize = random.randint(1, 3)
        guess = random.randint(1, 3)
        view = random.randint(1, 3)
        while (view == prize) or (view == guess):
                view = random.randint(1, 3)
        newGuess = random.randint(1, 3)
        while (newGuess == view) or (newGuess == guess):
            newGuess = random.randint(1, 3)
        print (" ", (prize), "        ", (guess), "       ", (view), "       ", (newGuess))
        if newGuess == prize:
            success += 1
        count += 1

    probability_win = round ((success/num_trials), 2)
    no_switch_probability_win = format ((1-probability_win), ".2f")

    print ('')
    print ("Probability of winning if you do switch =", probability_win)
    print ("Probability of winning if you do not switch =", no_switch_probability_win)
main ()
