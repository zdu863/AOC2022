from collections import deque

with open('input.txt','r') as f:
    data=f.read().splitlines()

import string
a = list(string.ascii_lowercase)
d = dict(zip(a,range(26)))

grid=[]
sx,sy = 0,0
ex,ey = 0,0
for i,line in enumerate(data):
    grid.append([])
    for j,c in enumerate(line):
        if c=='S':
            sx,sy = i,j
            grid[i].append(0)
        elif c=='E':
            ex,ey = i,j
            grid[i].append(25)
        else:
            grid[i].append(d[c])

m,n=len(grid),len(grid[0])

visited=[[0 for _ in range(n)] for _ in range(m)]

q = deque([(sx,sy,0)])

while q:
    x,y,dist = q.popleft()
    for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
        X,Y=x+dx,y+dy
        if 0<=X<m and 0<=Y<n and grid[X][Y]<=grid[x][y]+1 and (not visited[X][Y]):
            visited[X][Y]=1
            q.append((X,Y,dist+1))
            if X==ex and Y==ey:
                print(dist+1)
