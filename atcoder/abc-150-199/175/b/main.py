N = int(input())
L = list(map(int, input().split()))

ans = 0
length = len(L)
for i in range(length-2):
    for j in range(i+1, length):
        if L[i] == L[j]:
            continue
        for k in range(j+1, length):
            if L[i] == L[k] or L[j] == L[k]:
                continue
            if L[i]+L[j]>L[k] and L[j]+L[k]>L[i] and L[k]+L[i]>L[j]:
                ans += 1
print(ans)