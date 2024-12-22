from functools import lru_cache
with open('input.txt','r') as f:
    data=f.read().splitlines()

d = {}
for line in data:
    l = line.replace(' ','')
    n,v = l.split(':')
    d[n]=v

# print(d)

@lru_cache()
def val(name):
    if d[name].isnumeric():
        return int(d[name])
    for i,s in enumerate(['+','-','*','/']):
        if s in d[name]:
            a,b = d[name].split(s)
            return eval('val(a)'+s+'val(b)')

print(val('root'))
# print(val('zhfp'))
# print(val('hghd'))
