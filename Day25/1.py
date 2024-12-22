from copy import deepcopy
with open('input.txt','r') as f:
    data=f.read().splitlines()


def snafu(s):
    ans=0
    for i,c in enumerate(reversed(s)):
        if c.isdigit():
            ans+=int(c)*5**i
        elif c=='-':
            ans+=(-1)*5**i
        elif c=='=':
            ans+=(-2)*5**i
    return ans
    
ans=0
for line in data:
    ans+=snafu(line)

def rev(num):
    ret = []
    while num>=1:
        r = num%5
        if 0<=r<=2:
            ret.append(str(r))
        elif r==3:
            ret.append('=')
            num+=2
        elif r==4:
            ret.append('-')
            num+=1
        num//=5
    return ''.join(reversed(ret))

print(rev(ans))
    
    

    
    
