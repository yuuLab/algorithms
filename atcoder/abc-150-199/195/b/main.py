import math
A, B, W = map(int, input().split())

upper = int(math.floor(1000*W / A))
lower = int(math.ceil(1000*W / B))

if lower > upper:
    print("UNSATISFIABLE")
else:
    print(lower, upper)

