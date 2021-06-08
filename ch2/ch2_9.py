initialTemperature = eval(input('Enter the temperature in Fahrenheit between -58 and 41: '))
windSpeed = eval(input('Enter the wind speed in miles per hour: '))
windChill = 35.74 + 0.621 * initialTemperature - 35.75 * windSpeed ** 0.16 + 0.4275 * initialTemperature * windSpeed ** 0.16
windChill = round(windChill, 5)
print('The wind chill index is', windChill)
'''
When the 5th decimal place is 0, the program doesn't display that 0.
However, the other way of making this program I found is this: print(f'The wind chill index is {windChill:.7}')
in place of the current line 5 with the current line 4 removed. This way I found is not as reliable.
'''