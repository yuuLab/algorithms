import sys
sys.setrecursionlimit(10 ** 6)

N, Q = map(int, input().split())
X = list(map(int, input().split()))

# 各頂点に辺を張る
graph = [[] for _ in range(N)]
for i in range(N-1):
    A, B = map(int, input().split())
    A -= 1
    B -= 1
    graph[A].append(B)
    graph[B].append(A)

# iの部分木に含まれる頂点に書かれた整数のうち、大きい方から順にK個入った配列
sheet = [[] for _ in range(N)]
# 訪れた頂点を保持
set_vertex = set()
# Kの最大値
k_max = 20

# DFSで探索し、sheetを完成させる。
def dfs(x: int) -> list:
    set_vertex.add(x)
    for v in graph[x]:
        if v in set_vertex:
            continue
        sheet[x] += dfs(v)
    
    sheet[x].append(X[x])
    sheet[x].sort(reverse=True)
    return sheet[x][:k_max]

dfs(0)

# クエリに対してO(1)で答えることが可能。
for _ in range(Q):
    v, k = map(int, input().split())
    print(sheet[v-1][k-1])