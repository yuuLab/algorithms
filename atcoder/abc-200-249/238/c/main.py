N = int(input())
def sumN(n):
    return n*(n+1)//2

ans = 0
d = len(str(N))
for i in range(1, 20):
    if i == 1:
        if N < 10:
            ans += sumN(int(str(N)))
        else:
            ans += sumN(9)
    elif i < d:
        ans += sumN((10**i) - 10**(i-1))
    elif i == d:
        ans += sumN(N - 10**(i-1) + 1)
    else:
        break
        
print(ans % 998244353)