def count(s, ch):
    count = 0
    for char in s:
        if char == ch:
            count += 1
    return count


def main():
    s, ch = input('Enter a string followed by a search string: ').split()
    print(count(s, ch))


main()


'''
def count(s, ch):
    repeat = 1
    for i in range(len(s)):
        if s.find(ch) != -1:
            repeat += 1
        else:
            repeat = 0
        return repeat
'''