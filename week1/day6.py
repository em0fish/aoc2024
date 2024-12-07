
import copy

inString = open("input6.txt").read()

dirInd = 0 # 0 - up| 1 - right | 2 - down | 3 - left
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
inTab = [list(i) for i in inString.split("\n")]
lineLength = len(inTab[0])

guard = inString.replace("\n", "").find("^")
guardX = guard % lineLength
guardY = guard // lineLength

# takes in a map (tab) and the starting coordinated of
# the guard and determines whether the guard can get stuck
# in an infinite loop.
def isLoop(tab, x, y):
    visitedTiles = []
    dirInd = 0
    while (0 <= x < lineLength and
            0 <= y < len(tab)):
        posDir = [lineLength*y + x, dirInd]
        if posDir in visitedTiles: 
            return True
        
        visitedTiles.append(posDir)
        if tab[y][x] == "#":
            xUnchange, yUnchange = dirs[dirInd]
            x -= xUnchange
            y -= yUnchange 
            dirInd = (dirInd+1) % 4
        xChange, yChange = dirs[dirInd]
        x += xChange
        y += yChange
    return False

def part1(x, y, dirInd, dirs):
    total = 1
    while (0 <= x < lineLength and
            0 <= y < len(inTab)):
        pos = inTab[y][x]
        if pos == "#":
            xUnchange, yUnchange = dirs[dirInd]
            x -= xUnchange
            y -= yUnchange 
            dirInd = (dirInd+1) % 4
        elif pos == ".":
            inTab[y][x] = "X"
            total += 1
        xChange, yChange = dirs[dirInd]
        x += xChange
        y += yChange
    return total

# takes way too long :(
def part2(x, y, dirInd, dirs):
    # tiles visited during the unmodified walk
    ogVisited = []

    while (0 <= x < lineLength and
            0 <= y < len(inTab)):
        pos = inTab[y][x]
        if pos == "#":
            xUnchange, yUnchange = dirs[dirInd]
            x -= xUnchange
            y -= yUnchange 
            dirInd = (dirInd+1) % 4
        elif pos == ".":
            if [x, y] not in ogVisited:
                ogVisited.append([x, y])
        xChange, yChange = dirs[dirInd]
        x += xChange
        y += yChange

    total = 0
    tempTab = copy.deepcopy(inTab)
    for coords in ogVisited:
        x, y = coords
        tempTab[y][x] = "#"
        if isLoop(tempTab, guardX, guardY):
            total += 1
        tempTab[y][x] = "."
    return total
