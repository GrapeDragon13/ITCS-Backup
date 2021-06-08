import random
num1 = random.randint(0, 20)
num2 = random.randint(0, 20)
answer = eval(input(f'{num1} x {num2} = ? '))
key = num1 * num2
if answer == key:
    print('correct :)')
else:
    print('incorrect :(')
#So the grading rubric is just refusing to run this one for me.