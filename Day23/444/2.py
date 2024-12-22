#############
#...........#
###C#C#A#B###
  #D#C#B#A#
  #D#B#A#C#
  #D#D#B#A#
  #########

from collections import defaultdict
from heapq import heappush,heappop
from copy import copy,deepcopy
from time import time

start=time()

visited=set()
dist=defaultdict(lambda:10**9)

costs=[1,10,100,1000]
ini=((2,3,3,3),(2,2,1,3),(0,1,0,1),(1,0,2,0),(-1,-1),(-1,-1),(-1,-1,-1))
dist[ini]=0

def update(ns,s,w):
    global dist,q
    if dist[ns]>dist[s]+w:
        dist[ns]=dist[s]+w
        heappush(q,(dist[ns],ns))

# original or final
def ab(arr,ind):
    try:
        return [[-1,ind,ind,ind],[-1,-1,ind,ind],[-1,-1,-1,ind],[-1,-1,-1,-1],[ind,ind,ind,ind]].index(arr)
    except ValueError:
        return -1

# first non empty slot in a vertical line
def first(arr):
    for i,v in enumerate(arr):
        if v!=-1:
            return i,v
    return -1,-1
        
q=[(0,ini)]
while q:
    _,s = heappop(q)
    if s not in visited:
        visited.add(s)
        ls=[list(it) for it in s]
        *v,a,b,c=ls
        
        # moving out of a vertical line into a waiting spot
        for i in range(4):
            if ab(v[i],i)!=-1:
                continue
                
            j,val=first(v[i])
            for k in range(3):
                if all(it==-1 for it in c[i:k+1]+c[k:i]):
                    tmp=deepcopy(v); cc=copy(c);
                    tmp[i][j]=-1; cc[k]=val;
                    
                    ns=tmp+[a,b,cc]
                    ns=tuple(tuple(it) for it in ns)
                    update(ns,s,(j+2*(abs(k-i)+(k>=i)))*costs[val])
            
            #moving into the left and right ends
            for k in range(2):
                if a[k]!=-1:
                    break
                if all(it==-1 for it in c[:i]):
                    tmp=deepcopy(v); aa=copy(a);
                    tmp[i][j]=-1; aa[k]=val;
                    
                    ns=tmp+[aa,b,c]
                    ns=tuple(tuple(it) for it in ns)
                    update(ns,s,(j+2*(i+1)+k)*costs[val])
            
            for k in range(2):
                if b[k]!=-1:
                    break
                if all(it==-1 for it in c[i:]):
                    tmp=deepcopy(v); bb=copy(b);
                    tmp[i][j]=-1; bb[k]=val;
                    
                    ns=tmp+[a,bb,c]
                    ns=tuple(tuple(it) for it in ns)
                    update(ns,s,(j+2*(4-i)+k)*costs[val])
                    
        # moving out of a waiting spot into a vertical line
        
        # moving out of left side
        for k in range(2):
            if a[k]!=-1:
                i=a[k]
                j=ab(v[i],i)
                if j==-1:
                    break
                    
                if all(it==-1 for it in c[:i]):
                    tmp=deepcopy(v); aa=copy(a);
                    tmp[i][j]=i; aa[k]=-1;
                    
                    ns=tmp+[aa,b,c]
                    ns=tuple(tuple(it) for it in ns)
                    update(ns,s,(j+2*(i+1)+k)*costs[i])
                break
        
        # moving out of right side
        for k in range(2):
            if b[k]!=-1:
                i=b[k]
                j=ab(v[i],i)
                if j==-1:
                    break
                    
                if all(it==-1 for it in c[i:]):
                    tmp=deepcopy(v); bb=copy(b);
                    tmp[i][j]=i; bb[k]=-1;
                    
                    ns=tmp+[a,bb,c]
                    ns=tuple(tuple(it) for it in ns)
                    update(ns,s,(j+2*(4-i)+k)*costs[i])
                break
        
        # moving out of middle
        for k in range(3):
            if c[k]==-1:
                continue
            i=c[k]
            j=ab(v[i],i)
            if j==-1:
                continue
            if all(it==-1 for it in c[i:k]+c[k+1:i]):
                tmp=deepcopy(v); cc=copy(c);
                tmp[i][j]=i; cc[k]=-1;
                
                ns=tmp+[a,b,cc]
                ns=tuple(tuple(it) for it in ns)
                update(ns,s,(j+2*(abs(k-i)+(k>=i)))*costs[i])
        
print(dist[((0,0,0,0),(1,1,1,1),(2,2,2,2),(3,3,3,3),(-1,-1),(-1,-1),(-1,-1,-1))])

print(time()-start)
print(len(visited))
