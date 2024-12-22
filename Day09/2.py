with open('input.txt','r') as f:
    data=f.read().splitlines()

dirc = {'U':(-1,0),'L':(0,-1),'D':(1,0),'R':(0,1)}

snake = [[0,0] for _ in range(10)]

visited=set()

for line in data:
    d,l = line.split(' ')
    l = int(l)
    for _ in range(l):
        dx,dy = dirc[d]
        snake[0][0]+=dx
        snake[0][1]+=dy 
        for ind in range(1,10):
            tx,ty = snake[ind]
            hx,hy = snake[ind-1]
            del_x = abs(hx-tx)
            del_y = abs(hy-ty)
            if del_x<=1 and del_y<=1:
                pass
            elif del_x==2 and del_y==0:
                tx+= (hx-tx)//del_x
            elif del_x==0 and del_y==2:
                ty+= (hy-ty)//del_y
            elif (del_x==2 and del_y==1) or (del_x==1 and del_y==2) or (del_x==2 and del_y==2):
                tx+= (hx-tx)//del_x
                ty+= (hy-ty)//del_y
            else:
                print('wrong config')
                print(del_x,del_y)
            snake[ind] = [tx,ty]
            
        if tuple(snake[-1]) not in visited:
            visited.add(tuple(snake[-1]))

print(len(visited))
