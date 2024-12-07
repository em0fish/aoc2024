dico = {}
total = 0
info = open("input5.txt").read()
rules, updates = info.split("\n\n")

def switchy(nums, i, j):
    nums[i],nums[j] = nums[j], nums[i]
    return nums

# checks if an update is correct.
# returns: 
# bool add - correctness of the update
# int inc_ind1, inc_ind2 - indexes of the numbers 
#   that cause the update to be incorrect. both set 
#   to -1 if the update is correct
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


for line in rules.split("\n"):
    a,b = line.split("|")
    if a not in dico.keys():
        dico[a] = [b]
    else:
        dico[a] += [b]

def part1(updates):
    total = 0
    for line in updates.split("\n"):
        nums = line.split(",")
        add,_,_ = checkline(nums)
        if add:
            total += int(nums[(len(nums)-1)//2])
    return total

def part2(updates):
    total = 0
    for line in updates.split("\n"):
        nums = line.split(",")
        add,ind1,ind2 = checkline(nums)
        if not add:
            while add == False:
                nums = switchy(nums, ind1, ind2)
                add, ind1, ind2 = checkline(nums)
            total += int(nums[(len(nums)-1)//2])
    return total