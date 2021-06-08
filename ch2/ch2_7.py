minute = eval(input('Enter the number of minutes: '))
year = minute // 525600
day = minute % 525600 // 1440
print(minute, 'minutes is approximately', year, 'years and', day, 'days')