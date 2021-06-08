word = list(input(''))
print(*word, sep='')

if len(word) % 2 == 1:
    del word[len(word) // 2]

first = word[:len(word) // 2]
second = word[len(word) // 2:]

#set of the list to delete duplicate items, find the highest count of occurrences of each element, do for each half and use return to count from list

firstMax = first.count(max(set(first), key = first.count))
secondMax = second.count(max(set(second), key = second.count))

if firstMax > secondMax:
    print('RIGHT UNBALANCED')
elif firstMax < secondMax:
    print('LEFT UNBALANCED')
else:
    first.sort()
    second.sort()

    if first == second:
        print('PERFECTLY BALANCED')
    else:
        print('BALANCED')

'''
word = list(input(''))
print(*word, sep='')
if len(word) % 2 == 1:
    del word[len(word) // 2]
first, second = word[:len(word) // 2], word[len(word) // 2:]
firstMax, secondMax = first.count(max(set(first), key = first.count)), second.count(max(set(second), key = second.count))
print('RIGHT UNBALANCED') if firstMax > secondMax else (print('LEFT UNBALANCED') if firstMax < secondMax else first.sort(), second.sort(), print('PERFECTLY BALANCED') if first == second else print('BALANCED'))
'''