import numpy as np
import re
with open('input.txt') as f:
    data=f.read().splitlines()

mm = max(len(l) for l in data)
mat = []
for line in data:
    l = list(line)+[' ']*(mm-len(line))
    mat.append(l)
nn = len(mat)

for r in mat:
    print(''.join(r))
    print(len(r))
print(len(mat))

start = -1
for i,v in enumerate(mat[0]):
    if v!=' ':
        start = i
        break

with open('instructions.txt') as f:
    data=f.read().splitlines()
    
inst = data[0]
inst+=' '
i,j = 0,start
di,dj = 0,1

def turn(di,dj,dirc):
    if dirc == 'R':
        return dj,-di
    return -dj,di

# print(nn,mm)

steps = map(int,re.split('R|L', inst))
dircs = [c for c in inst if not c.isdigit()]

for l,c in zip(steps,dircs):
    stp = l
    while stp:
        oi,oj = i,j
        
        i+=di
        j+=dj
        if not 0<=i<nn:
            i=nn-abs(i)
        if not 0<=j<mm:
            j=mm-abs(j)
        
        while mat[i][j]==' ':
            print(i,j)
            i+=di
            j+=dj
            if not 0<=i<nn:
                i=nn-abs(i)
            if not 0<=j<mm:
                j=mm-abs(j)
                
        print(i,j)
        if mat[i][j]=='#':
            i,j=oi,oj
            break
        
        stp-=1
    if c!=' ':
        di,dj=turn(di,dj,c)

# print(i,j,di,dj)

def face(di,dj):
    if di==0 and dj==1:
        return 0
    if di==1 and dj==0:
        return 1
    if di==0 and dj==-1:
        return 2
    if di==-1 and dj==0:
        return 3
    
print(1000*(i+1)+4*(j+1)+face(di,dj))
