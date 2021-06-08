'''
N, S, T = input().split()
output = int(N)
mathTable = [3, 16, 2, 2, 4]
measurementTable = ['TEASPOONS', 'TABLESPOONS', 'CUPS', 'PINTS', 'QUARTS', 'GALLONS']

if measurementTable.index(S) > measurementTable.index(T):
    test = True
    table = [T, S]
else:
    test = False
    table = [S, T]

s, t = table[0], table[1]

counter = measurementTable.index(s)

if measurementTable.index(s) < measurementTable.index(t):
    while counter != measurementTable.index(t):
        if test:
            output *= mathTable[counter]
        else:
            output //= mathTable[counter]
        counter += 1

print(output)
'''

number, firstMeasurement, secondMeasurement = input().split()
number = int(number)
factors = [1, 3, 16, 2, 2, 4]
measurements = ['TEASPOONS', 'TABLESPOONS', 'CUPS', 'PINTS', 'QUARTS', 'GALLONS']

for i in measurements:
	if firstMeasurement == i:
		R = measurements.index(i)
	if secondMeasurement == i:
		S = measurements.index(i)
if R > S:
	for i in range(R - S):
		H = number * factors[S + i]
	print(H)
else:
	for i in range(S - R):
		H = number // factors[S + i]
	print(H)