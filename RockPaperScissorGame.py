import random
import time
from simple_chalk import green, red, yellow


def RPSGame():
    rounds = input('How many rounds do you want to play? ')
    while not rounds.isdigit():
        print('Your input is invalid Please try again.')
        print('Please Reenter The amount of rounds you want to play: ')
    rounds = int(rounds)
    u = 0
    c = 0
    t = 0
    for x in range(rounds):
        computerChoice = ['r', 'p', 's']
        computerChoice = random.choice(computerChoice)
        userChoice = input('Do you choose Rock = R, Paper = P, Or Scissors = S? ')
        userChoice = userChoice.lower()
        while userChoice not in ('r', 'p', 's'):
            print('')
            print('Please enter R, P, or S. ')
            userChoice = input('Reenter R, P, or S: ')

        if computerChoice == 'r':
            computerChoicePrint = 'Rock'
        elif computerChoice == 'p':
            computerChoicePrint = 'Paper'
        else:
            computerChoicePrint = 'Scissors'

        print('The Computer chose ' + computerChoicePrint)
        if computerChoice == 'r' and userChoice == 'r':
            print('')
            print(yellow("Tie..."))
            print('')
            t+=1
        elif computerChoice == 'r' and userChoice == 'p':
            print('')
            print(green('User Wins Round.'))
            print('')
            u+=1
        elif computerChoice == 'r' and userChoice == 's':
            print('')
            print(red('Computer Wins Round.'))
            print('')
            c+=1
        elif computerChoice == 'p' and userChoice == 'r':
            print('')
            print(red('Computer Wins Round.'))
            print('')
            c+=1
        elif computerChoice == 'p' and userChoice == 'p':
            print('')
            print(yellow("Tie..."))
            print('')
            t+=1
        elif computerChoice == 'p' and userChoice == 's':
            print('')
            print(green('User Wins Round.'))
            print('')
            u+=1
        elif computerChoice == 's' and userChoice == 'r':
            print('')
            print(green('User Wins Round.'))
            print('')
            u+=1
        elif computerChoice == 's' and userChoice == 'p':
            print('')
            print(red('Computer Wins Round.'))
            print('')
            c+=1
        elif computerChoice == 's' and userChoice == 's':
            print('')
            print(yellow("Tie..."))
            print('')
            t+=1
        else:
            print("I'm Sorry. Something Went Wrong. The game closed.")
            exit()
    u = str(u)
    c = str(c)
    t = str(t)
    print('User is ' + u)
    print('Computer is ' + c)
    print('Ties are ' + t)
    if (u == c):
        print(yellow.bold('The final Score is Tie'))
    elif (u > c):
        print(green.bold('User Wins'))
    else:
        print(red.bold('Computer Wins'))
    print('Game Ended.')
    endAction = input('If you want to play again, press P, and if you want to exit press X. ')
    endAction = endAction.lower()
    while endAction not in ('p', 'x'):
        print('')
        print('Please enter P, or X. ')
        endAction = input('Reenter P, or X. ')
    endAction = endAction.lower()
    if endAction == 'p':
        for y in range(5):
            time.sleep(0.15)
            print('')
            time.sleep(0.15)
        RPSGame()
    elif endAction == 'x':
        exit()
    else:
        print("I'm Sorry. Something Went Wrong. The game is closed.")
        exit()
RPSGame()