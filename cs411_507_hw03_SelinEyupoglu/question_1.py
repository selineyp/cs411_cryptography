import binascii
import random

# It clocks the LFSR once;
# Note that it changes LFSR state S
# S[0] is the leftmost bit of the LFSR
# The connection polynomial setting example:
# 1+x+x^3 --> C[0] = C[1} = C[3} = 1, C[2] = 0

def LFSR(C, S):
    L = len(S)
    fb = 0
    out = S[L-1]
    for i in range(0,L):
        fb = fb^(S[i]&C[i+1])
    for i in range(L-1,0,-1):
        S[i] = S[i-1]

    S[0] = fb
    return out

# Finds the period of a binary sequence s, if it repeates itself
# Note that the number of bits in s must be twice the size of the period
def FindPeriod(s):
    n = len(s)
    for T in range(1,n+1):
        chck = 0
        for i in range(0,n-T-1):
            if (s[i] != s[i+T]):
                chck += 1
                break
        if chck == 0:
            break
    if T > n/2:
        return n
    else:
        return T

s = [1,0,0,0,0,0]
c = [1,1,0,0,0,0,1]
sr='100000'
print(FindPeriod(c))
i=0

for k in range(0,6):
    xor=LFSR(c,s)
    sr = str(xor) + sr[:-1]
    print(sr)
