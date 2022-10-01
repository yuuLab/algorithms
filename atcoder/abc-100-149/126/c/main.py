N, K = map(int, input().split())

ans = 0
for i in range(1, N+1):
    x = 0
    tmp = i
    while tmp < K:
        tmp *= 2
        x += 1
    ans += (1/N) * (1/2)**x
    
print(ans)