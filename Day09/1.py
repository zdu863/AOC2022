with open('input.txt','r') as f:
    data=f.read().splitlines()

dirc = {'U':(-1,0),'L':(0,-1),'D':(1,0),'R':(0,1)}


hx,hy=0,0
tx,ty=0,0
visited=set()

for line in data:
    d,l = line.split(' ')
    l = int(l)
    for _ in range(l):
        dx,dy = dirc[d]
        hx+=dx
        hy+=dy 
        del_x = abs(hx-tx)
        del_y = abs(hy-ty)
        if del_x<=1 and del_y<=1:
            pass
        elif del_x==2 and del_y==0:
            tx+= (hx-tx)//del_x
        elif del_x==0 and del_y==2:
            ty+= (hy-ty)//del_y
        elif (del_x==2 and del_y==1) or (del_x==1 and del_y==2):
            tx+= (hx-tx)//del_x
            ty+= (hy-ty)//del_y
        else:
            print('wrong config')
        if (tx,ty) not in visited:
            visited.add((tx,ty))
# print(visited)
print(len(visited))
