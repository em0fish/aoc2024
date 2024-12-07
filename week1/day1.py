list1 = []
list2 = []

FD = open("input1.txt")
while True:
    line = FD.readline()
    if (line == ""): break
    new1, new2 = line.split("   ")
    list1.append(int(new1))
    list2.append(int(new2))

def part1():
    out = 0
    while list1 != []:
        min1 = min(list1)
        list1.remove(min1)
        min2 = min(list2)
        list2.remove(min2)
        out += (max(min1, min2)-min(min1, min2))
    return out

def part2():
    out = 0
    for el in list1:
        out += ( list2.count(el)*el )
    return out

FD.close()
print(part2())