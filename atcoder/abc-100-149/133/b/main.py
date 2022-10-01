import math

N, D = map(int, input().split())
X = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        tmp = 0
        for k in range(D):
            tmp += (X[i][k] - X[j][k])**2
        ans += 1 if math.sqrt(tmp).is_integer() else 0

print(ans)