A, B = map(int, input().split())

import math

x = math.sqrt(A**2 / (A**2 + B**2))
y = math.sqrt(B**2 / (A**2 + B**2))
print(x, y)