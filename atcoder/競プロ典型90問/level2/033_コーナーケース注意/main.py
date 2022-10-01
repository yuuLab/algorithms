H, W = map(int, input().split())

ans = 0

if H == 1:
    ans = W
elif W == 1:
    ans = H
else:
    for i in range(1, H+1):
        for j in range(1, W+1):
            if i%2 == 1 and j%2 == 1:
                ans += 1
print(ans)