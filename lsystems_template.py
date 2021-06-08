#!/usr/bin/python3

def applyRules(lhch):
    rhstr = ""
    if lhch == "A":
        rhstr = "B"    # RULE 1
    elif lhch == "B":
        rhstr = "AB"   # RULE 2
    else:
        rhstr = lhch    # no rules apply so keep the character
    return rhstr

def processString(oldStr):
    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)

    return newstr

def createLSystem(numIters,axiom):
    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString

    return endString


print(createLSystem(4, "A"))