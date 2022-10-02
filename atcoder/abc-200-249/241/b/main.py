N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

done = [False] * N
for i in range(M):
    length = B[i]
    isNG = True
    for j in range(N):
        if length == A[j] and not done[j]:
            done[j] = True
            isNG = False
            break
    if isNG:
        print('No')
        exit()
        
    
print('Yes') 