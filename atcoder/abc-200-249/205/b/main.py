n = int(input())
A = list(map(int, input().split()))

sheet = [False for _ in range(n)]
for a in A:
    sheet[a-1] = True
if all(sheet):
    print('Yes')
else:
    print('No')