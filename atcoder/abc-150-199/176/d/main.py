from collections import deque

H, W = map(int, input().split())
ch, cw = map(int, input().split())
dh_, dw_ = map(int, input().split())

fs = []
for i in range(H):
    r = list(input())
    fs.append(r)

walks = [(-1,0),(1,0),(0,1),(0,-1)]
magics = []
for i in range(-2,3):
    for j in range(-2,3):
        if i==j==0:
            continue
        if (i,j) not in walks:
            magics.append((i,j))

INF = 1 << 50
dps = [[INF]*W for i in range(H)]
dps[ch-1][cw-1] = 0

q = deque([])
q.appendleft((ch-1,cw-1,0))

while len(q)>0:
    h, w, cnt = q.popleft()
    if cnt > dps[h][w]:
        continue
    dps[h][w] = cnt
    
    for dh, dw in walks:
        hn = h + dh
        wn = w + dw
        if 0<=hn<H and 0<=wn<W:
            if dps[hn][wn] != INF:continue
            if fs[hn][wn] == ".":
                q.appendleft((hn, wn, cnt))
                
    for dh, dw in magics:
        hn = h + dh
        wn = w + dw
        if 0<=hn<H and 0<=wn<W:
            if dps[hn][wn] != INF:continue
            if fs[hn][wn] == ".":
                q.append((hn, wn, cnt+1))

ans = dps[dh_-1][dw_-1]
print(ans if ans != INF else -1)