import timeit
import time
from decimal import *


p= 10106404377238244429826597333701722135807526565404559030730896339579442857374388664504194768519009799965064145557030402164596983123568189834021494235031749
q= 13163502274590772696691357017188157383494073914454743555560229941893711785933411409679348168803213122008986323048364979277888128708485862429032314868646957
c= 86558429746256786220797160070602630299194622171442102432718868178774008203963283371082296312613592328933331443800737112868177768290770644915753506516969943009267919574620060086036513229518287908509845029476546407334692827450859273444583008387805272482776780230890488254799112954960574416568539455497347050126
e = 67
n=p*q
#Compute m = c^d  mod n  (where d = e-1 mod φ(n)).

def modInverse(a, m) :
    a = a % m;
    for x in range(1, m) :
        if ((a * x) % m == 1) :
            return x
    return 1

def findQElts(num):
    els=[]
    for i in range(1,num):
        if(gcd(num,i)==1):
            els.append(i)
    return els


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


#print(e%((p-1)*(q-1)))

d=int(modinv(e,((p-1)*(q-1))))
dp=d%(p-1)
dq=d%(q-1)
a1=pow(c, dp, p)
a2=pow(c, dq, q)
qinv=modinv(q, p)
pinv=modinv(p, q)
cp=c%p
cq=c%q
x=[]
iter=100
for i in range(0,iter):
    startcrt=time.time()
    h=(qinv*(a1-a2))%p
    m=a2+h*q
    endcrt=time.time()
    x.append(endcrt-startcrt)
print('avg time that crt takes ' + str(Decimal(sum(i for i in x)/100)))
print('result is ' + str(m))
print('cp^dp '+str(pow(cp,dp,p)))
print('cq^dq '+str(pow(cq,dq,q)))
iter=100
t1=time.time()
y=[]
for i in range(0,iter):
    pow(c,d,n)
    t2=time.time()
    y.append(t2-t1)
print('avg time that regular computation takes ' + str(sum(i for i in y)/100))
