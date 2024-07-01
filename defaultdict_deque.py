from collections import namedtuple

# similar to struct in C

Point =namedtuple("Point","x,y")
pt=Point(1,-4)

print(pt.x,pt.y)


from collections import defaultdict
d=defaultdict(int)
d['a']=1
d['b']=3
print(d['c'])
print(d['b'])
# in normal dictionary it doesn't have default value like 0 in here

from collections import deque
# fifo
de=deque()
de.append(1)
de.append(2) 
# appends from left
print(de)
de.appendleft(4)
# de.appendright(5) doesn't exist
print(de)
de.popleft()
print(de)
de.extendleft([4,5,6])
de.extend([6,7,8])
print(de)

de.rotate(2)
print(de)
de.rotate(-1)
print(de)