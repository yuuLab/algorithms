import math

N, M = map(int, input().split())
A = sorted(list(map(int, input().split())))

if M == N:
    print(0)
    exit()
if M == 0 :
    print(1)
    exit()
distance = [A[0] - 1] if A[0] -1 != 0 else []
for i in range(len(A)):
    if i == len(A) - 1:
        m = N - A[i]
        if m != 0 :
            distance.append(m) 
    else:
        m = A[i + 1] - A[i] - 1
        if m != 0:
            distance.append(m)
            
stamp = min(distance)

ans = sum([math.ceil(i / stamp) for i in distance])
print(ans)