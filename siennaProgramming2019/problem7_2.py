letter1 = 'send'
letter2 = 'more'
letterSolution = 'money'

wordList = [letter1, letter2, letterSolution]

setList = ['r', 's', 'e', 'n', 'd', 'm', 'o', 'y']
combination = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
combination = list(map(str, combination))

worthTesting = []

start = 0
end = len(setList)

while True:

    save = combination[start:end]
    print(save)

    testDictionary = dict(zip(setList, save))

    mathSave = []

    for word in wordList:
        mathSave.append(''.join(testDictionary.get(ele, ele) for ele in word))

    if mathSave[0] + mathSave[1] == mathSave[2]:
        worthTesting.append(mathSave)

    if end == 10:
        break

    start += 1
    end += 1

#letterList = list(letter1) + list(letter2) + list(letterSolution)
#numberList = list(number1) + list(number2) + list(numberSolution)

#example = dict(zip(keyList, valuesList))

# set list of all letter inputs

# take set of letters all
# can only be 10 unique letters, if more automatic fail
# save unique letters as list

# iterate through all possible combinations of 1234567890
# 1234567890 and all combinations, all segments equal to the length of the unique letter list

#example = dict(zip(keyList, valuesList))

# with each iteration combine unique letter list with iteration
# replace each letter in *letter1 + letter2 = letterSolution*
# if math works, save math as string with each letter replaced *letter1 + letter2 = letterSolution*

#if int(number1) + int(number2) != int(numberSolution):
#    failed = True

'''
dictionary = {"NORTH":"N", "SOUTH":"S" } 
for key in dictionary.keys():
    address = address.upper().replace(key, dictionary[key])
'''

'''
# Python3 code to demonstrate working of 
# Replace words from Dictionary
# Using list comprehension + join()

# initializing string
test_str = 'send'

# printing original string
print("The original string is : " + str(test_str))

# lookup Dictionary
lookp_dict = {'s':'9', 'e':'5', 'n':'6', 'd':'7', 'm':'1', 'o':'0', 'r':'8', 'y':'2'}

# one-liner to solve problem
res = " ".join(lookp_dict.get(ele, ele) for ele in test_str)

# printing result 
print("Replaced Strings : " + str(res)) 
'''