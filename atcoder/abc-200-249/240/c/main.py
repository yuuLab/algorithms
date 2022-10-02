N, X = map(int, input().split())

# dp[i][j]:i回ジャンプを行った時点で座標jの位置にいることが可能なら1、不可能なら0
dp = [[0] * (X+1) for _ in range(N+1)]
# dp初期値
dp[0][0] = 1

for i in range(1, N+1):
    a, b = map(int, input().split())
    li = dp[i-1]
    for j in range(X+1):
        if li[j] == 0:
            continue
        if a + j <= X:
            dp[i][a+j] = 1
        if b + j <= X:
            dp[i][b+j] = 1
        if a + j > X and b + j > X:
            break

if dp[N][X] == 1:
    print('Yes')
else:
    print('No')