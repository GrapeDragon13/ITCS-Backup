# https://www.analytics-link.com/post/2018/09/14/applying-the-a-path-finding-algorithm-in-python-part-1-2d-square-grid
# probably faster with numpy implementation

from heap import heappush, heappop
#import matplotlib.pyplot as plt


# ====================
def getLine(start, end):
    x1, y1 = start
    x2, y2 = end
    dx = x2 - x1
    dy = y2 - y1
    isSteep = abs(dy) > abs(dx)

    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2

    swapped = False

    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        swapped = True

    dx = x2 - x1
    dy = y2 - y1
    error = int(dx / 2)
    yStep = 1 if y1 < y2 else -1
    y = y1
    points = []

    for x in range(x1, x2 + 1):
        coordinates = (y, x) if isSteep else (x, y)
        points.append(coordinates)
        error -= abs(dy)

        if error < 0:
            y += yStep
            error += dx

    if swapped:
        points.reverse()

    return points
# ====================


# ====================
# plot grid
grid = [
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0],
    [0, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# start point and goal
start = (0,0)
goal = (0,19)


# heuristic function for path scoring
def heuristic(a, b):
    #return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)
    return ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5


# path finding function
def AStar(array, start, goal):
    xLength = len(grid[0])
    yLength = len(grid)
    neighbors = [(0, 1),(0, -1),(1, 0),(-1, 0),(1, 1),(1, -1),(-1, 1),(-1, -1)]
    close_set = set()
    came_from = {}
    gscore = {start:0}
    fscore = {start:heuristic(start, goal)}
    oheap = []
    heappush(oheap, (fscore[start], start))

    while oheap:
        current = heappop(oheap)[1]

        if current == goal:
            data = []

            while current in came_from:
                data.append(current)
                current = came_from[current]

            return data

        close_set.add(current)

        for i, j in neighbors:
            neighbor = current[0] + i, current[1] + j
            tentative_g_score = gscore[current] + heuristic(current, neighbor)

            if 0 <= neighbor[0] < yLength:
                if 0 <= neighbor[1] < xLength:
                    if array[neighbor[0]][neighbor[1]] == 1:
                        continue

                else:
                    # array bound y walls
                    continue

            else:
                # array bound x walls
                continue
 
            if neighbor in close_set and tentative_g_score >= gscore.get(neighbor, 0):
                continue
 
            if  tentative_g_score < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in oheap]:
                came_from[neighbor] = current
                gscore[neighbor] = tentative_g_score
                fscore[neighbor] = tentative_g_score + heuristic(neighbor, goal)
                heappush(oheap, (fscore[neighbor], neighbor))

    return False
# ====================

'''
for bots:
    on same team will be considered solid
    on different team will be target, not solid
    closest enemy will be target

have different intelligences
need to know their attack range and be in it before attacking
know player attack range and end turn outside of it?
know how many turns of attack they will get?
know if they have a chance to kill a player?

for players:
    all creatures are considered solid
    player chooses the target
        if more moves than player has
            player is informed of where they will end up
        else
            player is informed of how many moves they will have left, special print for no moves left
        ask confirmation? one both or neither?
'''

route = AStar(grid, start, goal)
route = route + [start]
route = route[::-1]
print(route)

'''
# plot the path
#extract x and y coordinates from route list

x_coords = []
y_coords = []

for i in (range(0,len(route))):
    x = route[i][0]
    y = route[i][1]
    x_coords.append(x)
    y_coords.append(y)

# plot map and path
fig, ax = plt.subplots(figsize=(3, 3))
ax.imshow(grid, cmap=plt.cm.Dark2)
ax.scatter(start[1],start[0], marker = "*", color = "yellow", s = 200)
ax.scatter(goal[1],goal[0], marker = "*", color = "red", s = 200)
ax.plot(y_coords,x_coords, color = "black")
plt.show()
'''