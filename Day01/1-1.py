c_max=-1
cur=0
inc=0
with open('1.txt','r') as f:
    for line in f:
        if line == '\n':
            c_max = max(c_max,cur)
            cur=0
            continue
        cur+=int(line)

print(c_max)
