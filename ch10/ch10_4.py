scores = input('Enter scores: ').split()
scores = list(map(int, scores))
average = sum(scores) // len(scores)
above, below, equal = 0, 0, 0
for score in scores:
    if score > average:
        above += 1
    elif score < average:
        below += 1
    else:
        equal += 1
print(f'average is {average}')
if above > 0:
    print(f'{above} above average')
if below > 0:
    print(f'{below} below average')
if equal > 0:
    print(f'{equal} equal')