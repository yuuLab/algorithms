# DFSで解く
H, W = map(int, input().split())
grid = [list(input()) for _ in range(H)]

dist = [[0]*W for _ in range(H)]
dist[0][0] = 1

def dfs(i, j):
    for i2, j2 in [[i, j+1], [i+1, j]]:
        if not (0 <= i2 < H and 0 <= j2 < W):
            continue
        
        if grid[i2][j2] == '#':
            continue
        # 最大値を求めたいため、大きくなるならば更新
        if dist[i2][j2] < dist[i][j] + 1:
            dist[i2][j2] = dist[i][j] + 1
            dfs(i2, j2)
dfs(0, 0)       
ans = 1
for d in dist:
    ans = max(ans, max(d))
    
print(ans)