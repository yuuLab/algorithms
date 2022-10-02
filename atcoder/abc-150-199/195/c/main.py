N = int(input())

ans = 0
if N < 1000:
    print(ans)
else:
    i = 1000
    while i <= N:
        ans += N - i + 1
        i = i * 1000
    print(ans)