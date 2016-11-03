'''
Finds the number between 1 and 1,000,000 that has the longest Collatz sequence
Basically run through every number from 1 to 1,000,000 and calculate the length
of its collatz sequence to reach 0. Uses a dict as a map to cache previously calculated
run lengths

I am not super happy with this one, it runs and gives the correct answer but it
takes almost half a minute and the memory cost of the dict is probably insane

Possible speed ups, only iterate over odd numbers? The answer is an odd number, but
i am not sure that I can prove that the answer has to be odd

After looking at the Euler threads, it appears that other coders were able to do a
complete brute force solution (they didnt use a cache like I did) in C and get an answer in under a second
Mine may just take a long time because it is Python
'''

numMap = {4: 2, 2: 1, 1: 0}
numStack = []
maxTrail = 1
maxNum = 0

# loop through all nums
for i in range(3, 1000000, 2):
    n = i
    while n not in numMap:
        numStack.append(n)
        if n % 2 == 0: # if its even
            n = n // 2
        else:
            n = (3 * n) + 1

    linkCount = numMap[n] + len(numStack)
    if linkCount > maxTrail:
        maxNum = numStack[0]
        maxTrail = linkCount
    for num in numStack:
        numMap[num] = linkCount
        linkCount -= 1
    numStack.clear()
print(maxNum)