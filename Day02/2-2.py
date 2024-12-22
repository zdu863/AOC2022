h,d=0,0
score = {'A':1,'B':2,'C':3}
tot = 0
with open('2.txt','r') as f:
    for line in f:
        o,m=line.split()
        so = score[o]

        if m=='X':
            sm=(so-2)%3+1
            tot+=sm
        elif m=='Y':
            sm=so
            tot+=sm+3
        else:
            sm=so%3+1
            tot+=sm+6
print(tot)
