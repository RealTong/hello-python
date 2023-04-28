from collections import namedtuple

Point = namedtuple('Point',['x','y'])
p = Point(1,2)
print(p.x)

print(isinstance(p,Point))

print(isinstance(p,tuple))