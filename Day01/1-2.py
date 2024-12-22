cal = []
cur=0
with open('1.txt','r') as f:
    for line in f:
        if line == '\n':
            cal.append(cur)
            cur=0
            continue
        cur+=int(line)
        
cal.sort(reverse=True)

print(sum(cal[:3]))
