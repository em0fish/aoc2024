FD = open("input2.txt")

def part1():
    nbSafe = 0
    while True:
        add = True
        line = FD.readline()
        if line == "": 
            break
        line = list(int(i) for i in line.split(" "))
        if line == sorted(line) or line == sorted(line, reverse = True):
            for i in range(len(line)-1):
                distance = abs(line[i] - line[i+1])
                if distance == 0 or distance > 3:
                    add = False
            if add:
                nbSafe += 1
    return nbSafe

def part2():
    nbSafe = 0
    while True:
        line =   FD.readline()
        if line == "": 
            break
        line = list(int(i) for i in line.split(" "))
        lineOG = list.copy(line)
        
        # try if the OG line is safe, if it isnt, try the line with each of 
        # the elements removed. break for loop when a safe version is found.
        for i in range(-1, len(lineOG)):
            line = list.copy(lineOG)
            if (i != -1): 
                line.pop(i)
            add = True ## resets the bool for the new iteration
            if line == sorted(line) or line == sorted(line, reverse = True):
                for i in range(len(line)-1):
                    distance = abs(line[i] - line[i+1])
                    if distance == 0 or distance > 3:
                        add = False
                if add:
                    nbSafe += 1
                    break
    return nbSafe

print(part2())
FD.close()