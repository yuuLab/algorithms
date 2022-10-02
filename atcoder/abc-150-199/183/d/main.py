import itertools

N, W = map(int, input().split())
li = [0 for _ in range(0, 2*10**5 + 1)]
for _ in range(N):
    S, T, P = map(int, input().split())
    # SでP増え、TでP減ると考える（いもす法）
    li[S] += P
    li[T] -= P
li_accu = itertools.accumulate(li)
if max(li_accu) > W:
    print('No')
else:
    print('Yes')