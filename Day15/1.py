with open('input.txt','r') as f:
    data=f.read().splitlines()

ry=2000000
beacons = set()
intervals = []
for line in data:
    l = line.replace(' ','')
    _, l = l.split('Sensorat')
    s,b = l.split(':closestbeaconisat')
    
    sx,sy = s.split(',')
    sx = int(sx.split('=')[1])
    sy = int(sy.split('=')[1])
    
    bx,by = b.split(',')
    bx = int(bx.split('=')[1])
    by = int(by.split('=')[1])
    beacons.add((bx,by))
    
    delta = abs(bx-sx)+abs(by-sy)-abs(ry-sy)
    if delta<0:
        continue
    lower = sx - delta
    upper = sx + delta
    intervals.append([lower,upper])

intervals.sort()
# print(intervals)
ans = 0

start = -9999999999999
end = start-1

for s,e in intervals:
    if s>end:
        ans += end-start+1
        start = s
        end = e
    else:
        end = max(e,end)
        
ans += end-start+1

for bx,by in beacons:
    if by==ry:
        ans-=1
print(ans)
