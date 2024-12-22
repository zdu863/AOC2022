with open('input.txt','r') as f:
    data=f.read().splitlines()

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

ind = 1
ans = 0
comp=[]
for line in data:
    if not line:
        if compare(comp[0],comp[1])==-1:
            ans+=ind
        ind+=1
        comp = []
        continue
    else:
        comp.append(eval(line))

print(ans)




    
