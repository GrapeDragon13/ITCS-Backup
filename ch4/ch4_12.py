integer = eval(input('Enter an integer: '))
d5 = integer % 5
d6 = integer % 6
if d5 == 0 and d6 == 0:
    print(f'{integer} is divisible by 5 and 6')
elif d5 != 0 and d6 != 0:
    print(f'{integer} is not divisible by 5 or 6')
elif d5 == 0:
    print(f'{integer} is divisible by 5')
else:
    print(f'{integer} is divisible by 6')