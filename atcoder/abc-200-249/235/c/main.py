N, Q = map(int, input().split())
A = list(map(int, input().split()))

m = {}
for i in range(N):
    a = A[i]
    if m.get(a) is None:
        m[a] = [i]
    else:
        l = m.get(a)
        l.append(i)
        m[a] = l

for i in range(Q):
    x, k = map(int, input().split())
    l = m.get(x)
    if l is not None and len(l) >= k:
        print(l[k-1] + 1)
    else:
        print(-1)