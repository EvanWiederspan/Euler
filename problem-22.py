import re
import string
from functools import reduce
alphabet = {string.ascii_lowercase[i-1]: i for i in range(1,27)}

def wordScore(word):
    return reduce(lambda total, l: total + alphabet[l], word, 0)

# assumes this file exists
f = open("p022_names.txt", "r")

names = re.split(r'","|"', f.read())[1:-1]

names.sort()

sum = 0
for i in range(0,len(names)):
    sum += (i+1) * wordScore(names[i].lower())
print(sum)

