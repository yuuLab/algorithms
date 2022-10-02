"""
動的計画法
dp[i][j]:=数列の先頭からi項まで決めた際に、総和がjであるような数列の決め方の総数とする。
※数列を先頭から決めていく際、覚えておくべき必要があるものはその時点での数列の総和のみであり、具体的に各要素の値が何であったかは捨象してよい。
"""

N, M, K = map(int, input().split())
dp = [[0]*(K+1) for _ in range(N+1)]
dp[0][0] = 1

for i in range(N):
    for j in range(K):
        for k in range(1, M+1):
            if j+k <= K:
                dp[i+1][j+k] += dp[i][j]
                
ans = sum(dp[N])
print(ans % 998244353)