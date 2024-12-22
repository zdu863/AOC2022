with open('3.txt','r') as f:
    data=f.read().splitlines()

import string
a = list(string.ascii_lowercase)
A = list(string.ascii_uppercase)
d = dict(zip(a, list(range(1,27))))
D = dict(zip(A, list(range(27,53))))

ans=0
for line in data:
    tot=len(line)
    f,l = line[:tot//2],line[tot//2:]
    for c in f:
        if c in l:
            if c in a:
                ans+=d[c]
            else:
                ans+=D[c]
            break
print(ans)
