with open('input.txt','r') as f:
    data=f.read().splitlines()

coors = set()
for line in data:
    x,y,z = map(int,line.split(','))
    # print(x,y,z)
    coors.add((x,y,z))

delta = [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]
ans = 0
for x,y,z in coors:
    for i,j,k in delta:
        nx,ny,nz = x+i,y+j,z+k
        if (nx,ny,nz) not in coors:
            ans+=1
            
print(ans)
