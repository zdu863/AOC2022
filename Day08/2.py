with open('input.txt','r') as f:
    data=f.read().splitlines()

mat = []
for line in data:
    tmp=[]
    for c in line:
        tmp.append(int(c))
    mat.append(tmp.copy())


seen = set()
m,n = len(mat),len(mat[0])

score = [[1 for _ in range(n)] for _ in range(m)]


for i in range(1,m-1):
    q = [[mat[i][0],0]]
    for j in range(1,n-1):
        while q and mat[i][j]>q[-1][0]:
            q.pop()
        if q:
            score[i][j]*=j-q[-1][1]
        else:
            score[i][j]*=j
        q.append([mat[i][j],j])
        
    q = [[mat[i][-1],n-1]]
    for j in range(n-1,-1,-1):
        while q and mat[i][j]>q[-1][0]:
            q.pop()
        if q:
            score[i][j]*=q[-1][1]-j
        else:
            score[i][j]*=n-1-j
        q.append([mat[i][j],j])

for j in range(1,n-1):
    q = [[mat[0][j],0]]
    for i in range(1,m-1):
        while q and mat[i][j]>q[-1][0]:
            q.pop()
        if q:
            score[i][j]*=i-q[-1][1]
        else:
            score[i][j]*=i
        q.append([mat[i][j],i])
        
    q = [[mat[-1][j],m-1]]
    for i in range(m-1,-1,-1):
        while q and mat[i][j]>q[-1][0]:
            q.pop()
        if q:
            score[i][j]*=q[-1][1]-i
        else:
            score[i][j]*=m-1-i
        q.append([mat[i][j],i])
        
print(max(max(r) for r in score))
