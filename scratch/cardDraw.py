import random
S = '\u2664'
H = '\u2661'
D = '\u2662'
C = '\u2667'
emptyList = []
usedCards = []
deck = ['A'+S, '2'+S, '3'+S, '4'+S, '5'+S, '6'+S, '7'+S, '8'+S, '9'+S, '10'+S, 'J'+S, 'Q'+S, 'K'+S, 'A'+H, '2'+H, '3'+H, '4'+H, '5'+H, '6'+H, '7'+H, '8'+H, '9'+H, '10'+H, 'J'+H, 'Q'+H, 'K'+H, 'A'+D, '2'+D, '3'+D, '4'+D, '5'+D, '6'+D, '7'+D, '8'+D, '9'+D, '10'+D, 'J'+D, 'Q'+D, 'K'+D, 'A'+C, '2'+C, '3'+C, '4'+C, '5'+C, '6'+C, '7'+C, '8'+C, '9'+C, '10'+C, 'J'+C, 'Q'+C, 'K'+C]
while True:
    if deck == emptyList:
        print('Out of cards!')
        shuffle = input('Would you like to shuffle? (y/n): ')
        if shuffle == 'y':
            deck = usedCards.copy()
            usedCards = emptyList.copy()
        else:
            break
    randomCard = random.choice(deck)
    print(randomCard)
    usedCards.append(randomCard)
    deck.remove(randomCard)
    repeat = input('Would you like to draw another card? (y/n): ')
    if repeat == 'n':
        break
'''
usedCards = []
while True:
    import random
    cardPoints = ['A','K','Q','J','2','3','4','5','6','7','8','9','10']
    cardSigns = ['Hearts','Clubs','Diamonds','Spades']
    randomPoint = random.choice(cardPoints)
    randomSign = random.choice(cardSigns)
    randomCard = randomPoint, randomSign
    if usedCards.count(randomCard):
        print('test')
    else:
        print(randomCard)
        usedCards.append(randomCard)
    repeat = input('Would you like to draw another card? (y/n): ')
    if repeat == 'n':
        break
'''