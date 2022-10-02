N, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# [a, b]
root = [True, True]
for i in range(1, N):
    an = A[i]
    bn = B[i]
    an1 = A[i-1]
    bn1 = B[i-1]
    
    doneA = False
    doneB = False
    if (abs(an - an1) <= K and root[0]) or (abs(an - bn1) <= K and root[1]) :
        doneA = True
    if (abs(bn - bn1) <= K and root[1]) or (abs(bn - an1) <= K and root[0]):
        doneB = True

    root[0] = doneA
    root[1] = doneB
    
if any(root):
    print('Yes')
else:
    print('No')