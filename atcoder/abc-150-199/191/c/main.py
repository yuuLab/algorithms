H, W = map(int, input().split())
L = [list(map(str, input())) for i in range(H)]

ans = 0
for i in range(0, H-1):
    for j in range(0, W-1):
        count = 0
        if L[i][j] == '#':
            count += 1
        if L[i][j+1] == '#':
            count += 1   
        if L[i+1][j] == '#':
            count += 1
        if L[i+1][j+1] == '#':
            count += 1    
        if count == 1 or count == 3:
            ans += 1
print(ans)