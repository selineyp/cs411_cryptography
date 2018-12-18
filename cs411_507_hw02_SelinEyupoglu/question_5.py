from operator import xor
out=[]
def lfsr(seed, taps):
    import time
    sr, xor = seed, 0
    l=len(seed)
    i=0
    print('states of the LSFR:')
    while i<50:
        for t in taps:
            xor += int(sr[t-1])
        if xor%2 == 0.0:
            xor = 0
        else:
            xor = 1
        print(xor)
        print
        time.sleep(0.5)
        sr, xor = str(xor) + sr[:-1], 0
        print(sr)
        print
        time.sleep(0.5)
        i+=1

lfsr('100000',(6,5))
#lfsr('11001001', (8,7,6,1))
