print('Sun = 0, Mon = 1, Tues = 2, Wed = 3, Thurs = 4, Frid = 5, Sat = 6')
currentDay = eval(input('Enter today\'s day: '))
elapsedDays = eval(input('Enter the number of days elapsed since today\'s day: '))
futureDay = (currentDay + elapsedDays) % 7
if currentDay == 0:
    day = 'Sunday'
elif currentDay == 1:
    day = 'Monday'
elif currentDay == 2:
    day = 'Tuesday'
elif currentDay == 3:
    day = 'Wednesday'
elif currentDay == 4:
    day = 'Thursday'
elif currentDay == 5:
    day = 'Friday'
else:
    day = 'Saturday'
if futureDay == 0:
    fday = 'Sunday'
elif futureDay == 1:
    fday = 'Monday'
elif futureDay == 2:
    fday = 'Tuesday'
elif futureDay == 3:
    fday = 'Wednesday'
elif futureDay == 4:
    fday = 'Thursday'
elif futureDay == 5:
    fday = 'Friday'
else:
    fday = 'Saturday'
print(f'Today is {day} and the future day is {fday}')