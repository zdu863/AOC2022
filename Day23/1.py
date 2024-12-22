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
print(mat)
p_size = 30
mat = np.pad(mat , ((p_size, p_size),(p_size,p_size)), 'constant', constant_values=((0,0),(0,0)))
print(mat.shape)
# print(mat)

rules = [[(-1,-1),(-1,0),(-1,1)],[(1,-1),(1,0),(1,1)],[(-1,-1),(0,-1),(1,-1)],[(-1,1),(0,1),(1,1)]]
dirc = [(-1,0),(1,0),(0,-1),(0,1)]
ind=0

m,n = mat.shape
for _ in range(10):
    tmp = np.zeros_like(mat)
    origin = defaultdict(list)
    for i in range(m):
        for j in range(n):
            if mat[i][j]==1:
                found=0
                if np.sum(mat[i-1:i+2,j-1:j+2])>1:
                    for k in range(4):
                        if all(mat[i+di][j+dj]==0 for di,dj in rules[(ind+k)%4]):
                            found=1
                            dir_i,dir_j=dirc[(ind+k)%4]
                            tmp[i+dir_i][j+dir_j]+=1
                            origin[(i+dir_i,j+dir_j)].append((i,j))        
                            break
                if not found:
                    tmp[i][j]=1
                        
    for i in range(m):
        for j in range(n):
            if tmp[i][j]>1:
                tmp[i][j]=0
                for oi,oj in origin[(i,j)]:
                    tmp[oi][oj]=1
    mat = np.copy(tmp)    
    ind+=1

infi = 9999
max_i,min_i,max_j,min_j = -infi,infi,-infi,infi
for i in range(m):
    for j in range(n):
        if mat[i][j]==1:
            max_i = max(max_i,i)
            min_i = min(min_i,i)
            max_j = max(max_j,j)
            min_j = min(min_j,j)

print(np.sum(1-mat[min_i:max_i+1,min_j:max_j+1]))
print(mat[min_i:max_i+1,min_j:max_j+1])


# for r in mat:
    # print(''.join(str(c) for c in r))

# mm = max(len(l) for l in data)
# mat = []
# for line in data:
#     l = list(line)+[' ']*(mm-len(line))
#     mat.append(l)
# nn = len(mat)
# 
# for r in mat:
#     print(''.join(r))
#     print(len(r))
# print(len(mat))
# 
# start = -1
# for i,v in enumerate(mat[0]):
#     if v!=' ':
#         start = i
#         break
# 
# with open('instructions.txt') as f:
#     data=f.read().splitlines()
# 
# inst = data[0]
# inst+=' '
# i,j = 0,start
# di,dj = 0,1
# 
# def turn(di,dj,dirc):
#     if dirc == 'R':
#         return dj,-di
#     return -dj,di
# 
# # print(nn,mm)
# 
# steps = map(int,re.split('R|L', inst))
# dircs = [c for c in inst if not c.isdigit()]
# 
# for l,c in zip(steps,dircs):
#     stp = l
#     while stp:
#         oi,oj = i,j
# 
#         i+=di
#         j+=dj
#         if not 0<=i<nn:
#             i=nn-abs(i)
#         if not 0<=j<mm:
#             j=mm-abs(j)
# 
#         while mat[i][j]==' ':
#             print(i,j)
#             i+=di
#             j+=dj
#             if not 0<=i<nn:
#                 i=nn-abs(i)
#             if not 0<=j<mm:
#                 j=mm-abs(j)
# 
#         print(i,j)
#         if mat[i][j]=='#':
#             i,j=oi,oj
#             break
# 
#         stp-=1
#     if c!=' ':
#         di,dj=turn(di,dj,c)
# 
# # print(i,j,di,dj)
# 
# def face(di,dj):
#     if di==0 and dj==1:
#         return 0
#     if di==1 and dj==0:
#         return 1
#     if di==0 and dj==-1:
#         return 2
#     if di==-1 and dj==0:
#         return 3
# 
# print(1000*(i+1)+4*(j+1)+face(di,dj))
