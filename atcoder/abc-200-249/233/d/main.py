from collections import Counter
from itertools import accumulate

N, K = map(int, input().split())
A = list(map(int, input().split()))

S = list(accumulate(A))
# l=0の場合に備えて、0で初期化
counter = Counter([0])

ans = 0

# 1<=l<=r かつ S[l-1]=S[r]-K を満たすlの個数を求める
for r in range(N):
    # m = S[r] - K である連続部分列が今まで何回出てきたかを調べる
    m = S[r] - K
    ans += counter[m]
    if counter[m] > 0:
        print(r)
    counter[S[r]] += 1
    
print(ans)