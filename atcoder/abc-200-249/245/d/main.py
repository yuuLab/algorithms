# numpyで簡単に解くパターン
import numpy as np

N, M = map(int, input().split())
A = list(map(int, input().split()))
C = list(map(int, input().split()))

x = np.array(C[::-1])
y = np.array(A[::-1])
d = np.polydiv(x, y)
ans = []
for i in list(d[0])[::-1]:
    ans.append(int(i))
print(*ans)