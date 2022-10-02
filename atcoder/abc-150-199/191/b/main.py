N, X = map(int, input().split())
A = list(map(int, input().split()))

ans = []
flag = False
for i in range(N):
    if A[i] != X:
        ans.append(A[i])
        flag = True
if flag:
    print(*ans)
else:
    print('')