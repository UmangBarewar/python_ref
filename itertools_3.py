from itertools import count,cycle,repeat

for _ in count(1):
    print(_)
    if _==100:
        break
a=[1,2,3,4,5]
for _ in cycle(a):
    print(_)
    
for _ in repeat(1,4):
    print(_)
    