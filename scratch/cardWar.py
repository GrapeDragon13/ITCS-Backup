import random
import time
player1Deck = []
player2Deck = []
player1Discard = []
player2Discard = []
#deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15,16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# player 1 hand deal
for _ in range(26):
    randomCard = random.choice(deck)
    player1Deck.append(randomCard)
    deck.remove(randomCard)
# player 2 hand deal
for _ in range(26):
    randomCard = random.choice(deck)
    player2Deck.append(randomCard)
    deck.remove(randomCard)
while True:

# **Problem Area**

  player1DeckLength = len(player1Deck)
  player2DeckLength = len(player2Deck)
  player1DiscardLength = len(player1Discard)
  player2DiscardLength = len(player2Discard)

  if player1DeckLength <= 4:
    for _ in range(player1DiscardLength):
      randomCard = random.choice(player1Discard)
      player1Deck.append(randomCard)
      player1Discard.remove(randomCard)

  if player2DeckLength <= 4:
    for _ in range(player2DiscardLength):
      randomCard = random.choice(player2Discard)
      player2Deck.append(randomCard)
      player2Discard.remove(randomCard)
  player1DeckLength = len(player1Deck)
  player2DeckLength = len(player2Deck)
  if len(player1Deck) < 4 and len(player2Deck) < 4:
    endgame = 0
    break
  elif len(player1Deck) < 4:
    endgame = 1
    break
  elif len(player2Deck) < 4:
    endgame = 2
    break

# **End Problem Area**
  player1Compare = random.choice(player1Deck)
  player2Compare = random.choice(player2Deck)
  if player1Compare > player2Compare:
    player1Discard.insert(player1Compare, player2Compare)
    player1Deck.remove(player1Compare)
    player2Deck.remove(player2Compare)
  elif player1Compare < player2Compare:
    player2Discard.insert(player1Compare, player2Compare)
    player1Deck.remove(player1Compare)
    player2Deck.remove(player2Compare)
  else:
    player1WarCard1 = random.choice(player1Deck)
    player1WarCard2 = random.choice(player1Deck)
    player1WarCard3 = random.choice(player1Deck)
    player2WarCard1 = random.choice(player2Deck)
    player2WarCard2 = random.choice(player2Deck)
    player2WarCard3 = random.choice(player2Deck)
    while True:
      player1Compare = random.choice(player1Deck)
      player2Compare = random.choice(player2Deck)
      if player1Compare > player2Compare:
        player1Discard.insert(player1Compare, player1WarCard1)
        player1Discard.insert(player1WarCard2, player1WarCard3)
        player1Discard.insert(player2Compare, player2WarCard1)
        player1Discard.insert(player2WarCard2, player2WarCard3)
        player1Deck.remove(player1Compare)
        player1Deck.remove(player1WarCard1)
        player1Deck.remove(player1WarCard2)
        player1Deck.remove(player1WarCard3)
        player2Deck.remove(player2Compare)
        player2Deck.remove(player2WarCard1)
        player2Deck.remove(player2WarCard2)
        player2Deck.remove(player2WarCard3)
        break
      elif player1Compare < player2Compare:
        player2Discard.insert(player1Compare, player1WarCard1)
        player2Discard.insert(player1WarCard2, player1WarCard3)
        player2Discard.insert(player2Compare, player2WarCard1)
        player2Discard.insert(player2WarCard2, player2WarCard3)
        player1Deck.remove(player1Compare)
        player1Deck.remove(player1WarCard1)
        player1Deck.remove(player1WarCard2)
        player1Deck.remove(player1WarCard3)
        player2Deck.remove(player2Compare)
        player2Deck.remove(player2WarCard1)
        player2Deck.remove(player2WarCard2)
        player2Deck.remove(player2WarCard3)
        break
      else:
        player1Deck.remove(player1Compare)
        player1Deck.remove(player1WarCard1)
        player1Deck.remove(player1WarCard2)
        player1Deck.remove(player1WarCard3)
        player2Deck.remove(player2Compare)
        player2Deck.remove(player2WarCard1)
        player2Deck.remove(player2WarCard2)
        player2Deck.remove(player2WarCard3)
  print(player1Deck)
  print(player2Deck)
  time.sleep(1)
if endgame == 0:
  print('tie')
elif endgame == 1:
  print('player 1 wins')
elif endgame == 2:
  print('player 2 wins')
else:
  print('You broke the program.')
print(player1Discard)
print(player2Discard)
print(len(player1Deck))
print(len(player2Deck))