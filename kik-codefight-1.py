import re
from fractions import Fraction
from collections import Counter

def findNot(arr, i, findString):
    length = len(arr)
    while (i < length and arr[i][0] == findString):
        i += 1
    return i

def spamDetection(messages, spamSignals):
    ret = []
    mesMap = dict()
    numMessages = len(messages)
    messages.sort(key=lambda x:x[0])
    lessFive = 0
    spamNum = 0
    spamWords = set()
    sameUsers = set()
    repeatWords = ""
    i=0
    for m in messages:
        if len(re.findall('\w ', m[0])) < 4:
            lessFive += 1
        subList = messages[i:findNot(messages,i,m[0])]
        if len(subList) > numMessages / 2 and numMessages > 2:
            repeatWords = m[0]
        if m[1] not in mesMap:
            mesMap[m[1]] = list()
        mesMap[m[1]].append(m[0])
        if len(spamSignals) > 0:
            reg = "\\b(" + ")\\b|\\b(".join(spamSignals) + ")\\b"
            words = [word for find in re.findall(reg, m[0], re.IGNORECASE) for word in find if word != ""]
            if len(words) > 0:
                spamNum += 1
            spamWords.update([str.lower(w) for w in words])
        i += 1
    
    for key, user in mesMap.items():
        num = len(user)
        maxSame = Counter(user).most_common(1)[0][1]
        if Fraction(maxSame, num) > 0.5 and num >= 2:
            sameUsers.add(key)
    
    lessRatio = 0
    spamRatio = 0
    if numMessages > 0:
        lessRatio = Fraction(lessFive, numMessages)
        spamRatio = Fraction(spamNum, numMessages)
    ret.append("passed" if lessRatio < 0.9 else "failed: " + str(lessRatio.numerator) + "/" + str(lessRatio.denominator))
    ret.append("passed" if len(sameUsers) == 0 else "failed: " + " ".join(sorted(list(sameUsers))))
    ret.append("passed" if repeatWords == "" else "failed: " + repeatWords)
    ret.append("passed" if spamRatio <= 0.5 else "failed: " + " ".join(sorted(list(spamWords))))
    return ret




        
spamDetection([["Sale today!", "2837273"],
            ["Unique offer!", "3873827"],
            ["Only today and only for you!", "2837273"],
            ["Sale today!", "2837273"],
            ["Unique offer!", "3873827"]], ["sale", "discount", "offer"])