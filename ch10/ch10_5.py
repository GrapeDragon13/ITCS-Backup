numbers = input('Enter ten numbers (0-9): ').split()
numbers = list(map(int, numbers))
numbers.sort()
numbers = list(map(str, numbers))
unique = ''
for i in numbers:
    if i not in unique:
        unique += ' ' + i
print(f'the distinct numbers are{unique}')