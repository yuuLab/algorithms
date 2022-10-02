# BFSで解く
from collections import deque

H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

que = deque()
que.append([0, 0])

# 初期化
dist = [[0]*W for _ in range(H)]
dist[0][0] = 1

while que:
    i, j = que.pop()
    for i2, j2 in [[i, j+1], [i+1, j]]:
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
            
        if grid[i2][j2] == '#':
            continue
        
        if dist[i2][j2] < dist[i][j] + 1:
            dist[i2][j2] = dist[i][j] + 1
            que.append([i2, j2])
            
ans = 1
for d in dist:
    ans = max(ans, max(d))
    
print(ans)