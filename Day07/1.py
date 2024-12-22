with open('input.txt','r') as f:
    data=f.read().splitlines()

ind = 0
ans = 0
def make_tree():
    global ind,ans
    cnt = 0
    ind += 2
    n_sub = 0
    ret = 0
    while ind<len(data):
        line=data[ind]
        a,*_ = line.split(' ')
        if a=='$':
            break
        if a=='dir':
            n_sub+=1
        else:
            ret+=int(a)
        ind+=1

    for _ in range(n_sub):
        ret += make_tree()
    ind+=1
    if ret<=100000:
        ans+=ret
    return ret
    
make_tree()
print(ans)
        
