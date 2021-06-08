import random

def sumOfRoll(numOfDice):
    total = 0
    for roll in range(numOfDice):
        dice = random.randint(1, 6)
        total += dice
    return total

def evalSum(roll):
    if roll == 7 or roll == 11:
        return 'natural'
    elif roll == 2 or roll == 3 or roll == 12:
        return 'craps'
    else:
        return evalPoint(roll)

def evalPoint(point):
    while True:
        roll = sumOfRoll(2)
        if roll == point:
            return 'point'
        elif roll == 7:
            return 'seven'
        else:
            continue

roll = sumOfRoll(2)

trial = eval(input('enter the number of trials: '))

success = 0
natural = 0
point = 0
seven = 0
craps = 0

for sample in range(trial):
    roll = sumOfRoll(2)
    outcome = evalSum(roll)
    if outcome == 'natural':
        natural += 1
        success += 1
    elif outcome == 'point':
        point += 1
        success += 1
    elif outcome == 'craps':
        craps += 1
    else:
        seven += 1

print(f'{natural} naturals out of {trial}: {natural / trial:.1%}')
print(f'{point} naturals out of {trial}: {point / trial:.1%}')
print(f'{craps} naturals out of {trial}: {craps / trial:.1%}')
print(f'{seven} naturals out of {trial}: {seven / trial:.1%}')
print(f'{success} naturals out of {trial}: {success / trial:.1%}')