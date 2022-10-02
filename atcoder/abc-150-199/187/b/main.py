N = int(input())
M = [list(map(int, input().split())) for i in range(N)]

count = 0
for i in range(len(M)):
    for j in range(len(M)):
        if i >= j:
            continue
        li = (M[j][1] - M[i][1]) / (M[j][0] - M[i][0])
        if li <= 1 and li >= -1:
            count += 1
print(count)