N = int(input())

ans = float('inf')
flag = False
for _ in range(N):
    A, P, X = map(int, input().split())
    if X >= 1 and X - A >= 1:
        if ans > P:
            ans = P
            flag = True
if not flag:
    ans = -1

print(ans)