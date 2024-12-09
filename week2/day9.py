inString = open("input9.txt").read().strip()

# split the input into files and gaps
files = []
gaps = []
for i, num in enumerate(inString):
    if i % 2 == 0:
        files.append(int(num))
    else:
        gaps.append(int(num))

# only usable / readable when the max index of file < 10
def tabToStringTest(tab):
    out = ""
    for i in range(len(tab)):
        if tab[i] == -1:
            out += "."
        else:
            out += str(tab[i])
    return out

# returns a table representing the state of memory
# specified by `gaps`, `files`.
# files represented by their ids, gaps by -1s.
def buildTab1(gaps, files):
    i, j = 0, 0
    out = []
    while j < len(files) and i < len(gaps):
        for _ in range(files[j]):
            out.append(j)
        if isinstance(gaps[i], int):
            for _ in range(gaps[i]):
                out.append(-1)
        else:
            out += gaps[i]
        i += 1
        j += 1
    return out

# same functionality as buildTab1, but modified
# for part 2.
# gaps: list of lists of ints
# files: list of ints
# lens: list of ints
def buildTab2(gaps, lens, files):
    i = 0
    out = []
    idsSeen = []
    while i < len(gaps):
        if i in idsSeen: # to not add moved files twice
            for _ in range(files[i]):
                out.append(-1)
        else:
            for _ in range(files[i]):
                out.append(i)
        out += gaps[i] # appends the content of the gap
        for id in gaps[i]:
            if id not in idsSeen: idsSeen.append(id)
        for _ in range(lens[i]): # adds empty slots for empty parts of gaps
            out.append(-1)
        i += 1
    # treats the last file in case theres more files than gaps
    if i < len(files):
        if i in idsSeen:
            for _ in range(files[i]):
                out.append(-1)
        else:
            for _ in range(files[i]):
                out.append(i)   
    return out

def part1(gaps, files):
    # break condition: trying to add a file with id i
    # to a gap with index >= i
    breakLoops = False
    indG = 0
    indF = len(files) - 1
    while not breakLoops:
        movedFiles = []
        while gaps[indG] > len(movedFiles) and not breakLoops:
            movedFiles.append(indF)
            files[indF] = files[indF] - 1
            if files[indF] == 0:
                indF -= 1
            if indG >= indF:
                breakLoops = True
        #print(movedFiles)
        gaps[indG] = movedFiles
        indG += 1
        #print(buildString(gaps, files))
    return gaps, files

def part2(gapLengths, files):
    # having gaps AND gapLengths allows for multiple files
    # to be able to fit into the same gap
    gaps = [[] for _ in range(len(gapLengths))]
    indG = 0 # we always search for the leftmost possible gap
    indF = len(files) - 1 # treat files from last to first
    while indF != -1:
        # searching for a gap big enough for the file
        while indG < len(gaps) and files[indF] > gapLengths[indG]:
            indG += 1
        if indG == len(gaps): # no gap big enough for file
            indF -= 1
            indG = 0
            continue
        # decrement the size of the gap
        gapLengths[indG] = gapLengths[indG] - files[indF]
        filledGap = gaps[indG]
        # update the gap with the new file
        for _ in range(files[indF]):
            filledGap.append(indF)
        gaps[indG] = filledGap
        indF -= 1
        indG = 0
    return gaps, gapLengths

def calcChecksum(tab):
    i = 0
    checksum = 0
    while i < len(tab):
        if tab[i] == -1:
            i += 1
            continue
        checksum += (i*tab[i])
        i += 1
    return checksum

#print(buildTab1(gaps, files)) # intial state of memory
#finalTab = buildTab1(*part1(gaps, files))
finalTab = buildTab2(*part2(gaps, files), files)
# print(tabToStringTest(finalTab))
print(calcChecksum(finalTab))


