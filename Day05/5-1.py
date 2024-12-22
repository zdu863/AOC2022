import numpy as np
with open('input.txt','r') as f:
    data=f.read().splitlines()

with open('instructions.txt','r') as f:
    ins=f.read().splitlines()

mat = []    
for line in data:
    mat.append(list(line))

def move(a,b,num):
    a=a-1
    b=b-1
    for _ in range(num):
        mat[b].append(mat[a].pop())

for line in ins:
    l = line.replace(' ','')
    _,x= l.split('move')
    num,y = x.split('from')
    num=int(num)
    a,b = map(int,y.split('to'))
    move(a,b,num)

print(''.join(r[-1] for r in mat))
