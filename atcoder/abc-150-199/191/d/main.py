from decimal import Decimal
import math

X, Y, R = [Decimal(x) for x in input().split()]

x_max = math.floor(X + R) #切り捨て
x_min = math.ceil(X - R) #切り上げ

ans = 0
# x座標（整数）に対応する円周上のy座標（2点）を円の公式から求め、その間に存在し、y座標が整数である個数を求めていく
for x in range(x_min, x_max+1):
    p = Decimal(R**2 - (x - X)**2).sqrt()
    top = math.floor(Y + p)
    bottom = math.ceil(Y - p)
    ans += top - bottom + 1
print(ans)