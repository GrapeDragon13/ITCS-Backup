contestants = ['Scissors', 'Paper', 'Rock', 'Lizard', 'LargeHadronCollider', 'Zombie', 'Spock']
contestantList = input().split()

if contestantList[0] == contestantList[1]:
    print('Tie')
else:
    #indexList = [contestants.index(item) for item in contestantList]
    #sortedContestants = [i for j, i in sorted(zip(indexList, contestantList))]
    order = {item:i for i, item in enumerate(contestants)}
    sortedContestants = sorted(contestantList, key = order.__getitem__)
    difference = contestants.index(sortedContestants[1]) - contestants.index(sortedContestants[0])

    if difference % 2 == 1:
        winner = sortedContestants[0]
    else:
        winner = sortedContestants[1]

    print(winner)

'''
while True:
    contestants = ['Scissors', 'Paper', 'Rock', 'Lizard', 'LargeHadronCollider', 'Zombie', 'Spock']
    contestant1 = input()
    contestant2 = input()
    start = contestants.index(contestant1)

    if contestant1 == contestant2:
        print('Tie')
    else:
        while True:
            start += 1
        
            if contestants[start % len(contestants)] == contestant2:
                break
        
        if start % 2 == 1:
            winner = contestant1
        else:
            winner = contestant2
        
        print(winner)
'''