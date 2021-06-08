def reverse(s):
    return s[::-1]


def main():
    s = input('Enter a string: ')
    print(reverse(s))


main()


'''
s = input('Enter a string: ')
newString = s[::-1]
print(newString)
'''


'''
s = input('Enter a string: ')
newString = ''
for i in range(len(s) - 1, - 1, - 1):
    newString += s[i]
print(newString)
'''


'''
s = input('Enter a string: ')
newString = ''
for char in s:
    newString = char + newString
print(newString)
'''