'''
★ 確率DPと呼ばれるジャンル

動的計画法（Dynamic Programming）  
回答参考ページ：  
https://zenn.dev/m193h/articles/35738abd5ef80bb8edbc  
https://qiita.com/tefuxu/items/42d3c0be111d7d76a101  
https://note.com/ktsukuda/n/n1bf96eea2f0c
'''
import sys

X, Y, Z  = map(int, input().split())

sys.setrecursionlimit(10 ** 6) #再帰数上限の引き上げ

def dfs(x, y, z): # メモ化再帰
    if dp[x][y][z] >= 0: # 既に値がわかっている場合はそのまま返す.
        ret = dp[x][y][z]
    else : # 値がわかっていない場合、漸化式により値を求める.
        ret = 0
        S = x + y + z
        ret += x / S * (dfs(x+1, y, z) + 1)
        ret += y / S * (dfs(x, y+1, z) + 1)
        ret += z / S * (dfs(x, y, z+1) + 1)
        dp[x][y][z] = ret
    return ret

M = 100
dp = [[[-1] * (M + 1) for _ in range(M + 1)] for _ in range(M + 1)]

# 終端条件（初期化）
for i in range(X, M + 1):
    for j in range(Y, M + 1):
        for k in range(Z, M + 1):
            if i == M or j == M or k == M:
                dp[i][j][k] = 0
# dp(X, Y, Z)が求める答え
print(dfs(X, Y, Z))