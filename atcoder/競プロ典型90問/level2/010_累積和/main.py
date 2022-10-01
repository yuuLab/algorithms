# 累積和を利用した問題

import itertools

N = int(input())

scores = [[0] * N for _ in range(2)]
for i in range(N):
    c, p = map(int, input().split())
    scores[c-1][i] = p
    
one = list(itertools.accumulate(scores[0]))
two = list(itertools.accumulate(scores[1]))

Q = int(input())
for i in range(Q):
    l, r = map(int, input().split())

    if l == 1:
        # index補正
        r -= 1
        print(one[r], end=' ')
        print(two[r])
    else:
        # index補正
        l -= 1
        r -= 1
        # 累積和の配列を利用して算出する。
        # lからr番目の合計値 = (rまでの累積和)-(l-1までの累積和)
        print(one[r] - one[l-1], end=' ')
        print(two[r] - two[l-1])