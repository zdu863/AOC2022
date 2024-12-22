from collections import defaultdict

with open('input.txt','r') as f:
    data=f.read().splitlines()


# it = [20,60,100,140,180,220]
x = 1
cycle=1

screen = [['.' for _ in range(40)] for _ in range(6)]
r,c = (cycle-1)//40,(cycle-1)%40
if c in [x-1,x,x+1]:
    screen[r][c]='#'

for line in data:
    ins,*_ = line.split(' ')
    if ins=='noop':
        cycle+=1
        r,c = (cycle-1)//40,(cycle-1)%40
        if c in [x-1,x,x+1]:
            screen[r][c]='#'
    elif ins=='addx':
        _,num = line.split(' ')
        num = int(num)
        cycle+=1
        r,c = (cycle-1)//40,(cycle-1)%40
        if c in [x-1,x,x+1]:
            screen[r][c]='#'
        cycle+=1
        x+=num
        r,c = (cycle-1)//40,(cycle-1)%40
        if c in [x-1,x,x+1]:
            screen[r][c]='#'
    if cycle>=240:
        break

for r in screen:
    print(''.join(r))
