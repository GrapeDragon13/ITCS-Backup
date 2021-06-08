import random
import os


def createPuzzle(colors, rowLength, repeatLength):
    puzzle = []

    for i in range(rowLength):
        while True:
            color = random.choice(colors)

            if puzzle.count(color) < repeatLength:
                break

        puzzle.append(color)

    return puzzle


def checkAccuracy(guess, puzzle):
    R = '\033[0;31m'    # red
    W = '\033[0;37m'    # white
    X = '\033[0m'       # reset
    circle = '\u2B24'
    testList = []
    testList.extend(puzzle)
    testGuess = []
    testGuess.extend(guess)
    feedback = []

    for i in range(len(testGuess)):
        if testGuess[i] == testList[i]:
            testGuess[i] = 'Del'
            testList[i] = 'Del'
            feedback.append(f'{R}{circle}{X}')

    for i in range(testGuess.count('Del')):
        testGuess.remove('Del')

    testList = list(set(testList))

    for i in testList:
        if i in testGuess:
            feedback.append(f'{W}{circle}{X}')

    return feedback


def main():

    R = '\033[0;31m'    # red
    G = '\033[0;32m'    # green
    Y = '\033[0;33m'    # yellow
    B = '\033[0;34m'    # blue
    P = '\033[0;35m'    # purple
    A = '\033[0;36m'    # aqua
    W = '\033[0;37m'    # white
    X ='\033[0m'       # reset
    circle = '\u2B24'
    colors = ['R', 'G', 'Y', 'B', 'P', 'A']

    #while True:
    rowLength = eval(input('Enter length of puzzle: '))
    repeatLength = eval(input('Enter maximum repeat length. Must be at least 1: '))
        # 6 times repeat
    '''
        if 6 * repeatLength > rowLength:
            print('Impossible situation.')
        else:
            break
    '''
    puzzle = createPuzzle(colors, rowLength, repeatLength)
    #print(puzzle)
    formerGuesses = []
    formerFeedback = []

    while True:
        os.system('clear')
        print(f'All colors are: {R}R, {G}G, {Y}Y, {B}B, {P}P, {A}A{X}\n====================')
        print(f'Puzzle length is {rowLength}.\n====================')
        print(f'Maximum repeat use of colors is {repeatLength}.\n====================')
        if len(formerGuesses) != 0:
            print('Previous guesses:')

            for i in range(len(formerGuesses)):
                printGuessed = ' '.join(map(str, (formerGuesses[i])))
        
                print(f'Guess {i + 1}: {printGuessed}      {formerFeedback[i]}\n====================')

        while True:
            inputGuess = input(f'Enter your {rowLength} guesses: ')
            guess = inputGuess.split()

            if len(guess) == rowLength:
                break

        formerGuesses.append(guess)

        if guess == puzzle:
            print('You win!')
            break

        feedback = checkAccuracy(guess, puzzle)
        feedback = ' '.join(map(str, feedback))
        formerFeedback.append(feedback)

main()