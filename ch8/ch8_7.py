def getNumber(uppercaseLetter):
    numberPad = [('1voicemail'), ('2ABC'), ('3DEF'), ('4GHI'), ('5JKL'), ('6MNO'), ('7PQRS'), ('8TUV'), ('9WXYZ'), ('0 ')]
    pad = 0
    for number in numberPad:
        if uppercaseLetter in numberPad[pad]:
            return (numberPad[pad][0])
        pad += 1
    else:
        return 'error'


def main():
    uppercaseLetter = input('Enter an uppercase letter: ')
    print(getNumber(uppercaseLetter))


main()