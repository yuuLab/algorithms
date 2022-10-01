import math

A, B, C, D = map(int, input().split())

# A未満を調べるために-1
A -= 1

lcm = C * D // math.gcd(C, D)
under_b = B - (B//C + B//D - B//lcm)
under_a = A - (A//C + A//D - A//lcm)

print(under_b - under_a)