N = int(input())
S = input()

from collections import deque

# 逆から考えて、両端キューで解く
A = [N]
dq = deque(A)
for i in range(N, 0, -1):
    if S[i-1] == 'R':
        dq.appendleft(i-1)
    else:
        dq.append(i-1)
        
print(*dq)