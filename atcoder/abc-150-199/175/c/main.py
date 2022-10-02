X, K, D = map(int, input().split())

# すべて一方向に移動してもゼロを超えれないなら、その最終到達点が解
if abs(X) >= K * D:
    print(abs(X) - K * D)
    exit()
    
# 一番ゼロに近づくタイミング（ゼロは超えないで）
q, mod = divmod(abs(X), D)
# 残り移動回数
moveCount = K - q
# 残り移動回数が偶数なら今いる地点が解
if moveCount % 2 == 0:
    print(mod)
# 残り移動回数が奇数ならゼロをちょうど一回跨いだ地点が解
else:
    print(abs(abs(X) - (D * (q + 1))))