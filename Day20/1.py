import numpy as np
from collections import Counter

with open('input.txt','r') as f:
    data=f.read().splitlines()

arr=[]
for i,line in enumerate(data):
    arr.append((i,int(line)))

l=len(arr)

for i in range(l):
    for k,(j,v) in enumerate(arr):
        if i==j:
            del arr[k]
            r=(k+v)%(l-1)
            arr.insert(r,(j,v))
            break

vals = [v for _,v in arr]
ind = vals.index(0)
print(vals[(ind+1000)%l]+vals[(ind+2000)%l]+vals[(ind+3000)%l])
