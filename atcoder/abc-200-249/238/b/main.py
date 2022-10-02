N = int(input())
A = list(map(int, input().split()))

cut = [0, 360]
tmp = 0
for a in A:
    tmp += a
    tmp %= 360
    cut.append(tmp)
cut.sort()

angle = [cut[i+1] - cut[i] for i in range(len(cut)-1)]
print(max(angle))