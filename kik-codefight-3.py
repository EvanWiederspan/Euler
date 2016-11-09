import time
from collections import Counter
from datetime import datetime

def getNext(sent, received):
    i = 0
    j = 0
    sentLen = len(sent)
    recLen = len(received)
    while True:
        if i >= sentLen and j >= recLen:
            raise StopIteration
            break
        if i >= sentLen or (j < recLen and received[j][0] <= sent[i][0]):
            yield (received[j], False, j)
            j += 1
        elif j >= recLen or  (i < sentLen and sent[i][0] < received[j][0]):
            yield (sent[i], True, i)
            i += 1

def getCount(userDict, key, default):
    if key not in userDict:
        userDict[key] = default
        return default
    else:
        return userDict[key]

def getDate(timestamp):
    return datetime.fromtimestamp(timestamp).strftime("%Y:%M:%d")

def rateLimit(sentBatches, receivedMessages, startingAllowance):
    counts = dict()
    failed = []
    lastDate = "0"
    for (batch, sent, pos) in getNext(sentBatches, receivedMessages):
        if getDate(batch[0]) != lastDate:
            lastDate = getDate(batch[0])
            for k in counts.keys():
                counts[k] = startingAllowance
        if sent:
            for i in range(1,len(batch)):
                if getCount(counts, batch[i], startingAllowance) == 0:
                    failed.append(pos)
                    break
            else:
                for j in range(1,len(batch)):
                    counts[batch[j]] -= 1

        else: # received
            for rec in batch[1:]:
                counts[rec] = getCount(counts, rec, startingAllowance) + 1
    return failed
 
rateLimit([[1,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,98,99], 
 [2,1,2], 
 [3,1,25], 
 [4,12,15,25,35,55], 
 [86400,1,2], 
 [86401,1,2,3,77,88,99], 
 [1471046399,1,2,3,55,77,88,99], 
 [1471046400,1,2,3,77,88,99], 
 [1471046401,2,3,6]], [[4,1], 
 [1471046432,3], 
 [1471046433,55], 
 [1471046434,1], 
 [1471046435,99], 
 [1471046436,4]], 2)