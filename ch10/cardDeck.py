import random


def createDeck():
    deck = []
    suits = ['\u2661', '\u2662', '\u2667', '\u2664']
    faces = ['J', 'Q', 'K', 'A']
# creates cards
    for digit in range(2, 11):
        for suit in suits:
            deck.append(str(digit) + suit)
    for face in faces:
        for suit in suits:
            deck.append(face + suit)
    random.shuffle(deck)

    return deck


def dealCards(deck, playerCount):
    playerDecks = []
    interval = len(deck) // playerCount
    start = 0
    end = interval
    for players in range(playerCount):
        playerDecks.append(deck[start:end])
        start = end
        end += interval

    return playerDecks


def main():
    deck = (createDeck())
    playerCount = 2
    print(deck[0])
    
main()