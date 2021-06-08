'''
number = eval(input())
binary = []

while number > 1:
    toList = number % 2
    binary.append(toList)
    number //= 2

binary.append(number)
binary = [i for i in reversed(binary)]

print(*binary, sep = '')
'''

number = eval(input())
binary = []

while number != 0:
    toList = number % 2
    binary.insert(0, toList)
    number //= 2
    print(number, toList)

print(*binary, sep = '')