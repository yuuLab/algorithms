# 解法1
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())

G = [[] for i in range(N)]
# G[i] は都市iから道路で直接繋がっている都市のリスト
for i in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B-1)
    
def dfs(v):
    if seen[v]:
        # 同じ頂点を2度以上調べないためのreturn
        return
    seen[v] = True
    for g in G[v]:
        dfs(g)
        
ans = 0
# 都市iからスタートする場合
for i in range(N):
    seen = [False] * N
    # temp[j] は都市jに到達可能かどうかを表す
    dfs(i)
    ans += sum(seen)
print(ans)