x = int(input())

if x % 10 == 0:
    print(x//10)
elif x < 0:
    ans = abs(x) // 10
    print(-1 * (ans+1))
else:
    ans = abs(x) // 10
    print(ans)