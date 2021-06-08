import random
while True:
    num1 = random.randint(0, 10)
    num2 = random.randint(0, 10)
    answer = eval(input(f'{num1} + {num2} = ?'))
    key = num1 + num2
    if answer == key:
        print('Correct answer!')
    else:
        print('Incorrect answer.')
    repeat = input('Would you like to try again? (y/n): ')
    if repeat == 'n':
        break