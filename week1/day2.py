FD = open("input2.txt")
nbSafe = 0

### part 1
# while True:
#     add = True
#     line = FD.readline()
#     if line == "": 
#         break
#     line = list(int(i) for i in line.split(" "))
#     if line == sorted(line) or line == sorted(line, reverse = True):
#         for i in range(len(line)-1):
#             distance = abs(line[i] - line[i+1])
#             if distance == 0 or distance > 3:
#                 add = False
#         if add:
#             nbSafe += 1

while True:
    line = FD.readline()
    if line == "": 
        break
    line = list(int(i) for i in line.split(" "))
    lineOG = list.copy(line)
    for i in range(-1, len(lineOG)):
        line = list.copy(lineOG)
        if (i != -1): 
            line.pop(i)
        #print(line)
        add = True ## resets the bool for the new it
        if line == sorted(line) or line == sorted(line, reverse = True):
            for i in range(len(line)-1):
                distance = abs(line[i] - line[i+1])
                if distance == 0 or distance > 3:
                    add = False
            if add:
                nbSafe += 1
                #print("^safe")
                break


print(nbSafe)