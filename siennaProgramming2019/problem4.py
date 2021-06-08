N = input()
counter = 0

while True:
    if N == '89' or N == '1':
        break

    counter += 1
    newN = 0

    for i in N:
        newN += int(i) ** 2

    N = str(newN)

print(N, counter)