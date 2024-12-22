with open('input.txt','r') as f:
    data=f.read().splitlines()

mat = []
for line in data:
    tmp=[]
    for c in line:
        tmp.append(int(c))
    mat.append(tmp.copy())

for line in mat:
    print(line)

seen = set()
m,n = len(mat),len(mat[0])

for i in range(m):
    c_max = -1
    for j in range(n):
        if mat[i][j]>c_max:
            c_max=mat[i][j]
            seen.add((i,j))
    c_max=-1
    for j in range(n-1,-1,-1):
        if mat[i][j]>c_max:
            c_max=mat[i][j]
            seen.add((i,j))
            
for j in range(n):
    c_max = -1
    for i in range(m):
        if mat[i][j]>c_max:
            c_max=mat[i][j]
            seen.add((i,j))
    c_max=-1
    for i in range(m-1,-1,-1):
        if mat[i][j]>c_max:
            c_max=mat[i][j]
            seen.add((i,j))
            
print(len(seen))
print(m,n)
