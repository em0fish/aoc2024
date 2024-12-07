def isResPosssible(res, numList, numbersleft, prevRes):
    if prevRes > res:
        return False
    if numbersleft == 0:
        #print(res,"=?", prevRes)
        return res == prevRes
    else:
        return (isResPosssible(res, numList[1:], numbersleft-1, prevRes+numList[0])
            or isResPosssible(res, numList[1:], numbersleft-1, prevRes*numList[0])
            or isResPosssible(res, numList[1:], numbersleft-1, int(str(prevRes)+str(numList[0]))))

lines = open("input7.txt").readlines()

total = 0

for line in lines:
    res, nums = line.split(":")
    res = int(res)
    numList = [int(i) for i in nums[1:].split(" ")]
    if isResPosssible(res, numList[1:], len(numList)-1, numList[0]):
        total += res
        #print(line)

#print(41*7*265*5*242*994*7)
print(total)