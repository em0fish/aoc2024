def splitter(s):
    #print(s)
    l = s.split(",")
    # no comma
    if len(l) != 2: return -1
    for e in l:
        if any([ord("9") < ord(c) or ord(c) < ord("0") for c in e]):
            return -1
    return int(l[0])*int(l[1])

inString = open("input3.txt").read()

while True:
    #print("--------------")
    #print(len(inString))
    ind1 = inString.find("don't()")
    if ind1 == -1:
        break
    ind2 = inString.find("do()", ind1)
    if ind2 == -1:
        inString = inString[:ind1]
        break
    print("ind1: ", ind1, "ind2: ", ind2)
    inString = inString[:ind1] + inString[(ind2+4):]

# - find "don't()" => ind1
#     - if ind1 == -1: 
#         break
# - find "do()" => ind2
#     - if ind2 == -1:
#           inString = inString[ind1:]
#           break 
# - inString = inString[:ind1] + inString[ind2:]

out = 0
while True:
    #print(inString)
    ind1 = inString.find("mul(")
    inString = inString[ind1:]
    ind2 = inString.find(")")
    if ind1 == -1 or ind2 == -1: break
    #print("ind1: ",ind1,", ind2: ",ind2)
    if ind2-4 < 3 or ind2-4 > 8: 
        inString = inString[4:]
        continue
    res = splitter(inString[4:ind2])
    if res != -1: 
        out += res
    inString = inString[ind2:]

print(out)
## 190815282 - too high