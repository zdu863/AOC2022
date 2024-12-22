with open('4.txt','r') as f:
    data=f.read().splitlines()

cnt = 0
for line in data:
    f,s = line.split(',')
    fl,fh = map(int,f.split('-'))
    sl,sh = map(int,s.split('-'))
    
    if (fl<=sl and fh>=sh) or (sl<=fl and sh>=fh):
        cnt+=1

print(cnt)
    
