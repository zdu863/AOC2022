h,d=0,0
d = {'X':'A','Y':'B','Z':'C'}
score = {'A':1,'B':2,'C':3}
tot = 0
with open('2.txt','r') as f:
    for line in f:
        o,m=line.split()
        m = d[m]
        so,sm = score[o],score[m]
        if o==m:
            tot+=3+sm
        elif sm-1==so%3:
            tot+=6+sm
        else:
            tot+=sm
        # print(tot)
print(tot)
