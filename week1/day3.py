# checks the format and it its correct, returns the value of mul(a,b)
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

### part 2
# throw out all segments between don't() and do() as theyre not counted
while True:
    ind1 = inString.find("don't()")
    if ind1 == -1:
        break
    ind2 = inString.find("do()", ind1)
    if ind2 == -1:
        inString = inString[:ind1]
        break
    inString = inString[:ind1] + inString[(ind2+4):]
### part 2 end


out = 0
while True:
    ind1 = inString.find("mul(")
    inString = inString[ind1:]
    ind2 = inString.find(")")
    if ind1 == -1 or ind2 == -1: break
    if ind2-4 < 3 or ind2-4 > 8: 
        inString = inString[4:]
        continue
    res = splitter(inString[4:ind2])
    if res != -1: 
        out += res
    inString = inString[ind2:]