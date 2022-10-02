N = int(input())
A = list(map(int, input().split()))

total = 0
for i in range(1, N):
    if A[i] < A[i-1]:
        step = A[i-1] - A[i]
        A[i] += step
        total += step
print(total)