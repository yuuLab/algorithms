# 一見TLEになりそうだが、nC5で1/120N*5となり、定数倍が非常に軽いので十分間に合う

N, P, Q = map(int, input().split())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i):
        for k in range(j):
            for l in range(k):
                for m in range(l):
                    ans += 1 if A[i]%P*A[j]%P*A[k]%P*A[l]%P*A[m]%P == Q else 0
                    
print(ans)