speed, acceleration = eval(input('Enter the speed and acceleration: '))
runwayLength = (speed ** 2) / (2 * acceleration)
runwayLength = round(runwayLength, 3)
print('The minimum runway length for this airplane is', runwayLength, 'meters')
# If the thousandths place is 0, it doesn't print