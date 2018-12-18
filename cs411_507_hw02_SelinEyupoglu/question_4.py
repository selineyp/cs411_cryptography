import math

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

def findroots(a,b,n):
    k=math.gcd(a,n)
    if(k==1):
        print('here is the unique solution:' + str((modinv(a,n)*b)%n))
    elif(b%k==0):
        if(math.gcd(a//k,n//k)==1):
            i=0
            while(i<k):
                m=(modinv(a//k,n//k)*(b//k))%(n//k)
                print('here is one:' + str(m+(i*n//k)))
                i+=1
    else:
        print('there is no solution')

n = 876757185537497549441688380876
a1 = 726529482843138430251706107365
b1 = 374479581720142608093094131318

a2 = 682523910410036363063715440006
b2 = 233807680780339430865969182340

a3 = 217662435485891894157847112298
b3 = 815512939769276810314824385915

print('root of 1st eq:')
findroots(a1,b1,n)
print('root of 2nd eq:')
findroots(a2,b2,n)
print('root of 3rd eq:')
findroots(a3,b3,n)
