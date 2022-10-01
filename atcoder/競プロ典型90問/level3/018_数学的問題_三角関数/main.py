import math

t = int(input())

l, x, y = map(int,input().split())
r = l / 2

q = int(input())

p = math.pi

for i in range(q):
    e = int(input())
    angle = 2 * p * e / t
    ye = - r * math.sin(angle)
    ze = r - r * math.cos(angle)
    tmp = x**2 + (y - ye)**2
    dist = pow(tmp, 0.5)
    dep = math.atan2(ze, dist)

    print(math.degrees(dep))