def celciusToFahrenheit(number):
    fahrenheit = (9 / 5) * number + 32
    return fahrenheit

def fahrenheitToCelcius(number):
    celcius = (5 / 9) * (number - 32)
    return celcius

def feetToMeter(number):
    meter = number / 3.281
    return meter

def meterToFeet(number):
    feet = number * 3.281
    return feet

def sumDigits(number):
    total = 0
    for i in str(number):
        total += int(i)
    return total

def reverse(number):
    digits = []
    for digit in range(len(str(number))):
        digits.append(number % 10)
        number //= 10
    output = ''
    for each in digits:
        output += str(each)
    return int(output)

def isPalindrome(number):
    if number == reverse(number):
        return True
    else:
        return False

def futureValue(p, r, m, t):
    interest = (r * 0.01) / m
    periods = t * m
    futureValue = p * ((1 + interest) ** periods)
    return futureValue