def triangles():
    val = 1
    i = 1
    while True:
        yield val
        i += 1
        val += i

divisors = {1:{1}, 2:{1,2}, 3:{1,3}, 4:{1,2,4}}

def getDivisors():
    divs = list()
    i=0
    for num in triangles():
        if i > 10000:
            divs.append(num)
        else:
            i += 1
        if len(divs) > 100:
            break
    print(divs)

getDivisors()

