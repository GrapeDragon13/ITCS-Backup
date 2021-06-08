scores = input('Enter scores: ').split()
scores = [int(x) for x in scores]
best = max(scores)
for i in range(len(scores)):
    if scores[i] >= best - 10:
        print(f'Student {i} score is {scores[i]} and grade is A')
    elif scores[i] >= best - 20:
        print(f'Student {i} score is {scores[i]} and grade is B')
    elif scores[i] >= best - 30:
        print(f'Student {i} score is {scores[i]} and grade is C')
    elif scores[i] >= best - 40:
        print(f'Student {i} score is {scores[i]} and grade is D')
    else:
        print(f'Student {i} score is {scores[i]} and grade is F')