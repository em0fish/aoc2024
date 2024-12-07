lines = open("input4.txt").readlines()

## dir order
#    8 1 2
#  7   .   3
#    6 5 4
##

# directions= [
#     [0, -1], [1, -1],
#     [1, 0], [1, 1],
#     [0, 1], [-1, 1],
#     [-1, 0], [-1, -1]
#     ]

# total = 0

# for i, line in enumerate(lines):
#     for j, c in enumerate(line):
#         if c == "X":
#             for d in range(len(directions)):
#                 xChange, yChange = directions[d]
#                 x = j + xChange
#                 y = i + yChange
#                 add = True
#                 for symb in "MAS":
#                     if 0 <= y < len(lines) and 0 <= x < len(line) and lines[y][x] == symb:
#                         x += xChange
#                         y += yChange
#                     else:
#                         add = False
#                         break
#                 if add:
#                     total += 1

# print(total)

#   X.X
#    .
#   X X

total = 0

inds = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == "A":
            if (j == 0 or i == 0 or j == (len(line)-1) or i == (len(lines)-1)):
                continue
            word1 = lines[i-1][j-1] + "A" + lines[i+1][j+1]
            word2 = lines[i+1][j-1] + "A" + lines[i-1][j+1]
            if ((word1 == "MAS" or word1 == "SAM")
                and (word2 == "MAS" or word2 == "SAM")):
                total += 1
                inds += [[j, i], [j-1, i-1], [j+1, i-1], [j-1, i+1], [j+1, i+1]]

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if [j, i] not in inds:
            print(".", end="")
        else:
            print(c, end="")
    print("")

print(total)