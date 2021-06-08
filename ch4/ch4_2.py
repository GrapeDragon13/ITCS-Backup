import random
n1 = random.randint(0,9)
n2 = random.randint(0,9)
n3 = random.randint(0,9)
userAnswer = eval(input(f'What is {n1} + {n2} + {n3}?'))
answer = n1 + n2 + n3
if answer == userAnswer:
    print(f'{n1} + {n2} + {n3} = {userAnswer} is True')
else:
    print(f'{n1} + {n2} + {n3} = {userAnswer} is False')