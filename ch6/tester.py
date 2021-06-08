import myFunctions

number = eval(input('Celcius to fahrenheit: '))
print(myFunctions.celciusToFahrenheit(number))

number = eval(input('Fahrenheit to celcius: '))
print(myFunctions.fahrenheitToCelcius(number))

number = eval(input('Feet to meters: '))
print(myFunctions.feetToMeter(number))

number = eval(input('Meters to feet: '))
print(myFunctions.meterToFeet(number))

number = eval(input('Sum of digits: '))
print(myFunctions.sumDigits(number))

number = eval(input('Reverse: '))
print(myFunctions.reverse(number))

number = eval(input('Palindrome test: '))
print(myFunctions.isPalindrome(number))

p, r, m, t = eval(input('Principle, rate, compound, years: '))
print(myFunctions.futureValue(p, r, m, t))