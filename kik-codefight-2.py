import re

def kikCode(userId):
    id = bin(int(userId))[2:].zfill(52)[::-1]
    ret = []
    splitVals = [0,3,7,15,25,37,52]
    for i in range(1,7):
        sectors = []
        bits = id[splitVals[i-1]:splitVals[i]]
        angleUnit = 360 // (splitVals[i] - splitVals[i-1])
        for match in re.finditer("1+", bits):
            start = int(match.start())
            end = int(match.end())
            sectors.append([i, start * angleUnit])
            sectors.append([i, (start*angleUnit + (end - start) * angleUnit) % 360])
        if len(sectors) > 0 and sectors[-1][1] >= sectors[0][1] and sectors[-1][1] <= sectors[1][1]:
            if len(sectors) > 2:
                sectors[-1][1] = 360 + sectors[1][1]
                sectors.pop(0)
                sectors.pop(0)
            elif sectors[-1][1] == 0:
                sectors[-1][1] = 360
        if len(sectors) > 0 and sectors[-1][1] == 0:
            sectors[-1][1] = 360
        for j in range(0, len(sectors), 2):
            ret.append([sectors[j], sectors[j+1]])
    return ret


kikCode("1851027803204441")