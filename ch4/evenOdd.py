number = eval(input('Enter a number: '))
evenOdd = number % 2
if evenOdd == 0:
    print(f'{evenOdd} is an even number.')
else:
    print(f'{evenOdd} is an odd number.')