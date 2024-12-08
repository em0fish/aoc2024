import re

inData = open("input8.txt").readlines()
lineLength = len(inData[0])-1 # -1 bc of \n
dataLength = len(inData)
inData = "".join(inData).replace("\n", "")

def isInBounds(coords):
    x, y = coords
    return 0<=y<dataLength and 0<=x<lineLength
def indToXY(ind):
    return [ind%lineLength, ind//lineLength]

uniquePos = []

def part1(x1, y1, x2, y2):
    global uniquePos
    antinode1 = [x1-(x2-x1), y1-(y2-y1)]
    antinode2 = [x2+(x2-x1), y2+(y2-y1)]
    if isInBounds(antinode1) and antinode1 not in uniquePos:
        uniquePos.append(antinode1)
    if isInBounds(antinode2) and antinode2 not in uniquePos:
        uniquePos.append(antinode2) 

def part2(x1, y1, x2, y2):
    global uniquePos
    vecX = x2 - x1
    vecY = y2 - y1
    # all antinodes in one direction
    currX = x2 + vecX
    currY = y2 + vecY
    currCoords = [currX, currY]
    while isInBounds(currCoords):
        if currCoords not in uniquePos:
            uniquePos.append(currCoords)
        currX += vecX
        currY += vecY
        currCoords = [currX, currY]
    # all antinodes in the opposite direction
    currX = x1 - vecX
    currY = y1 - vecY
    currCoords = [currX, currY]
    while isInBounds(currCoords):
        if currCoords not in uniquePos:
            uniquePos.append(currCoords)
        currX -= vecX
        currY -= vecY
        currCoords = [currX, currY]

i = 0
while i < len(inData):
    c = inData[i]
    if c != ".":
        # get all indexes of c in inData
        indsOfChar = [m.start() for m in re.finditer(c, inData)]
        inData = inData.replace(c, ".") # ensure every char is only treated once
        for j, first in enumerate(indsOfChar):
            x1, y1 = indToXY(first)
            # part 2
            if [x1, y1] not in uniquePos:
                uniquePos.append([x1, y1]) # we need to add the satelites themselves
            # part 2 end
            for second in indsOfChar[(j+1):]:
                x2, y2 = indToXY(second)
                #part1(x1, y1, x2, y2)
                part2(x1, y1, x2, y2)
    i += 1

print(len(uniquePos))