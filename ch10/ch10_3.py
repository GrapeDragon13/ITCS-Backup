integers = input('Enter integers: ').split()
integers = list(map(int, integers))
numbers = []
for i in integers:
    if i not in numbers:
        numbers.append(i)
numbers.sort()
for i in numbers:
    count = integers.count(i)
    if count == 1:
        print(f'{i} occurs 1 time')
    else:
        print(f'{i} occurs {count} times')