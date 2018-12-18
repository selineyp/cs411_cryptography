
import collections
compare = lambda x, y: collections.Counter(x) == collections.Counter(y)

def findZElts(num):
    els=[]
    for i in range(1,num):
        if(gcd(num,i)==1):
            els.append(i)
    return els

def findQElts(num):
    els=set()
    for i in range(1,num):
        if(gcd(pow(i,2),num)==1):
            els.add(pow(i,2)%num)
    return els

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

def findZGens(num):
    els=set(findZElts(num))
    els1=set()
    gens=[]
    for x in els:
        for i in range(0,len(els)):
            if(pow(x,i)%num not in els1):
                els1.add(pow(x,i)%num)
            else:
                break
        if(compare(els,els1)):
            gens.append(x)
        els1.clear()
    return gens

def findQGens(num):
    els=set(findQElts(num))
    els1=set()
    gens=[]
    for x in els:
        for i in range(0,len(els)):
            if(pow(x,i)%num not in els1):
                els1.add(pow(x,i)%num)
            else:
                break
        if(compare(els,els1)):
            gens.append(x)
        els1.clear()
    return gens

print(findZElts(58))
print(findZGens(58))
print(findQElts(58))
print(findQGens(58))
