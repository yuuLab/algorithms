N = int(input())
A = list(map(int, input().split()))

N = int(input())
A = list(map(int, input().split()))

def has_bit(n, i):
    return (n & (1<<i) > 0)

ans = float('INF')
for n in range(1 << N):
    cand = 0
    tmp = 0
    # i番目とi+1番目を区切るとき、i+1番目を1とする
    for i in range(N):
        if has_bit(n, i):
            cand = cand ^ tmp
            tmp = A[i]
        else:
            tmp = tmp | A[i]
    cand = cand ^ tmp
    ans = min(ans, cand)
print(ans)