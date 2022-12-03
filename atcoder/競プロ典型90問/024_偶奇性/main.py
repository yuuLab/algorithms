# 偶奇性（パリティ）を利用した問題

N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

k = 0
for i in range(N):
    a = A[i]
    b = B[i]
    if a == b:
        continue
    if a < b:
        k += b - a
    else:
        k += a - b
        
if k <= K and (K-k)%2 == 0:
    print('Yes')
else:
    print('No')