a = list(map(int, input().split()))
ans = a[0]
for i in range(2):
    ans = a[ans]
print(ans)