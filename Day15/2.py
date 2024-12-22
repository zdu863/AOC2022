from time import time

ts = time()

with open('input.txt','r') as f:
    data=f.read().splitlines()

d_max = 4000000

ss = []
bb = []
for line in data:
    l = line.replace(' ','')
    _, l = l.split('Sensorat')
    s,b = l.split(':closestbeaconisat')
    
    sx,sy = s.split(',')
    sx = int(sx.split('=')[1])
    sy = int(sy.split('=')[1])
    ss.append([sx,sy])
    
    bx,by = b.split(',')
    bx = int(bx.split('=')[1])
    by = int(by.split('=')[1])
    bb.append([bx,by])    

for ry in range(d_max+1):
    intervals = []
    for (sx,sy),(bx,by) in zip(ss,bb):
        delta = abs(bx-sx)+abs(by-sy)-abs(ry-sy)
        if delta<0:
            continue
        lower = sx - delta
        upper = sx + delta
        intervals.append([lower,upper])
    intervals.sort()

    ans = 0
    start = 0
    end = start-1
    
    for s,e in intervals:
        if s>d_max:
            break
        if s>end:
            ans += end-start+1
            start = max(0,s)
            end = min(e,d_max)
        else:
            end = min(max(e,end),d_max)
            
    ans += end-start+1
    

    if d_max == ans:
        start = 0
        end = start-1
        
        rx=0
        for s,e in intervals:
            if s>d_max:
                break
            if s>end:
                if s-end==2:
                    rx=s-1
                ans += end-start+1
                start = max(0,s)
                end = min(e,d_max)
            else:
                end = min(max(e,end),d_max)
        print(rx,ry)
        print(rx*4000000+ry)
        break
        
print(time() - ts)
