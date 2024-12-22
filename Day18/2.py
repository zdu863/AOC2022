with open('input.txt','r') as f:
    data=f.read().splitlines()
    
import sys
sys.setrecursionlimit(150000)

coors = set()
for line in data:
    x,y,z = map(int,line.split(','))
    coors.add((x,y,z))
    
# for i in range(3):
#     print(min(it[i] for it in coors),max(it[i] for it in coors))
    # print()

delta = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]

#[-5,25]
v_min,v_max = -5,25
visited = set()
def dfs(x,y,z):
    if (x,y,z) in visited:
        return
    visited.add((x,y,z))
    for dx,dy,dz in delta:
        nx,ny,nz = x+dx,y+dy,z+dz
        if v_min<=nx<=v_max and v_min<=ny<=v_max and v_min<=nz<=v_max and (nx,ny,nz) not in coors:
            dfs(nx,ny,nz)

dfs(-5,-5,-5)

ans=0            
for x,y,z in visited:
    for i,j,k in delta:
        nx,ny,nz = x+i,y+j,z+k
        if (nx,ny,nz) in coors:
            ans+=1
print(ans)
