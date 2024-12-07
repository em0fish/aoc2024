
import copy

inString = open("input6.txt").read()

dirInd = 0
dirs = [[0, -1], [1, 0], [0, 1], [-1, 0]]
inTab = [list(i) for i in inString.split("\n")]
lineLength = len(inTab[0])
inString = inString.replace("\n", "")

#print(inTab)

guard = inString.find("^")
x = guard % lineLength
y = guard // lineLength
guardX = x
guardY = y

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

### part 1
# total = 1
# while (0 <= x < lineLength and
#         0 <= y < len(inTab)):
#     pos = inTab[y][x]
#     if pos == "#":
#         xUnchange, yUnchange = dirs[dirInd]
#         x -= xUnchange
#         y -= yUnchange 
#         dirInd = (dirInd+1) % 4
#     elif pos == ".":
#         inTab[y][x] = "X"
#         total += 1
#     xChange, yChange = dirs[dirInd]
#     x += xChange
#     y += yChange

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

print(len(ogVisited))

total = 0
tempTab = copy.deepcopy(inTab)
for coords in ogVisited:
    x, y = coords
    tempTab[y][x] = "#"
    if isLoop(tempTab, guardX, guardY):
        total += 1
    tempTab[y][x] = "."

print(total)
