with open('input.txt','r') as f:
    data=f.read().splitlines()

items = [[83, 88, 96, 79, 86, 88, 70],[59, 63, 98, 85, 68, 72],[90, 79, 97, 52, 90, 94, 71, 70],[97, 55, 62],[74, 54, 94, 76],[58],[66, 63],[56, 56, 90, 96, 68]]

oper = [lambda x:x*5,lambda x:x*11,lambda x:x+2,lambda x:x+5,lambda x:x*x,lambda x:x+4,lambda x:x+6,lambda x:x+7]

div = [11,5,19,13,7,17,2,3] 

tt = [2,4,5,2,0,7,7,4]
ff = [3,0,6,6,3,1,5,1] 

f = 1
for it in div:
    f*=it

n_insp = [0]*8    
for _ in range(10000):
    for i in range(len(items)):
        for it in items[i]:
            n_insp[i]+=1
            w = oper[i](it)
            w = w%f
            # w = w//3
            if w%div[i]==0:
                items[tt[i]].append(w)
            else:
                items[ff[i]].append(w)
        items[i]=[]

n_insp.sort(reverse=True)
print(n_insp[0]*n_insp[1])
        
