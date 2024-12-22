from z3 import Int, Optimize, sat

with open('input.txt') as f:
    data = f.read().splitlines()

s = Optimize()
for line in data:
    l = line.replace(' ','')
    n,v = l.split(':')
    
    if n=='humn':
        continue

    if v.isdigit():
        s.add(Int(n) == int(v))
    else:
        for sign in ['+','-','*','/']:
            if sign in v:
                a,b = v.split(sign)
                if n=='root':
                    s.add(Int(a) == Int(b))
                else:
                    s.add(eval('Int(n) == Int(a)' + sign + 'Int(b)'))
                break

assert s.check() == sat
m = s.model()
print(m[Int('humn')])
