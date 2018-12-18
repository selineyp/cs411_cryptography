import numpy as np
p1=[1,1,0,1,0,1,0,0]
p2=[1,0,0,0,1,1,1,1]
p3=np.polymul(p1,p2)
p4=[1,0,0,0,1,1,0,1,1]
div,rem = np.polydiv(p3,p4)
res=[]
for i in rem:
    res.append((i+2) % 2)
#print(p3)
print(np.poly1d(res))
#print(rem)

#part b
p1=[1,1,0,1,0,1,0,0]
p2=[1,1,0,0,0,1,0,1]
p3=np.polymul(p1,p2)
div,rem = np.polydiv(p3,p4)
res=[]
for i in rem:
    res.append((i+2) % 2)
#print(p3)
print(np.poly1d(rem))
