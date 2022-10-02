from itertools import accumulate

N = int(input())

ans = 0
l = [i for i in range(0, 10**6+1)]
l_accu = list(accumulate(l))


for _ in range(N):
    A, B = map(int, input().split())
    ans += l_accu[B] - l_accu[A-1]
print(ans)