'''
allEmotions = ['se+', 'aggressiveness', 'at+', 'optimism', 'pl+', 'love', 'ap+', 'submission', 'se-', 'awe', 'at-', 'disapproval', 'pl-', 'remorse', 'ap-', 'contempt']
i1 = allEmotions[2]
i2 = allEmotions[2]
length1 = []
length2 = []
for i in range(allEmotions.index(i1), allEmotions.index(i2) + 1):
    length1.append(allEmotions[i])
#for i in reversed(range(allEmotions.index(i1), allEmotions.index(i2) + 1)):
for i in range(allEmotions.index(i1), allEmotions.index(i2) -(len(allEmotions) + 1), -1):
    length2.append(allEmotions[i])

if len(length1) <= len(length2):
    print(length1)
else:
    print(length2)
'''


import random
import time


def solveEquation(equation):
    solution = eval(equation)

    return solution


def generateProgramEmotions():
    programEmotions = []

    for i in range(4):
        programEmotions.append([random.randint(-3, 3) for i in range(4)])

    return programEmotions


def findOperationAmounts(equation):
    operations = ['+', '-', '*', '/']
    operationAmounts = []

    for operation in operations:
        operationAmounts.append(equation.count(operation))

    return operationAmounts


def findOperationPercentages(operationAmounts):
    operationTotal = 0
    operationPercentages = []

    for amount in operationAmounts:
        operationTotal += amount

    for amount in operationAmounts:
        if amount != 0:
            operationPercentages.append(amount / operationTotal * 100)

    return operationPercentages


def calculateDifficulty(equation, operationAmounts):
    #operationAmounts = [equation.count('+'), equation.count('-'), equation.count('*'), equation.count('/')]
    difficulty = 0
    repeat = 0
    multiplier = 1

    for amount in operationAmounts:
        difficulty += amount

    for i in equation:
        if i.isnumeric():
            repeat += 1
            multiplier += 0.1 * repeat
        else:
            repeat = 0

    difficulty = round(difficulty * multiplier)

    return difficulty


def calculateAptitude(emotionValues, operationAmounts):
    aptitude = 10

    for emotion in emotionValues:
        aptitude += (emotion[0])

    for emotion, amount in zip(emotionValues, operationAmounts):
        aptitude += amount * (emotion[0])

    return aptitude


def calculatePleasantness(emotionValues, operationAmounts):
    pleasantness = 0
    operationAmountTotal = 0

    for amount in operationAmounts:
        operationAmountTotal += amount

    for emotion, amount in zip(emotionValues, operationAmounts):
        pleasantness += amount * (emotion[1])

    if operationAmountTotal!= 0:
        pleasantness /= operationAmountTotal

    return pleasantness


def calculateAttention(emotionValues, operationAmounts):
    attention = 0

    for emotion in emotionValues:
        attention += (emotion[2])

    for emotion, amount in zip(emotionValues, operationAmounts):
        attention += amount * (emotion[2])

    attention /= 2

    return attention


def calculateSensitivity(emotionValues, operationAmounts, operationPercentages, pleasantness):
    sensitivity = []

    for i in range(4):
        sensitivity.append([])
        for j in range(4):
            sensitivity[i].append(0)

    for i in range(4):
        for j, percentage in zip(range(4), operationPercentages):
            if percentage != 0:
                sensitivity[i][j] += pleasantness / percentage / 4

    return sensitivity


def findAccuracy(solution, difficulty, aptitude):
    if aptitude < 0:
        return 'failure'

    percentError = 0

    if difficulty > aptitude:
        percentError += difficulty - aptitude / 4

    returnSolution = -(solution * percentError / 100 - solution)

    return returnSolution


def regulateValues(emotionValues, sensitivity):
    regulated = []
    maximum = 3
    minimum = -3

    for emotion, sense in zip(emotionValues, sensitivity):
        regulated.append([])
        for i in range(len(emotion)):
            append = emotion[i] + sense[i]

            if append > 3:
                append = 3
            elif append < -3:
                append = -3

            regulated[-1].append(append)

    return regulated


def createPureEmotions(alteredEmotions):
    pureEmotions = []

    for i in range(4):
        total = 0

        for emotion in alteredEmotions:
            total += emotion[i]
        pureEmotions.append(round(total / 4, 15))

    return pureEmotions


def findTime(difficulty, attention, pleasantness):
    time = 2 ** attention / 2 + 10

    if time > 60:
        time = 60

    if pleasantness > 0:
        time /= 2

    return time


def findMaxMin(pureEmotions):
    finalValues = [round(pureEmotions[1]), round(pureEmotions[2]), round(pureEmotions[0]), round(pureEmotions[3])]
    #print(finalValues)
# if 1, pass that emotion
# if 2, pass emotion between, "combination" emotion
# if 3, pass emotion in the middle, despite polarized emotion loop
# if 4, pass general emotion statement


    maxMin = max(max(finalValues), -min(finalValues))
    #print(maxMin)

    if maxMin == 0:
        print(f'Go ahead and crash. {0 / maxMin}')

    return maxMin, finalValues


def findSeparate(maxMin, finalValues):
    values = []
    place = []

    for i, j in zip(finalValues, range(4)):
        if abs(i) == maxMin:
            values.append(i)
            place.append(j)
# use values for extracting emotions from emotion lists to be used
# find general, then amp up intensity
    #print(values)
    #print(place)

    keyPositive = ['se+', 'at+', 'pl+', 'ap+']
    keyNegative = ['se-', 'at-', 'pl-', 'ap-']
    separateBy = []

    for i, j in zip(values, place):
        if i > 0:
            separateBy.append(keyPositive[j])
        elif i < 0:
            separateBy.append(keyNegative[j])
    '''
    print(separateBy)

    if len(separateBy) == 2:
        cutLength = 9
    else:
        cutLength = 5

    print(cutLength)
    '''

    return separateBy


    #separateBy = ['at+', 'ap-']
    # in this instance, 'at+' then needs to go to the back of the list to take the center of allEmotions for end emotion ^
    #separateBy = ['se-', 'at+', 'pl-']
    # in this instance, 'at+' is in between to sections that are being removed, it needs to be removed as well, it is completely opposite on the end emotion ^
    #separateBy = ['se+', 'pl+', 'ap-']
    # in this instance, 'ap-', 'contempt' need to go to the front of the list, section between that and the rest of the list is deleted ^
    #separateBy = ['se+', 'at+', 'pl-', 'ap+']
    # in this instance, 'pl-' to 'contempt' need to go to the front of the list, section between that and the rest of the list is deleted ^


def filterEmotion(separateBy, maxMin):
    allEmotions = ['se+', 'aggressiveness', 'at+', 'optimism', 'pl+', 'love', 'ap+', 'submission', 'se-', 'awe', 'at-', 'disapproval', 'pl-', 'remorse', 'ap-', 'contempt']

# 6, 4, 2, 4 max and right after, but long route to include all in separateBy
# 4, 6, 4, 2 same as above
# 2, 4, 6, 4 same as above
# 4, 2, 4, 6 same as above
# 10, 4, 2 max and right after, short route but includes all in separateBy
# 10, 2, 4 same as above
# 2, 10, 4 same as above
# 4, 10, 2 same as above
# 2, 4, 10 same as above
# 4, 2, 10 same as above
# 12, 2, 2 same as above
# 2, 12, 2 same as above
# 2, 2, 12  same as above
# 10, 2, 2, 2 same as above
# 2, 10, 2, 2 same as above
# 2, 2, 10, 2 same as above
# 2, 2, 2, 10 same as above
# 6, 4, 6 both max, long route to include all in separateBy, counts out at 5 so remove first max and all until second
# maybe remove it beforehand, test for distance to any other in separateBy and if it exceeds the count remove it ^ (theory)
# 6, 6, 4 same as above
# 4, 6, 6 same as above

    #print(allEmotions)
# start isolating at first feeling in separateBy, if feeling in seperateBy it gets it's own list to separated, end after len(separateBy) + 1 with list being created before it, accounting for wrap iteration

# test this: if item(s) at front of allEmotions not in separateBy, all items at the beginning up to first separateBy item are added to the back of separated list
    if len(separateBy) == 1:
        finalEmotion = separateBy[0]

    else:
        if len(separateBy) > 2:
            filteredEmotions = []

            for emotion in allEmotions:
                if emotion in separateBy:
                    filteredEmotions.append(emotion)

            separateBy = filteredEmotions
            print(separateBy)

            count = 0
            distance = 0
            distances = []

            while count < len(separateBy):
                for i in range(len(allEmotions)):
                    feeling = allEmotions[i % len(allEmotions)]

                    if feeling in separateBy:
                        if count > 0:
                            distances.append(distance)
                        distance = 0
                        count += 1

                    distance += 1

            testValue = allEmotions.index(separateBy[0])
            endValue = 0

            while True:
                testValue -= 1
                endValue -= 1

                if allEmotions[testValue] in separateBy:
                    break

            distances.append(abs(endValue))

            print(distances)

            i = 0

            # only need to test for an instance where the length is 3, and an item in separateBy is 5 away in both directions, if this is the case that item gets removed
            '''
            while True:
                testFirst = distances[i % len(distances)]
                testSecond = distances[i % len(distances) + 1]

                distanceTolerate = 2

                if len(separateBy) == 4:
                    distanceTolerate *= 2

                

            print(testFirst)
            print(testSecond)

            '''

        emotionPlace = []

        for i, j in enumerate(allEmotions):
            if j in separateBy:
                emotionPlace.append(i)

        #print(emotionPlace)
        #print(allEmotions)
        i1 = allEmotions[emotionPlace[0]]
        i2 = allEmotions[emotionPlace[-1]]
        length1 = []
        length2 = []
        for i in range(allEmotions.index(i1), allEmotions.index(i2) + 1):
            length1.append(allEmotions[i])

        #for i in reversed(range(allEmotions.index(i1), allEmotions.index(i2) + 1)):
        for i in range(allEmotions.index(i1), allEmotions.index(i2) -(len(allEmotions) + 1), -1):
            length2.append(allEmotions[i])

        if len(length1) <= len(length2):
            print(length1)
            allEmotions = length1
        else:
            print(length2)
            allEmotions = length2

        if len(allEmotions) % 2 == 0:
            finalEmotion = allEmotions[len(allEmotions) // 2 - 1]
        else:
            finalEmotion = allEmotions[len(allEmotions) // 2]
        #print(finalEmotion)

    return finalEmotion


def dictionaryAccessed(maxMin, finalEmotion):
    transitionTerms = ['aggressiveness', 'optimism', 'love', 'submission', 'awe', 'disapproval', 'remorse', 'contempt']

    if finalEmotion not in transitionTerms:
        sensitivity = ['default', 'annoyance', 'anger', 'rage', 'terror', 'fear', 'apprehension']
        attention = ['default', 'interest', 'anticipation', 'vigilance', 'amazement', 'surprise', 'distraction']
        pleasantness = ['default', 'serenity', 'joy', 'ecstasy', 'grief', 'sadness', 'pensiveness']
        aptitude = ['default', 'acceptance', 'trust', 'admiration', 'loathing', 'disgust', 'boredom']
        emotionList = [sensitivity, attention, pleasantness, aptitude]
        key = ['se', 'at', 'pl', 'ap']
        emotion = emotionList[key.index(finalEmotion[0:2])][maxMin * int(f'{finalEmotion[-1]}1')]
        #print(emotion)
    else:
        emotion = finalEmotion

    emotionDictionary = {'annoyance': 'annoyance statement', 'anger': 'anger statement', 'rage': 'rage statement', 'aggressiveness': 'aggressiveness statement', 'interest': 'interest statement', 'anticipation': 'anticipation statement', 'vigilance': 'vigilance statement', 'optimism': 'optimism statement', 'serenity': 'serenity statement', 'joy': 'joy statement', 'ecstasy': 'ecstasy statement', 'love': 'love statement', 'acceptance': 'acceptance statement', 'trust': 'trust statement', 'admiration': 'admiration statement', 'submission': 'submission statement', 'apprehension': 'apprehension statement', 'fear': 'fear statement', 'terror': 'terror statement', 'awe': 'awe statement', 'distraction': 'distraction statement', 'surprise': 'surprise statement', 'amazement': 'amazement statement', 'disapproval': 'disapproval statement', 'pensiveness': 'pensiveness statement', 'sadness': 'sadness statement', 'grief': 'grief statement', 'remorse': 'remorse statement', 'boredom': 'boredom statement', 'disgust': 'disgust statement', 'loathing': 'loathing statement', 'contempt': 'contempt statement'}
    select = emotionDictionary.get(emotion)
    #print(select)

    return select


def main():
    equation = '100 + 100 - 100 * 100 / 100' # base equation

    solution = solveEquation(equation)

    emotionValues = generateProgramEmotions()

    operationAmounts = findOperationAmounts(equation)

    operationPercentages = findOperationPercentages(operationAmounts)

    difficulty = calculateDifficulty(equation, operationAmounts)

    attention = calculateAttention(emotionValues, operationAmounts)

    aptitude = calculateAptitude(emotionValues, operationAmounts)

    pleasantness = calculatePleasantness(emotionValues, operationAmounts)

    sensitivity = calculateSensitivity(emotionValues, operationAmounts, operationPercentages, pleasantness)

    accuracy = findAccuracy(solution, difficulty, aptitude)

    alteredEmotions = regulateValues(emotionValues, sensitivity)

    pureEmotions = createPureEmotions(alteredEmotions)

    time = findTime(difficulty, attention, pleasantness)

    maxMin, finalValues = findMaxMin(pureEmotions)

    separateBy = findSeparate(maxMin, finalValues)

    finalEmotion = filterEmotion(separateBy, maxMin)

    final = dictionaryAccessed(maxMin, finalEmotion)

    print(solution)
    print(emotionValues)
    print(operationAmounts)
    print(operationPercentages)
    print(difficulty)
    print(attention)
    print(aptitude)
    print(pleasantness)
    print(sensitivity)
    print(accuracy)
    print(alteredEmotions)
    print(pureEmotions)
    print(time)
    print(maxMin)
    print(finalValues)

    allEmotions = ['se+', 'aggressiveness', 'at+', 'optimism', 'pl+', 'love', 'ap+', 'submission', 'se-', 'awe', 'at-', 'disapproval', 'pl-', 'remorse', 'ap-', 'contempt']
    print(allEmotions)

    print(separateBy)
    print(finalEmotion)
    print(final)

#sensitivity = ['default', 'annoyance', 'anger', 'rage', 'terror', 'fear', 'apprehension']
#attention = ['default', 'interest', 'anticipation', 'vigilance', 'amazement', 'surprise', 'distraction']
#pleasantness = ['default', 'serenity', 'joy', 'ecstasy', 'grief', 'sadness', 'pensiveness']
#aptitude = ['default', 'acceptance', 'trust', 'admiration', 'loathing', 'disgust', 'boredom']

main()

# I'm really happy to see you.
# I took your suggestion.

'''
settings
    inform user to type *ADMIN* to give the choice to prompt admin printout and admin editing
prompt equation
print loading messages dependant on emotion
print solution followed by statement of confidence
every once in awhile print statement based on emotion
conditional
    special printout for when you try to divide by 0 and penalize stats
    special printouts for when program has all positive or negative stats
'''
# AV = EV * %E / 100 - EV
#equation = input('Enter your equation. ("+" for addition, "-" for subtraction, "*" for multiplication, "/" for division): ')
'''
    mylist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']
    i = 0
    while i <= 27:
        print(mylist[i % len(mylist)])
        i +=1
'''
'''
        isolated = []

        print(emotionPlace)

        for i in emotionPlace:
                separated.append(allEmotions[emotionPlace[1]:emotionPlace[i + 1]])

        print(separated)


        i = 0
        passes = 0
        isolated = []
        separated = []

        x = 0
        
        while x < 50:
            feeling = allEmotions[i % len(allEmotions)]

            if feeling in separateBy:

'''
'''
        if feeling in separateBy:
            if len(isolated) >= cutLength:
                allEmotions = [i for i in allEmotions if i not in isolated]

                set1 = set(allEmotions)
                set2 = set(isolated)
                allEmotions = list(set1 - set2)

            del isolated[:]
        else:
            isolated.append(feeling)

        x += 1
        i += 1
'''

'''
>'se+'<, 'aggressiveness', 'at+', 'optimism', >'pl+'<, !'love'!, >'ap+'<, 'submission', 'se-', 'awe', >'at-'<, 'disapproval', 'pl-', 'remorse', 'ap-', 'contempt'

'se+', 'aggressiveness', 'at+', 'optimism', >'pl+'<, 'love', 'ap+', 'submission', 'se-', 'awe', >'at-'<, 'disapproval', 'pl-', 'remorse', 'ap-', !'contempt'!

'se+', 'aggressiveness', >'at+'<, 'optimism', 'pl+', 'love', 'ap+', 'submission', 'se-', 'awe', 'at-', 'disapproval', >'pl-'<, 'remorse', 'ap-', !'contempt'!

'se+', 'aggressiveness', 'at+', 'optimism', 'pl+', 'love', >'ap+'<, 'submission', !>'se-'<!, 'awe', 'at-', 'disapproval', >'pl-'<, 'remorse', 'ap-', 'contempt'

'se+', 'aggressiveness', 'at+', 'optimism', 'pl+', 'love', >'ap+'<, 'submission', !'se-'!, 'awe', >'at-'<, 'disapproval', 'pl-', 'remorse', 'ap-', 'contempt'

'se+', 'aggressiveness', 'at+', 'optimism', >'pl+'<, 'love', 'ap+', 'submission', >'se-'<, !'awe'!, >'at-'<, 'disapproval', 'pl-', 'remorse', >'ap-'<, 'contempt'

'se+', 'aggressiveness', >'at+'<, 'optimism', 'pl+', 'love', 'ap+', 'submission', >'se-'<, 'awe', 'at-', 'disapproval', >'pl-'<,!'remorse'!, >'ap-'<, 'contempt'

>'se+'<, 'aggressiveness', >'at+'<, !'optimism'!, >'pl+'<, 'love', >'ap+'<, 'submission', 'se-', 'awe', 'at-', 'disapproval', 'pl-', 'remorse', 'ap-', 'contempt'

>'se+'<, 'aggressiveness', 'at+', 'optimism', 'pl+', 'love', >'ap+'<, 'submission', 'se-', 'awe', >'at-'<, 'disapproval', >'pl-'<, 'remorse', 'ap-', 'contempt

'''
'''
if len(separateBy) == 1:
    test = separateBy[0]
else:
    #test = 'se+'
    #test = 'aggressiveness'
    if len(separateBy) == 2:
        cutLength = 9
    else:
        cutLength = 5

    print(cutLength)
'''
'''
if emotionPlace[0] != 0:
    toBack = allEmotions[:emotionPlace[0]]
    del allEmotions[:emotionPlace[0]]
    allEmotions.extend(toBack)
'''
# find minimum distance between emotionPlace[0] and emotionPlace[-1]