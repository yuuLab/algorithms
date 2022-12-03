# 全探索で解くことが可能
# O(H*W)

H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

ans = [[0]*W for _ in range(H)]

# 各行の合計値
w_sum = []
for a in  A:
    w = sum(a)
    w_sum.append(w)

# 各列の合計値
h_sum = []
for i in range(W):
    h = 0
    for j in range(H):
        h += A[j][i]
    h_sum.append(h)
    
# 各行列の計算結果をまとめて出力する。
for i in range(H):
    for j in range(W):
        ans = w_sum[i] + h_sum[j] - A[i][j]
        if j != W-1:
            print(ans, end=' ')
        else:
            # 最後の行は改行する。
            print(ans)