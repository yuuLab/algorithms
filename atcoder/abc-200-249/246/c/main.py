N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort(reverse=True)
remain = []
ans = 0
for i in range(N):
    price = A[i]
    if K > 0:
        used = min((price // X), K)
        tmp = price - (X * used)
        remain.append(tmp)
        ans += tmp
        K -= used
    else:
        remain.append(price)
        ans += price

# クーポンを使い切っている場合、そのまま出力
if K == 0:
    print(ans)
else:
    # クーポンが余っているなら価格が高いものから使用していく
    remain.sort(reverse=True)
    for i in range(N):
        if K > 0:
            ans -= remain[i]
            K -= 1
        else:
            break
    print(ans)