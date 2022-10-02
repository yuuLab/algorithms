H, W, X, Y = map(int, input().split())
S = [input() for _ in range(H)]

ans = 0
for i in range(Y-2, -1, -1):
    if S[X-1][i] == '.':
        ans += 1
    else:
        break
for i in range(Y, W):
    if S[X-1][i] == '.':
        ans += 1
    else:
        break
for i in range(X-2, -1, -1):
    if S[i][Y-1] == '.':
        ans += 1
    else:
        break
for i in range(X, H):
    if S[i][Y-1] == '.':
        ans += 1
    else:
        break
            
if S[X-1][Y-1] == '.':
    print(ans+1)
else:
    print(ans)