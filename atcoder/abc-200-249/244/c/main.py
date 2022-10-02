N = int(input())
isUsed = [False] * (2 * N + 1 + 1)
ans = -1
while ans != 0:
    for i in range(1, 2*N+2):
        if not isUsed[i]:
            print(i)
            isUsed[i] = True
            break
    ans = int(input())
    isUsed[ans] = True