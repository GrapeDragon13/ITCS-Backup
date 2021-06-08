import random

def generatePassword():
    myFile = open('descriptions.txt', 'r')
    descriptions = myFile.read().split('\n')
    myFile.close()

    myFile = open('things.txt', 'r')
    things = myFile.read().split('\n')
    myFile.close()

    password = random.choice(descriptions).capitalize() + random.choice(things).capitalize()

    return password


def cipher(password):
    specialLetter = ['a', 'i', 's']
    letterSpecial = ['@', '!', '$']
    specialNumber = ['e', 'l', 'o']
    numberSpecial = ['3', '1', '0']
    specialList = [specialLetter, specialNumber]
    letterNumberList = [letterSpecial, numberSpecial]
    beginningAdd = []
    
    for specials, numberLetters in zip(specialList, letterNumberList):
        replace = ''
        replacement = ''
        for i in password:
            breakTest = False
            for special, symbol in zip(specials, numberLetters):
                if special == i:
                    replace = special
                    replacement = symbol
                    password = password.replace(replace, replacement, 1)
                    breakTest = True

            if breakTest:
                break

    testLetter = True
    testNumber = True

    for letter, number in zip(letterSpecial, numberSpecial):
        if letter in password:
            testLetter = False

        if number in password:
            testNumber = False

    if testLetter:
        password = '&' + password

    if testNumber:
        password = password + '88'

    return password


def main():
    password = generatePassword()
    cipherPassword = cipher(password)

    print(cipherPassword)

main()