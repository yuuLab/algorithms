N, M = map(int, input().split())
S = list(input().split())
T = list(input().split())

tmp = 0
for i in range(0, N):
    if S[i] == T[tmp]:
        print('Yes')
        tmp += 1
    else:
        print('No')
        