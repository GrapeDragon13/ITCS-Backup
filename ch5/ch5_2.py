accumulate = 0
num1 = 1
while num1 != 0:
    num1 = eval(input('Enter an integer, "0" will exit: '))
    accumulate += num1
print(f'{accumulate} accumulated value')