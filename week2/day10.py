# parsing + padding the input
inTab = [[-1] + [int(j) for j in i.strip()] + [-1] for i in open("input10.txt").readlines()]

# padding the input to avoid having to check indexes
minusOnes = []
for _ in range(len(inTab[0])):
    minusOnes.append(-1)
inTab = [minusOnes] + inTab + [minusOnes]

unique = []
# recursive algo that finds all trails from the position of a 0
def findTrail(prevPos, prevElev, currElev):
    global unique
    if prevElev+1 != currElev:
        return 0
    if currElev == 9:
        if prevPos not in unique:
            unique.append(prevPos) # for part 1
        return 1
    x, y = prevPos
    return ( findTrail([x, y-1], currElev, inTab[y-1][x])
            + findTrail([x, y+1], currElev, inTab[y+1][x])
            + findTrail([x+1, y], currElev, inTab[y][x+1])
            + findTrail([x-1, y], currElev, inTab[y][x-1]))

total1 = 0
total2 = 0
for y, line in enumerate(inTab):
    for x, num in enumerate(line):
        if num == 0:
            unique = [] # clear array before next call of findTrail
            nbTrails = findTrail([x, y], -1, 0)
            total1 += len(unique) # number of unique 9s reachable from the current 0
            total2 += nbTrails # number of all posible trails

print("part1: ", total1)
print("part2: ", total2)