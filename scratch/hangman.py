import random
import os


R = '\033[0;31m'
BR = '\033[1;31m'
G = '\033[0;32m'
BG='\033[1;32m'
Y='\033[0;33m'
X='\033[0m'


def termSelection():
    myFile = open('terms.txt', 'r')
    term = myFile.read().split('\n')
    myFile.close()
    
    term = random.choice(term)

    return term


def cutTerm(term):
    define, definition = term.split('-', 1)

    return define, definition


def fillGallows(wrongGuesses):
    parts = 'O|/\/\ '
    fill = '      '

    for p, f, i in zip(parts, fill, range(wrongGuesses)):
        replace = ''
        replacement = ''
        replace = f
        replacement = p
        fill = fill.replace(replace, replacement, 1)

    gallows = f'{Y}|-----|\n|     {R}{fill[0]}{Y}\n|    {R}{fill[2]}{fill[1]}{fill[3]}{Y}\n|    {R}{fill[4]} {fill[5]}{Y}\n--------{X}'

    return gallows


def testGuess(guessed, guess):
    if guess not in guessed and guess.isalpha() and len(guess) == 1:
        guessed += guess

    guessed = ''.join(sorted(guessed))

    return guessed


def findCorrect(define, guessed):
    testReturn = ''

    for character in define:
        if character in guessed:
            testReturn += character
        else:
            testReturn += '-'

    return testReturn


def main():
    score = 0
    breakTest = True

    while breakTest:
        term = termSelection()
        define, definition = cutTerm(term)
        guessed = ''
        correct = findCorrect(define, guessed)
        wrongGuesses = 0
        gallows = fillGallows(wrongGuesses)

        while True:
            os.system('clear')

            if '-' not in correct:
                score += 10
                print(f'{BG}|-----|\n|\n|    \O/\n|     |\n-----/-\ \nYou win!{X}')
                break
            elif wrongGuesses == 7:
                score -= 10
                print(f'     {BR}_______________\n    |_______________``\ \n     [/]           [  ]\n     [\]           |  |\n     [/]           |  |\n     [\]           |  |\n     [/]           || |\n    [---]          |  |\n    [---]          |@ |\n    [---]          |  |\n   oOOOOOo         |  |\n  oOO`./OOo        | @|\n oO| X  X|Oo       |  |\n OO|  ¿ ` OO       |  |\n/*O \ ── /O*\      |  |\n   *O`--`O*  |     |  |\n  |       |  |     | ||\n  |       |  |_____| ||__\n _/_______\__|  \  ||||  \ \n /         \_|\  _ | ||\  \ \n |    V    |\  \//\  \  \  \ \n |    |    | __//  \  \  \  \ \n |    |    |\|//|\  \  \  \  \ \n ------------\--- \  \  \  \  \ \n \  \  \  \  \  \  \  \  \  \  \ \n _\__\__\__\__\__\__\__\__\__\__\ \n __|__|__|__|__|__|__|__|__|__|__|\n |___| |___| \n |###/ \###|\n \##/   \##/\n  ``     ``\nYou lose.{X}')
                break

            print(gallows)
            print(f'Definition: {Y}{definition}{X}')
            print(f'Correct: {G}{correct}{X}')
            print(f'Guessed: {Y}{guessed}{X}')
            print(f'Score: {Y}{score}{X}')

            guess = input('Guess a letter: ')

# possible to change here to not punish for not alnum or repeat guess

            guessed = testGuess(guessed, guess)

            if guess in define:
                score += 1
                correct = findCorrect(define, guessed)
            else:
                score -= 1
                wrongGuesses += 1
                gallows = fillGallows(wrongGuesses)

        while True:
            repeat = input('Would you like to play again? (y/n): ')

            if repeat == 'y':
                break
            elif repeat == 'n':
                breakTest = False
                break

main()