def inputTest():
    test = []
    while len(test) != 10:
        test.append(input('Test: '))

    return test


def main():
    test = inputTest()
    print(test)

main()