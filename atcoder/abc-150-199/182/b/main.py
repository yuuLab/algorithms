N = int(input())
A = list(map(int, input().split()))

ans = -1
mx = 0

for x in range(2, 1001):
    s = sum(a % x == 0 for a in A)
    if mx < s:
        mx = s
        ans = x
        
print(ans)