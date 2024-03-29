N = int(input())

MOD = 998244353

dp = [[0]*11 for _ in range(N+1)]
for i in range(1, 10):
    # 1桁目は1~9の1通り
    dp[1][i] = 1

for i in range(1, N):
    for j in range(1, 10):
        dp[i+1][j] = (dp[i][j-1] + dp[i][j] + dp[i][j+1]) % MOD
        
print(sum(dp[N]) % MOD)
