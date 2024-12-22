from collections import deque
import math
with open('input.txt','r') as f:
    data=f.read().splitlines()

adj = {}
flow = {}
for line in data:
    l = line.replace(' ','')
    try:
        a,b  =l.split(';tunnelsleadtovalves')
    except:
        a,b  =l.split(';tunnelleadstovalve')

    valve,rate = a.split('hasflowrate=')
    valve = valve[-2:]
    rate = int(rate)
    
    child = b.split(',')
    
    adj[valve] = child
    flow[valve] = rate

start='AA'

useful = []
for k,v in flow.items():
    if v!=0:
        useful.append(k)

def bfs(node):
    q = deque([(node,0)])
    dist = {node:0}
    visited = {node}
    while q:
        n,d = q.popleft()
        for c in adj[n]:
            if c not in visited:
                visited.add(c)
                q.append((c,d+1))
                if c in useful:
                    dist[c]=d+1
    return dist
    
dist = {}
for node in ['AA']+useful:
    dist[node] = bfs(node)

def backtrack(t,node):
    global cur,ans
    if t>=25 or not left:
        return
        
    if flow[node]!=0:
        t+=1
        cur+=flow[node]*(26-t)
        ans = max(ans,cur)
        
    for c in left.copy():
        if c in dist[node]:
            left.remove(c)
            backtrack(t+dist[node][c],c)
            left.add(c)
    
    if flow[node]!=0:
        cur-=flow[node]*(26-t)
        t-=1


aaa = []
tot = 2**len(useful)
for msk in range(tot):
    left=set()
    for i in range(len(useful)):
        if (1<<i)&msk:
            left.add(useful[i])
    ans = 0
    cur = 0
    backtrack(0,start)
    aaa.append(ans)
    if math.floor(100*msk/tot)-math.floor(100*(msk-1)/tot)==1:
        print(f'{math.floor(100*msk/tot)}% done')

res = 0
for msk in range(2**len(useful)):
    res = max(res,aaa[msk]+aaa[2**len(useful)-1-msk])
print(res)
