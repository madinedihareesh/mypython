from collections import deque

L=[1,2,3,4,5,6,7]
d=deque(L)
d.append(8)
print(d)
d.appendleft(9)
print(d)
d.extend([10,11,12])
print(d)
d.extendleft([13,14,15])
print(d)
d.rotate(5)
print(d[0])