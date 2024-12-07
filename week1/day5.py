dico = {}
total = 0

def switchy(nums, i, j):
    nums[i],nums[j] = nums[j], nums[i]
    return nums

def checkline(nums):
    add = True
    inc_ind1 = -1
    inc_ind2 = -1
    for i, e in enumerate(nums):
        if e not in dico.keys():
            continue
        for number in dico[e]:
            if number in nums and nums.index(number) < i:
                add = False
                inc_ind1 = i
                inc_ind2 = nums.index(number)
                break
        if not add:
            break 
    return [add, inc_ind1, inc_ind2]

info = open("input5.txt").read()

part1, part2 = info.split("\n\n")

for line in part1.split("\n"):
    a,b = line.split("|")
    if a not in dico.keys():
        dico[a] = [b]
    else:
        dico[a] += [b]

print(dico)

for line in part2.split("\n"):
    nums = line.split(",")
    add,ind1,ind2 = checkline(nums)
    if not add:
        print(line)
        while add == False:
            nums = switchy(nums, ind1, ind2)
            add, ind1, ind2 = checkline(nums)
        total += int(nums[(len(nums)-1)//2])

print(total)