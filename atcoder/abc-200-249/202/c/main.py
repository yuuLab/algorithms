N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

l = [[0] for _ in range(N)]
for i in range(N):
    s = B[C[i]-1]
    l[s-1][0] += 1
ans = 0
for i in range(N):
    ans += l[A[i]-1][0]

print(ans)