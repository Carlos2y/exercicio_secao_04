from collections import defaultdict

def MMC(lista):
    
    """

    Recive a list of numbers and build a defaultdict(list) by saving all
    multiples up to ( n * 1000 ) as values and the numbers ( lista ) as keys
    and using a simple cont ( c ) look through all numbers and all the keys
    until ( c == len(v) ) meaning MMC has been found.

    """
    
    v = defaultdict(list)
    c = 0
    m = 0

    for item in lista:
        for i in range(1000):
            v[item].append((item*i))

    for x in v.values():
        for i in x:
            if i == 0:
                continue
            for k in range(len(v)):
                if i in v[lista[k]]:
                    c += 1
                    m = i
                else:
                    c -= 1

            if c == len(v):
                return m
                break
            else:
                c = 0
