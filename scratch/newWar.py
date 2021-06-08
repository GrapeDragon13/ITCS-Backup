import random


def createDeck():
    deck = []
    suits = [' of S', ' of C', ' of H', ' of D']
# creates cards
    for digit in range(1, 14):
        for suit in suits:
            deck.append(str(digit) + suit)
    random.shuffle(deck)

    return deck
# ace is 13, '#' for compare seperation


# deal cards to players
def dealCards(deck, playerCount):
    playerDecks = []
    numberOfPlayers = playerCount
    interval = len(deck) // numberOfPlayers
    start = 0
    end = interval + 1
    for players in range(numberOfPlayers):
        playerDecks.append(deck[start:end])
        start = end
        end += interval

    return playerDecks
# player 1 deck: playerDecks[0]
# player 2 deck: playerDecks[1]


def createDiscard(playerCount):
    discard = []
    numberOfPlayers = playerCount
    for players in range(numberOfPlayers):
        discard.append([])

    return discard


def compareCardsDraw(playerDecks, playerCount):
    cardsDrawn = []
    numberOfPlayers = playerCount
    player = 0
    for players in range(numberOfPlayers):
        cardsDrawn.append(playerDecks[player][0])
        player += 1

    return cardsDrawn


# largest integer card set to highestDrawnCard
def highestCard(cardsDrawn, playerCount):
    integerCardsDrawn = [cards[:-5] for cards in cardsDrawn]

    return integerCardsDrawn


# find largest integer, extract players with largest integer, if more than one then war, if 1 player put in their discard
# use str.isnumeric and maybe local list?
# use max to find max in cardsDrawn
# another player list, add a player to the list if the string of max is in the card string
# pool of cards list, winner takes pool


# driving function
def main():
    playerCount = 2
    deck = createDeck()
    playerDecks = dealCards(deck, playerCount)
    discard = createDiscard(playerCount)
    cardsDrawn = compareCardsDraw(playerDecks, playerCount)
    roundCardWinner = highestCard(cardsDrawn, playerCount)
    print(playerDecks)
    print(cardsDrawn)
    print(discard)
    # discard[0].append('test')
    print(roundCardWinner)

main()

'''
1. create deck

2. deal deck to players

3. characters are allowed to view and rearrange their cards

4. isolate the first card in each deck to use for comparing

5. procedurally compare cards in the rules as follows:
    compare card is added to a pool
    each card must retain a connection to the player they came from
    the highest value cards are isolated among the winners category
    if there is a tie among the highest value cards, they enter a war
    if a player loses during a war, but there are still other players that repeat the war, they exit the war
    if a player runs out of cards to add to the pool during the war, they automatically lose
    once there is only one player with the highest card value remaining, they win all cards in the pool, added to their discard pile

    war rules:
        3 cards selected from the top of each players' deck in the war are added to a more local pool between warring players
        a 4th card is drawn from the top of the warring players' deck
        the value of the 4th card is taken and compared to other players' war card compare card
        the player with the highest value card gets all the cards in the pool added to their discard pile
        wars can repeat, adding to the pool
        players that lose a war can be cut from an ongoing war, they are no longer involved in the war

6. in the case of a player running out of cards:
    at ANY POINT if a character runs out of cards, even in the middle of a war, they may access their discard pile
    their discard pile is added to their deck and players are given the chance to rearrange their cards

7. if a player is out of cards in their pile and discard pile, they lose

8. repeat 4-7 until one player remains, this player wins
    if all players lose, most likely as a result of war, there is no winner

'''

'''
# playerCount = eval(input('Enter the number of players: '))


def compareCardsDraw(playerDecks, playerCount):
    cardsDrawn = []
    numberOfPlayers = playerCount
    player = 0
    for players in range(numberOfPlayers):
        cardsDrawn.append(playerDecks[player][0])
        player += 1

    return cardsDrawn


def seperateCompareCards(cardsDrawn):
    seperateCompareCardsList = []
    player = 0
    for cards in cardsDrawn:
        seperateCompareCardsList.append(cardsDrawn[player].split('#'))
        player += 1

    return seperateCompareCardsList


print(cardsDrawn)

def compareCardsDraw(playerDecks, playerCount):
    cardsDrawn = []
    seperateCompareCards = []
    numberOfPlayers = playerCount
    player = 0
    for players in range(numberOfPlayers):
        cardsDrawn.append(playerDecks[player][0])
        seperateCompareCards += cardsDrawn[player].split('#')
        player += 1

    return seperateCompareCards

    print(seperateCompareCards)
    for player in range(playerCount):
        print(int(seperateCompareCards[playerRepeat]))
        playerRepeat += 2
'''