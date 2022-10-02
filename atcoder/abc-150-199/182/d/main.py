from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

a = list(accumulate(A))

x = 0
m = 0
ans = 0

for i in range(N):
    m = max(a[i], m)
    ans = max(ans, x+m)
    x += a[i]
print(ans)