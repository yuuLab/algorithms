import itertools

N = int(input())
A = list(map(int, input().split()))

MOD = 10**9 + 7
result = 0
A_accu = list(itertools.accumulate(A))
for i in range(N-1):
    result += A[i] * (A_accu[N-1] - A_accu[i])

print(result % MOD)