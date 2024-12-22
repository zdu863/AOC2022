# poly='NCOPHKVONVPNSKSHBNPF'
# # poly='NNCB'
# poly=list(poly)

with open('input.txt','r') as f:
    data=f.read().splitlines()

n=2000
mat = [[0 for _ in range(n)] for _ in range(n)]

for line in data:
    l = line.replace(' ','')
    arr = l.split('->')
    lx,ly = -1,-1
    for ps in arr:
        x,y = map(int,ps.split(','))        
        if lx==ly==-1:
            lx,ly = x,y
            continue
        if x==lx:
            for j in range(ly,y+1):
                mat[j][x]=1
            for j in range(y,ly+1):
                mat[j][x]=1
        elif y==ly:
            for i in range(lx,x+1):
                mat[y][i]=1
            for i in range(x,lx+1):
                mat[y][i]=1
        else:
            print('wrong')
        lx,ly = x,y
        
# for l in mat[:10]:
#     print(l[494:504])
# sand = [500,0]

end=False
n_sand = 0
while True:
    sy,sx = 0,500
    while True:
        if mat[sy+1][sx]==0:
            sy+=1
        else:
            if mat[sy+1][sx-1]==0:
                sx-=1
                sy+=1
            elif mat[sy+1][sx+1]==0:
                sx+=1
                sy+=1
            else:
                mat[sy][sx]=1
                n_sand+=1
                # print(sx,sy)
                # for l in mat[:10]:
                #     print(l[494:504])
                break
        if sy>=1999 or sx<=1 or sx>=1999:
            end=True
            break
    if end:
        break
        
print(n_sand)

# rules={}
# for line in data:
#     x,y=line.replace(' ','').split('->')
#     rules[x]=y
# 
# for it in range(10):
#     stk=[]
#     for c in poly:
#         if stk:
#             for k in rules:
#                 if k[0]==stk[-1] and k[1]==c:
#                     stk.append(rules[k])
#                     break
#         stk.append(c)
#     poly=stk.copy()
# 
# from collections import Counter
# 
# cntr=Counter(poly)
# print(max(cntr.values())-min(cntr.values()))
