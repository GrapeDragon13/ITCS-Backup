def isSubString(string, subString):
    if string.find(subString) >= 0:
        return True
    else:
        return False


def main():
    subString = input('Enter a string: ')
    string = input('Enter a string: ')
    if isSubString(string, subString):
        print('is a substring')
    else:
        print('not a substring')



main()

'''
subString = input('Enter a string: ')
string = input('Enter a string: ')
if subString in string:
    print('is a substring')
else:
    print('not a substring')
'''