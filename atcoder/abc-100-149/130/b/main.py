N, X = map(int, input().split())
L = list(map(int, input().split()))

D = 0
ans = 1
for i in range(2, N+2):
    D += L[i-2]
    if D > X:
        break
   
    ans += 1
        
print(ans)