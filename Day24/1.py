from collections import deque
from copy import deepcopy

with open('input.txt','r') as f:
    data=f.read().splitlines()

grid=[]
for i,line in enumerate(data):
    grid.append(list(line))

m,n=len(grid),len(grid[0])

# print(m,n)

sx,sy = 0,1
ex,ey = m-1,n-2

dirc = {'>':(0,1),'<':(0,-1),'^':(-1,0),'v':(1,0)}

for i in range(1,m-1):
    for j in range(1,n-1):
        if grid[i][j] in dirc:
            grid[i][j]=[grid[i][j]]

blizz=[deepcopy(grid)]

def update_blizz(blizz):
    grid = blizz[-1]
    m,n=len(grid),len(grid[0])
    tmp = deepcopy(grid)
    for i in range(1,m-1):
        for j in range(1,n-1):
            tmp[i][j]='.'
            
    for i in range(m):
        for j in range(n):
            if type(grid[i][j])==list:
                for c in grid[i][j]:
                    di,dj = dirc[c]
                    ni,nj = i+di,j+dj
                    if ni==0:
                        ni=m-2
                    elif nj==0:
                        nj=n-2
                    elif ni==m-1:
                        ni=1
                    elif nj==n-1:
                        nj=1
                        
                    if tmp[ni][nj]=='.':
                        tmp[ni][nj]=[c]
                    else:
                        tmp[ni][nj].append(c)
                        
    blizz.append(tmp)

visited=set()
q = deque([(sx,sy,0)])

found = False
while q:
    x,y,tt = q.popleft()
    while len(blizz)<tt+2:
        update_blizz(blizz)
    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1),(0,0)]:
        X,Y=x+dx,y+dy
        if 0<=X<m and 0<=Y<n and blizz[tt+1][X][Y]=='.' and ((X,Y,tt+1) not in visited):
            visited.add((X,Y,tt+1))
            q.append((X,Y,tt+1))
            if X==ex and Y==ey:
                found=True
                print(tt+1)
    if found:
        break
                
