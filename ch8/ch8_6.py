s = input('Enter a string: ')

def count_letter(s):
    unique = list()
    for i in s:
        if i not in unique:
            unique.append(i)
    return len(unique)

print(count_letter(s))


'''
def def count_letter(s):
    unique = ''
    for char in s:
        if char not in unique:
            unique += char
        return unique


    def main():
    s = input('Enter a string: ')
    print(count_letter(s))


main()
'''