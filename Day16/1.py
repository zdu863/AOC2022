from collections import deque
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
    # print(a,b)
    valve,rate = a.split('hasflowrate=')
    valve = valve[-2:]
    rate = int(rate)
    # print(valve,rate)
    child = b.split(',')
    # print(child)
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
for node in flow:
    dist[node] = bfs(node)

ans = 0
cur = 0
left = set(useful)

def backtrack(t,node):
    global cur,ans
    if t>=29:
        return
        
    if flow[node]!=0:
        t+=1
        cur+=flow[node]*(30-t)
        ans = max(ans,cur)
        
    for c in left.copy():
        if c in dist[node]:
            left.remove(c)
            backtrack(t+dist[node][c],c)
            left.add(c)
    
    if flow[node]!=0:
        
        cur-=flow[node]*(30-t)
        t-=1

backtrack(0,start)
print(ans)
