def prefix(s1, s2):
    if s1[0] == s2[0]:
        if len(s1) > len(s2):
            length = len(s2)
        else:
            length = len(s1)
        for i in range(length):
            if s1[i] != s2[i]:
                return (s1[:i])
    else:
        return ('no matches')


def main():
    s1 = input('Enter first string: ')
    s2 = input('Enter second string: ')
    print(prefix(s1, s2))


main()