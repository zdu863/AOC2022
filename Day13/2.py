with open('input.txt','r') as f:
    data=f.read().splitlines()

from functools import cmp_to_key

def compare(l1,l2):
    if type(l1)==int and type(l2)==int:
        if l1<l2:
            return -1
        if l1>l2:
            return 1
        else:
            return 0
    if type(l1)==list and type(l2)==list:
        for i,j in zip(l1,l2):
            if compare(i,j)==-1:
                return -1
            if compare(i,j)==1:
                return 1
        if len(l1)<len(l2):
            return -1
        if len(l1)>len(l2):
            return 1
        return 0
    if type(l1)==int and type(l2)==list:
        return compare([l1],l2)
    if type(l1)==list and type(l2)==int:
        return compare(l1,[l2])
        
ls = [[[2]],[[6]]]
for line in data:
    if line:
        ls.append(eval(line))
        
arr = sorted(ls, key=cmp_to_key(compare)) 

ans=1
for ind,it in enumerate(arr,1):
    if it==[[2]] or it==[[6]]:
        ans*=ind
print(ans)




    
