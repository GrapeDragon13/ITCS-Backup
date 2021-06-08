# brute force method 1, working on more intelligent method
def permute(l, wordList, setList, mathList):
    combination = list(map(str, l))
    start = 0
    end = len(setList)

    while True:
        save = combination[start:end]
        testDictionary = dict(zip(setList, save))
        mathSave = []

        for word in wordList:
            mathSave.append(''.join(testDictionary.get(ele, ele) for ele in word))

        if int(mathSave[0]) + int(mathSave[1]) == int(mathSave[2]) and mathSave not in mathList:
            print(mathSave[0], '+', mathSave[1], '=', mathSave[2])
            mathList.append(mathSave)

        if end == 10:
            break

        start += 1
        end += 1


def main():
    letter1, letter2, letterSolution = input().split()
    print(letter1, letter2, letterSolution)
    wordList = [letter1.lower(), letter2.lower(), letterSolution.lower()]
    setList = list(set(''.join(wordList)))

    if len(setList) > 10:
        print('Too many unique letters.')
    else:
        mathList = []

        l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        c = len(l) * [0]
        permute(l, wordList, setList, mathList)
        i = 0

        while i < len(l):
            if c[i] < i:
                if i % 2 == 0:
                    tmp = l[0]
                    l[0] = l[i]
                    l[i] = tmp
                else:
                    tmp = l[c[i]]
                    l[c[i]] = l[i]
                    l[i] = tmp
                permute(l, wordList, setList, mathList)
                c[i] += 1
                i = 0
            else:
                c[i] = 0
                i += 1

        '''
        sortMathList = []

        for math in mathList:
            sortMathList.append(math[2])

        sortMathList.sort()
        print(*sortMathList, sep = ', ')
        '''
# sort lists to not print duplicates with reverse operator, possible to make other operators besides '+'?

main()