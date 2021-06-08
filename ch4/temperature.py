celciusFahrenheit = input('Would you like to convert to Celcius or Fahrenheit (C or F)? ')
temperature = eval(input('Enter the temerature you would like to convert: '))
if celciusFahrenheit == 'C':
    converted = (temperature - 32) * (5/9)
else:
    converted = temperature * (9/5) + 32
print(converted)