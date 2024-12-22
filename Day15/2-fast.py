from time import time
start=time()
arr=[7,12,1,0,16,2]

origin={a:i for i,a in enumerate(arr)}
last={}

lst=arr[-1]
for i in range(len(arr),30000000):
    if lst not in last:
        spoken=0
    else:
        spoken=last[lst]-origin[lst]
    if spoken in last:
        last[spoken],origin[spoken]=i,last[spoken]
    elif spoken in origin:
        last[spoken]=i
    else:
        origin[spoken]=i
    lst=spoken
print(spoken)
print(time()-start)
