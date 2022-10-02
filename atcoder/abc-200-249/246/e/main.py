from collections import deque

N = int(input())
Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
board = [list(input()) for _ in range(N)]
    
ax = Ax - 1
ay = Ay - 1
bx = Bx - 1
by = By - 1

# 全ての地点までの距離をINFで初期化
INF = 10**9
sheet = [[INF] * N for _ in range(N)]
# スタート地点
sheet[ax][ay] = 1

# 移動四方向のベクトル
dx = [1, 1, -1, -1]
dy = [1, -1, 1, -1]
directions = [0, 1, 2, 3] #どの方向に進んでいたかを表す (同じ方向に進む場合コストは0)

# 両端キュー
q = deque()
for i in range(4):
    q.append([ax, ay, i])

while q:
    x, y, direction = q.popleft()
   
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        nd = directions[i]
        # 盤外ならスキップ
        if not (0 <= ny < N and 0 <= nx < N):
            continue
        # ボーンならスキップ
        if board[nx][ny] == '#':
            continue
        # 同じ方向に進む場合はコスト0 (キューの先頭に入れる)
        if direction == nd:
            if sheet[nx][ny] > sheet[x][y]:
                sheet[nx][ny] = sheet[x][y]
                q.appendleft([nx, ny, nd])
        else:
            # 別の方向に進む場合はコスト＋1 (キューの末尾に入れる)
            if sheet[nx][ny] > sheet[x][y] + 1:
                sheet[nx][ny] = sheet[x][y] + 1
                q.append([nx, ny, nd])
        

ans = -1 if sheet[bx][by] == INF else sheet[bx][by]
print(ans)
