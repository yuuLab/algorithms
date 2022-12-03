# 隣接リストを利用する問題

n, m = map(int,input().split())
 
graph = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    graph[a-1].append(b-1)
    graph[b-1].append(a-1)

ans = 0
for i in range(n):
    tmp = 0
    for j in graph[i]:
        if i > j:
            tmp += 1
    if tmp == 1:
        ans += 1

print(ans)