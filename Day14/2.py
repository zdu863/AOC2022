with open('input.txt','r') as f:
    data=f.read().splitlines()

n=2000
y_max = 161

mat = [[0 for _ in range(n)] for _ in range(y_max+3)]
delta = 500

for line in data:
    l = line.replace(' ','')
    arr = l.split('->')
    lx,ly = -1,-1
    for ps in arr:
        x,y = map(int,ps.split(','))
        x+=delta
        
        y_max= max(y,y_max)
        
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

mat[-1] = [1 for _ in range(n)]
# print(y_max)
# for l in mat[:10]:
#     print(l[494:504])

end=False
blocked=False

n_sand = 0
while True:
    sy,sx = 0,delta+500
    if mat[sy][sx]==1:
        blocked = True
        break
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
                break
        if sx<=1 or sx>=n-1:
            end=True
            break
    if end:
        break

# for l in mat[:12]:
    # print(l[500+494:500+504])

print(n_sand)
print(blocked,end)
