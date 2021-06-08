amountOfWater = eval(input('Enter the amount of water in kilograms: '))
initialTemerature = eval(input('Enter the initial temerature: '))
finalTemperature = eval(input('Enter the final temperature: '))
energy = amountOfWater * (finalTemperature - initialTemerature) * 4184
energy = round(energy, 1)
print('The energy needed is', energy)