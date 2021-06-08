# can make a list if there is only one variable receiving
letter1, letter2, letterSolution = input().split()
number1, number2, numberSolution = input().split()
print(letter1, letter2, letterSolution)
print(number1, number2, numberSolution)

if int(number1) + int(number2) != int(numberSolution):
    failed = True
else:
    letterList = list(letter1) + list(letter2) + list(letterSolution)
    numberList = list(number1) + list(number2) + list(numberSolution)
    failed = False
    remember = {}

    for letter, number in zip(letterList, numberList):
        if letter in remember:
            if remember[letter] != number:
                failed = True
        else:
            remember[letter] = number

if failed:
    print('BAD')
else:
    print('GOOD')

'''
letter1, letter2, letterSolution = list(letter1), list(letter2), list(letterSolution)
number1, number2, numberSolution = list(number1), list(number2), list(numberSolution)
letterList = letter1 + letter2 + letterSolution
numberList = number1 + number2 + numberSolution
'''

'''
my_dictionary = {'foo' : 10, 'bar' : 20}
variable = my_dictionary['foo']

#test_values = [1, 4, 5]

# Printing original keys-value lists
print ("Original key list is : " + str(test_keys))
print ("Original value list is : " + str(test_values))

# using zip()
# to convert lists to dictionary
res = dict(zip(test_keys, test_values))

# Printing resultant dictionary 
print ("Resultant dictionary is : " +  str(res))

d = {'a': 1, 'b': 2}
print(d)
d['a'] = 100  # existing key, so overwrite
d['c'] = 3  # new key, so add
d['d'] = 4
print(d)
'''