# 最大公約数を利用した問題

import math

a, b, c = map(int, input().split())
a_b_gcd = math.gcd(a, b)
b_c_gcd = math.gcd(b, c)
gcd = math.gcd(a_b_gcd, b_c_gcd)

print(a//gcd + b//gcd + c//gcd - 3)