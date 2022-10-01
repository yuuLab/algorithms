L, R = map(int, input().split())

# L~RもしくはL+2019の範囲で全探索する。
m = L + min(R-L, 2019)
ans = 2019
for i in range(L, m):
    for j in range(i+1, m+1):
        ans = min((i*j)%2019, ans)

print(ans)