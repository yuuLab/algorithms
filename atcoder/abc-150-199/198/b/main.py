N = input()
idx = float('INF')
for i in range(1, len(N)+1):
    if N[-i] != '0':
        break
    idx = -(i)
if idx != float('INF'):
    N = N[:idx]
for i in range(len(N)//2):
    if N[i] != N[-i-1]:
        print('No')
        exit()
print('Yes')