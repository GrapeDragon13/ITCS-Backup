#import random
#import time


w = '#'
f = '+'


def get_line(start, end):
    # Setup initial conditions
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    # Determine how steep the line is
    is_steep = abs(dy) > abs(dx)
    # Rotate line
    if is_steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    # Swap start and end points if necessary and store swap state
    swapped = False

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    # Recalculate differentials
    dx = x2 - x1
    dy = y2 - y1
    # Calculate error
    error = int(dx / 2.0)
    ystep = 1 if y1 < y2 else -1
    # Iterate over bounding box generating points between start and end
    y = y1
    points = []

    for x in range(x1, x2 + 1):
        coord = (y, x) if is_steep else (x, y)
        points.append(coord)
        error -= abs(dy)

        if error < 0:
            y += ystep
            error += dx

    # Reverse the list if the coordinates were swapped
    if swapped:
        points.reverse()

    return points

# many if elif statements, variables from previous updates won't change with wrong input, need to add loops and only accept correct inputs

# map prints before characters or enemies move, tag will separate players from monsters in terms of funcionality

class sword1:
    name = 'sword1'
    tag = 'weapon'
    damage = 1
    weaponRange = 1
    duration = 1

class axe1:
    name = 'axe1'
    tag = 'weapon'
    damage = 2
    weaponRange = 1
    duration = 2

class bow1:
    name = 'bow1'
    tag = 'weapon'
    damage = 4
    weaponRange = 1
    duration = 2

class player1:
    name = 'Player1'
    tag = 'player'
    vincible = True
    health = 10
    damage = 5
    reach = 10
    turns = 2
    x, y = 4, 2
    symbol = '@'
    equip = []
    inventory = []

class player2:
    name = 'Player2'
    tag = 'player'
    vincible = True
    health = 5
    damage = 5
    reach = 4
    turns = 4
    x, y = 4, 6
    symbol = '&'
    equip = []
    inventory = []

# vampire for players?

# vampire, gargoyle, 
# slimes, venus flytrap plants, rats, giants, fairies, nature contructs, all sizes
# rust monster, armored worm-like creature
# goblin, kobold, shaman
# necromancer, skeleton, 
# human variant classes and skills
# elf variant classes and skills
# dwarf variant classes and skills

class dummyMonster(object):
    tag = 'enemy'
    vincible = True
    health = 10
    turns = 1
    symbol = '%'

    def __init__(self, x, y):
        self.x, self.y = x, y

class chest(object):
    symbol = '$'

    def __init__(self, x, y, list):
        self.x, self.y = x, y
        print(list)


#playerCount = int(input('How many players? '))
#print(playerCount)

creatureList = [player1, player2, dummyMonster(2, 4), dummyMonster(6, 4)]
lootList = [chest(1, 1, ['loot1', sword1]), chest(1, 4, ['loot2', axe1]), chest(1, 7, ['loot3', bow1])]

# creatures and monsters on separate lists to update but not print map, simplify separation mechanics

while True:
    for creature in creatureList:
        for turn in range(creature.turns):
            mapList = [
            [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, f, f, f, f, f, f, f, f, f, f, f, f, f, f, f, w],
            [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]
            ]

            for mapCreature in creatureList:
                mapList[mapCreature.y][mapCreature.x] = mapCreature.symbol

            for mapLoot in lootList:
                mapList[mapLoot.y][mapLoot.x] = mapLoot.symbol

            for i in mapList:
                for j in i:
                    print(j, end = " ")
                print()

            if creature.tag == 'player':
                #choice = 'MOVE'
                choice = 'ATTACK'
                #choice = input(f'{creature.name} what do you want to do? (ATTACK/MOVE) ')

                rememberX, rememberY = creature.x, creature.y

                if choice == 'ATTACK':
                    start = (creature.y, creature.x)
                    attackX, attackY = input(f'{creature.name} what coordinate do you want to attack? ').split()

                    end = (int(attackY), int(attackX))
                    trajectory = get_line(start, end)

                    for target in creatureList:
                        for coordinate, limit in zip(trajectory, range(creature.reach)):
                            if (target.y, target.x) == coordinate:
                                if target.tag == 'enemy' and target.vincible:
                                    target.health -= creature.damage

                                    if target.health <= 0:
                                        creatureList.remove(target)
                                break

                            elif mapList[coordinate[1]][coordinate[0]] == '#':
                                print('broken')
                                break

    # loop through range in range, maybe change name and work on funcionabiliy

                elif choice == 'MOVE':
                    moveDirection = input(f'{creature.name}, what direction do you want to go? (W/E/D/C/X/Z/A/Q) ')

                    if moveDirection == 'W':
                        creature.y -= 1
                    elif moveDirection == 'E':
                        creature.x += 1
                        creature.y -= 1
                    elif moveDirection == 'D':
                        creature.x += 1
                    elif moveDirection == 'C':
                        creature.x += 1
                        creature.y += 1
                    elif moveDirection == 'X':
                        creature.y += 1
                    elif moveDirection == 'Z':
                        creature.x -= 1
                        creature.y += 1
                    elif moveDirection == 'A':
                        creature.x -= 1
                    elif moveDirection == 'Q':
                        creature.x -= 1
                        creature.y -= 1

                if mapList[creature.y][creature.x] != '+':
                    creature.x, creature.y = rememberX, rememberY
            #elif creature.tag == 'enemy':


'''
# is wall
+ is floor
@ is creature
$ is enemy

w = '#'
f = '+'

# want (x, y)

dR1 = f'{w} {w} {w} {w} {w} {w} {w} {w} {w}'
dR2 = f'{w} {f} {f} {f} {f} {f} {f} {f} {w}'
dR3 = f'{w} {f} {f} {f} {f} {f} {f} {f} {w}'
dR4 = f'{w} {f} {f} {f} {f} {f} {f} {f} {w}'
dR5 = f'{w} {f} {f} {f} {f} {f} {f} {f} {w}'
dR6 = f'{w} {f} {f} {f} {f} {f} {f} {f} {w}'
dR7 = f'{w} {f} {f} {f} {f} {f} {f} {f} {w}'
dR8 = f'{w} {f} {f} {f} {f} {f} {f} {f} {w}'
dR9 = f'{w} {w} {w} {w} {w} {w} {w} {w} {w}'

# (x, y) is dR(y)[x]

#layer1 = f'{dR1}\n{dR2}\n{dR3}\n{dR4}\n{dR5}\n{dR6}\n{dR7}\n{dR8}\n{dR9}'
#print(layer1)
layer1 = [dR1, dR2, dR3, dR4, dR5, dR6, dR7, dR8, dR9]
print(*layer1, sep='\n')

x = 2
y = 1

print(layer1[y][x])

if choice == 'ATTACK':
    attackDirection = input(f'{creature.name} what direction would you like to attack? (W/E/D/C/X/Z/A/Q) ')

    attackX, attackY = creature.x, creature.y

    if attackDirection == 'W':
        attackXMod = 0
        attackYMod = -1
    elif attackDirection == 'E':
        attackXMod = 1
        attackYMod = -1
    elif attackDirection == 'D':
        attackXMod = 1
        attackYMod = 0
    elif attackDirection == 'C':
        attackXMod = 1
        attackYMod = 1
    elif attackDirection == 'X':
        attackXMod = 0
        attackYMod  = 1
    elif attackDirection == 'Z':
        attackXMod = -1
        attackYMod = 1
    elif attackDirection == 'A':
        attackXMod = -1
        attackYMod = 0
    elif attackDirection == 'Q':
        attackXMod = -1
        attackYMod = -1

    for i in range(creature.reach):
        attackX += attackXMod
        attackY += attackYMod

        print('(',attackX,',', attackY,')')
        print(mapList[attackY][attackX])
'''