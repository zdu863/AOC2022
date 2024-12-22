from heapq import *

with open('input.txt','r') as f:
    data=f.read().splitlines()

import string
a = list(string.ascii_lowercase)
d = dict(zip(a,range(26)))

grid=[]
start = []
end = []
for i,line in enumerate(data):
    grid.append([])
    for j,c in enumerate(line):
        if c=='S':
            start = [i,j]
            grid[i].append(0)
        elif c=='E':
            end = [i,j]
            grid[i].append(25)
        else:
            grid[i].append(d[c])

m,n=len(grid),len(grid[0])

visited=[[0 for _ in range(n)] for _ in range(m)]
dist=[[10**10 for _ in range(n)] for _ in range(m)]

ex,ey = end
dist[ex][ey]=0

q=[(0,ex,ey)]
while q:
    _,x,y = heappop(q)
    if not visited[x][y]:
        visited[x][y]=1
        for dx,dy in [(0,1),(1,0),(-1,0),(0,-1)]:
            X,Y=x+dx,y+dy
            if 0<=X<m and 0<=Y<n and grid[X][Y]>=grid[x][y]-1 and dist[X][Y]>dist[x][y]+1:
                dist[X][Y]=dist[x][y]+1
                heappush(q,(dist[X][Y],X,Y))

ans = 10000000
for i in range(m):
    for j in range(n):
        if grid[i][j]==0 and dist[i][j]<ans:
            ans = dist[i][j]
        # print(dist[sx][sy])
print(ans)
