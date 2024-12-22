from collections import defaultdict

with open('input.txt','r') as f:
    data=f.read().splitlines()


it = [20,60,100,140,180,220]
x = 1
cycle=1
ans=0
for line in data:
    ins,*_ = line.split(' ')
    if ins=='noop':
        cycle+=1
        if cycle in it:
            ans+=x*cycle
            # print(cycle,x)
    elif ins=='addx':
        _,num = line.split(' ')
        num = int(num)
        cycle+=1
        if cycle in it:
            ans+=x*cycle
            # print(cycle,x)
        cycle+=1
        x+=num
        if cycle in it:
            ans+=x*cycle
            # print(cycle,x)

print(ans)
