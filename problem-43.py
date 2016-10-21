primes = [3,5,7,11,13,17]

def multsInRange(mult, start):
    num = start
    if start % mult != 0:
        num = start + (mult - start % mult)
    while num < start + 10:
        yield num
        num += mult
    raise StopIteration

class multGen(object):
    def __init__(self, mult, max):
        self.mult = mult
        self.n = -1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        self.n = self.n + 1
        if self.n * self.mult > self.max:
            raise StopIteration
        else:
            return self.n * self.mult

nums = [] # holds numbers found

def recMultCheck(layer, num, boolArr):
    for d in multsInRange(primes[layer], (num % 100) * 10):
        if not boolArr[d % 10]:
          newArr = list(boolArr)
          newArr[d % 10] = True
          if layer == len(primes) - 1:
              nums.append(num * 10 + (d % 10))
          else:
              recMultCheck(layer + 1, num * 10 + (d % 10), newArr)

for d in range(0,10):
    boolArray = [False,False,False,False,False,False,False,False,False,False]
    boolArray[d] = True
    for d1 in multGen(2,999):
        _d1 = str(d1).zfill(3)
        if not boolArray[int(_d1[0])] and not boolArray[int(_d1[1])] and not boolArray[int(_d1[2])] and _d1[0] != _d1[1] and _d1[1] != _d1[2] and _d1[0] != _d1[2]:
            boolArr = list(boolArray)
            boolArr[d1 % 10] = True
            boolArr[d1 % 100 // 10] = True
            boolArr[d1 // 100] = True
            recMultCheck(0, d * 1000 + d1, boolArr)
            
print(nums)