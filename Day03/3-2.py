with open('3.txt','r') as f:
    data=f.read().splitlines()

import string
a = list(string.ascii_lowercase)
A = list(string.ascii_uppercase)
d = dict(zip(a, list(range(1,27))))
D = dict(zip(A, list(range(27,53))))

ans=0
cnt=0
cur=[]
for line in data:
    tl = set(line)
    cur.append(tl)
    cnt+=1
        
    if cnt==3:
        tmp = set(a+A)
        for s in cur:
            tmp = tmp.intersection(s)
        c = tmp.pop()
        if c in a:
            ans+=d[c]
        else:
            ans+=D[c]
        cnt=0
        cur=[]
print(ans)
