import numpy as np
import re
from collections import defaultdict
with open('input.txt') as f:
    data=f.read().splitlines()

mat = []
for line in data:
    r = []
    for c in line:
        if c=='.':
            r.append(0)
        else:
            r.append(1)
    mat.append(np.array(r))

mat=np.array(mat)
# print(mat)
p_size = 200
mat = np.pad(mat , ((p_size, p_size),(p_size,p_size)), 'constant', constant_values=((0,0),(0,0)))
# print(mat.shape)
# print(mat)

rules = [[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)],[(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)]]
dirc = [(-1,0),(1,0),(0,-1),(0,1)]
ind=0

m,n = mat.shape
for tt in range(1000):
    moved = False

    tmp = np.zeros_like(mat)
    origin = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if mat[i][j]==1:
                found=0
                if np.sum(mat[i-1:i+2,j-1:j+2])>1:
                    for k in range(4):
                        if all(mat[i+di][j+dj]==0 for di,dj in rules[(ind+k)%4]):
                            moved=True
                            found=1
                            dir_i,dir_j=dirc[(ind+k)%4]
                            tmp[i+dir_i][j+dir_j]+=1
                            origin[(i+dir_i,j+dir_j)].append((i,j))        
                            break
                            
                if not found:
                    tmp[i][j]=1
    if not moved:
        print(tt+1)
        break
                        
    for i in range(m):
        for j in range(n):
            if tmp[i][j]>1:
                tmp[i][j]=0
                for oi,oj in origin[(i,j)]:
                    tmp[oi][oj]=1
    mat = np.copy(tmp)    
    ind+=1
